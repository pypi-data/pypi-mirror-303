import datetime

from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

import graphene
from graphene_django import DjangoObjectType
from reversion import create_revision, set_comment, set_user

from aleksis.apps.alsijil.models import NewPersonalNote, ParticipationStatus
from aleksis.apps.alsijil.schema.personal_note import PersonalNoteType
from aleksis.apps.kolego.models import Absence
from aleksis.apps.kolego.schema.absence import AbsenceType
from aleksis.core.schema.base import (
    BaseBatchPatchMutation,
    DjangoFilterMixin,
    OptimisticResponseTypeMixin,
    PermissionsTypeMixin,
)


class ParticipationStatusType(
    OptimisticResponseTypeMixin,
    PermissionsTypeMixin,
    DjangoFilterMixin,
    DjangoObjectType,
):
    class Meta:
        model = ParticipationStatus
        fields = (
            "id",
            "person",
            "absence_reason",
            "related_documentation",
            "base_absence",
            "tardiness",
        )

    notes_with_extra_mark = graphene.List(PersonalNoteType)
    notes_with_note = graphene.List(PersonalNoteType)

    @staticmethod
    def resolve_notes_with_extra_mark(root: ParticipationStatus, info, **kwargs):
        return NewPersonalNote.objects.filter(
            person=root.person,
            documentation=root.related_documentation,
            extra_mark__isnull=False,
        )

    @staticmethod
    def resolve_notes_with_note(root: ParticipationStatus, info, **kwargs):
        return NewPersonalNote.objects.filter(
            person=root.person,
            documentation=root.related_documentation,
            note__isnull=False,
        ).exclude(note="")


class ParticipationStatusBatchPatchMutation(BaseBatchPatchMutation):
    class Meta:
        model = ParticipationStatus
        fields = (
            "id",
            "absence_reason",
            "tardiness",
        )  # Only the reason and tardiness can be updated after creation
        return_field_name = "participationStatuses"

    @classmethod
    def check_permissions(cls, root, info, input, *args, **kwargs):  # noqa: A002
        pass

    @classmethod
    def after_update_obj(cls, root, info, input, obj, full_input):  # noqa: A002
        if not info.context.user.has_perm(
            "alsijil.edit_participation_status_for_documentation_with_time_range_rule",
            obj.related_documentation,
        ):
            raise PermissionDenied()


class ExtendParticipationStatusToAbsenceBatchMutation(graphene.Mutation):
    class Arguments:
        input = graphene.List(graphene.ID, description=_("List of ParticipationStatus IDs"))

    participations = graphene.List(ParticipationStatusType)
    absences = graphene.List(AbsenceType)

    @classmethod
    def create_absence(cls, info, participation_id):
        participation = ParticipationStatus.objects.get(pk=participation_id)

        if participation.date_end:
            end_date = participation.date_end
        else:
            end_date = ParticipationStatus.value_end_datetime(participation).date()

        end_datetime = datetime.datetime.combine(
            end_date, datetime.time.max, participation.timezone
        )

        if participation.base_absence:
            # Update the base absence to increase length if needed
            absence = participation.base_absence

            if absence.date_end:
                if absence.date_end < end_date:
                    absence.date_end = end_date
                    absence.save()

                return participation, absence

            # Absence uses a datetime
            if absence.datetime_end.astimezone(absence.timezone) < end_datetime:
                # The end date ends after the previous absence end
                absence.datetime_end = end_datetime
                absence.save()

            return participation, absence

        else:
            # No base absence, simply create one
            data = dict(
                reason_id=participation.absence_reason.id,
                person=participation.person,
            )

            if participation.date_start:
                data["date_start"] = participation.date_start
                data["date_end"] = end_date
            else:
                data["datetime_start"] = ParticipationStatus.value_start_datetime(participation)
                data["datetime_end"] = end_datetime

            absence, __ = Absence.objects.get_or_create(**data)

            participation.base_absence = absence
            participation.save()

            return participation, absence

    @classmethod
    def mutate(cls, root, info, input):  # noqa
        with create_revision():
            set_user(info.context.user)
            set_comment(_("Extended absence reason from coursebook."))
            participations, absences = zip(
                *[cls.create_absence(info, participation_id) for participation_id in input]
            )

        return ExtendParticipationStatusToAbsenceBatchMutation(
            participations=participations, absences=absences
        )

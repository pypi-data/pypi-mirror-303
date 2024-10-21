import datetime
from typing import List

from django.core.exceptions import PermissionDenied
from django.db.models import Q

import graphene

from aleksis.apps.kolego.models import Absence
from aleksis.core.models import Person

from ..models import ParticipationStatus
from .participation_status import ParticipationStatusType


class AbsencesForPersonsCreateMutation(graphene.Mutation):
    class Arguments:
        persons = graphene.List(graphene.ID, required=True)
        start = graphene.DateTime(required=True)
        end = graphene.DateTime(required=True)
        comment = graphene.String(required=False)
        reason = graphene.ID(required=True)

    ok = graphene.Boolean()
    participation_statuses = graphene.List(ParticipationStatusType)

    @classmethod
    def mutate(
        cls,
        root,
        info,
        persons: List[str | int],
        start: datetime.datetime,
        end: datetime.datetime,
        comment: str,
        reason: str | int,
    ):
        participation_statuses = []

        persons = Person.objects.filter(pk__in=persons)

        for person in persons:
            if not info.context.user.has_perm("alsijil.register_absence_rule", person):
                raise PermissionDenied()

            # Check if there is an existing absence with overlapping datetime
            absences = Absence.objects.filter(
                Q(datetime_start__lte=start) | Q(date_start__lte=start.date()),
                Q(datetime_end__gte=end) | Q(date_end__gte=end.date()),
                reason_id=reason,
                person=person,
            )

            if len(absences) > 0:
                kolego_absence = absences.first()
            else:
                # Check for same times and create otherwise
                kolego_absence, __ = Absence.objects.get_or_create(
                    datetime_start=start,
                    datetime_end=end,
                    reason_id=reason,
                    person=person,
                    defaults={"comment": comment},
                )

            events = ParticipationStatus.get_single_events(
                start,
                end,
                None,
                {"person": person},
                with_reference_object=True,
            )

            for event in events:
                participation_status = event["REFERENCE_OBJECT"]
                participation_status.absence_reason_id = reason
                participation_status.base_absence = kolego_absence
                participation_status.save()
                participation_statuses.append(participation_status)

        return AbsencesForPersonsCreateMutation(
            ok=True, participation_statuses=participation_statuses
        )

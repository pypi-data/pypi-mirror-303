from typing import Any, Dict

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext as _
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView

from django_tables2 import SingleTableView
from reversion.views import RevisionMixin
from rules.contrib.views import PermissionRequiredMixin, permission_required

from aleksis.core.decorators import pwa_cache
from aleksis.core.mixins import (
    AdvancedCreateView,
    AdvancedDeleteView,
    AdvancedEditView,
    SuccessNextMixin,
)
from aleksis.core.models import Group, PDFFile
from aleksis.core.util import messages
from aleksis.core.util.celery_progress import render_progress_page
from aleksis.core.util.core_helpers import has_person, objectgetter_optional

from .forms import (
    AssignGroupRoleForm,
    GroupRoleAssignmentEditForm,
    GroupRoleForm,
)
from .models import GroupRole, GroupRoleAssignment
from .tables import (
    GroupRoleTable,
)
from .tasks import generate_full_register_printout


@permission_required(
    "alsijil.view_full_register_rule", fn=objectgetter_optional(Group, None, False)
)
def full_register_group(request: HttpRequest, id_: int) -> HttpResponse:
    group = get_object_or_404(Group, pk=id_)

    file_object = PDFFile.objects.create()
    if has_person(request):
        file_object.person = request.user.person
        file_object.save()

    redirect_url = f"/pdfs/{file_object.pk}"

    result = generate_full_register_printout.delay(group.pk, file_object.pk)

    back_url = request.GET.get("back", "")
    back_url_is_safe = url_has_allowed_host_and_scheme(
        url=back_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    )
    if not back_url_is_safe:
        back_url = reverse("my_groups")

    return render_progress_page(
        request,
        result,
        title=_("Generate full register printout for {}").format(group),
        progress_title=_("Generate full register printout …"),
        success_message=_("The printout has been generated successfully."),
        error_message=_("There was a problem while generating the printout."),
        redirect_on_success_url=redirect_url,
        back_url=back_url,
        button_title=_("Download PDF"),
        button_url=redirect_url,
        button_icon="picture_as_pdf",
    )


@method_decorator(pwa_cache, "dispatch")
class GroupRoleListView(PermissionRequiredMixin, SingleTableView):
    """Table of all group roles."""

    model = GroupRole
    table_class = GroupRoleTable
    permission_required = "alsijil.view_grouproles_rule"
    template_name = "alsijil/group_role/list.html"


@method_decorator(never_cache, name="dispatch")
class GroupRoleCreateView(PermissionRequiredMixin, AdvancedCreateView):
    """Create view for group roles."""

    model = GroupRole
    form_class = GroupRoleForm
    permission_required = "alsijil.add_grouprole_rule"
    template_name = "alsijil/group_role/create.html"
    success_url = reverse_lazy("group_roles")
    success_message = _("The group role has been created.")


@method_decorator(never_cache, name="dispatch")
class GroupRoleEditView(PermissionRequiredMixin, AdvancedEditView):
    """Edit view for group roles."""

    model = GroupRole
    form_class = GroupRoleForm
    permission_required = "alsijil.edit_grouprole_rule"
    template_name = "alsijil/group_role/edit.html"
    success_url = reverse_lazy("group_roles")
    success_message = _("The group role has been saved.")


@method_decorator(never_cache, "dispatch")
class GroupRoleDeleteView(PermissionRequiredMixin, RevisionMixin, AdvancedDeleteView):
    """Delete view for group roles."""

    model = GroupRole
    permission_required = "alsijil.delete_grouprole_rule"
    template_name = "core/pages/delete.html"
    success_url = reverse_lazy("group_roles")
    success_message = _("The group role has been deleted.")


@method_decorator(pwa_cache, "dispatch")
class AssignedGroupRolesView(PermissionRequiredMixin, DetailView):
    permission_required = "alsijil.view_assigned_grouproles_rule"
    model = Group
    template_name = "alsijil/group_role/assigned_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()

        today = timezone.now().date()
        context["today"] = today

        self.roles = GroupRole.objects.with_assignments(today, [self.object])
        context["roles"] = self.roles
        assignments = (
            GroupRoleAssignment.objects.filter(
                Q(groups=self.object) | Q(groups__child_groups=self.object)
            )
            .distinct()
            .order_by("-date_start")
        )
        context["assignments"] = assignments
        return context


@method_decorator(never_cache, name="dispatch")
class AssignGroupRoleView(PermissionRequiredMixin, SuccessNextMixin, AdvancedCreateView):
    model = GroupRoleAssignment
    form_class = AssignGroupRoleForm
    permission_required = "alsijil.assign_grouprole_for_group_rule"
    template_name = "alsijil/group_role/assign.html"
    success_message = _("The group role has been assigned.")

    def get_success_url(self) -> str:
        return reverse("assigned_group_roles", args=[self.group.pk])

    def get_permission_object(self):
        self.group = get_object_or_404(Group, pk=self.kwargs.get("pk"))
        try:
            self.role = GroupRole.objects.get(pk=self.kwargs.get("role_pk"))
        except GroupRole.DoesNotExist:
            self.role = None
        return self.group

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        kwargs["initial"] = {"role": self.role, "groups": [self.group]}
        return kwargs

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["role"] = self.role
        context["group"] = self.group
        return context


@method_decorator(never_cache, name="dispatch")
class AssignGroupRoleMultipleView(PermissionRequiredMixin, SuccessNextMixin, AdvancedCreateView):
    model = GroupRoleAssignment
    form_class = AssignGroupRoleForm
    permission_required = "alsijil.assign_grouprole_for_multiple_rule"
    template_name = "alsijil/group_role/assign.html"
    success_message = _("The group role has been assigned.")

    def get_success_url(self) -> str:
        return reverse("assign_group_role_multiple")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


@method_decorator(never_cache, name="dispatch")
class GroupRoleAssignmentEditView(PermissionRequiredMixin, SuccessNextMixin, AdvancedEditView):
    """Edit view for group role assignments."""

    model = GroupRoleAssignment
    form_class = GroupRoleAssignmentEditForm
    permission_required = "alsijil.edit_grouproleassignment_rule"
    template_name = "alsijil/group_role/edit_assignment.html"
    success_message = _("The group role assignment has been saved.")

    def get_success_url(self) -> str:
        pk = self.object.groups.first().pk
        return reverse("assigned_group_roles", args=[pk])


@method_decorator(never_cache, "dispatch")
class GroupRoleAssignmentStopView(PermissionRequiredMixin, SuccessNextMixin, DetailView):
    model = GroupRoleAssignment
    permission_required = "alsijil.stop_grouproleassignment_rule"

    def get_success_url(self) -> str:
        pk = self.object.groups.first().pk
        return reverse("assigned_group_roles", args=[pk])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.date_end:
            self.object.date_end = timezone.now().date()
            self.object.save()
            messages.success(request, _("The group role assignment has been stopped."))
        return redirect(self.get_success_url())


@method_decorator(never_cache, "dispatch")
class GroupRoleAssignmentDeleteView(
    PermissionRequiredMixin, RevisionMixin, SuccessNextMixin, AdvancedDeleteView
):
    """Delete view for group role assignments."""

    model = GroupRoleAssignment
    permission_required = "alsijil.delete_grouproleassignment_rule"
    template_name = "core/pages/delete.html"
    success_message = _("The group role assignment has been deleted.")

    def get_success_url(self) -> str:
        pk = self.object.groups.first().pk
        return reverse("assigned_group_roles", args=[pk])

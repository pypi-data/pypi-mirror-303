from django.utils.translation import gettext as _

from aleksis.core.models import Group, Person

# Dynamically add extra permissions to Group and Person models in core
# Note: requires migrate afterwards
Group.add_permission(
    "view_week_class_register_group",
    _("Can view week overview of group class register"),
)
Group.add_permission(
    "view_lesson_class_register_group",
    _("Can view lesson overview of group class register"),
)
Group.add_permission("view_personalnote_group", _("Can view all personal notes of a group"))
Group.add_permission("edit_personalnote_group", _("Can edit all personal notes of a group"))
Group.add_permission(
    "view_lessondocumentation_group", _("Can view all lesson documentation of a group")
)
Group.add_permission(
    "edit_lessondocumentation_group", _("Can edit all lesson documentation of a group")
)
Group.add_permission("view_full_register_group", _("Can view full register of a group"))
Group.add_permission(
    "register_absence_group", _("Can register an absence for all members of a group")
)
Group.add_permission("assign_grouprole", _("Can assign a group role for this group"))
Person.add_permission("register_absence_person", _("Can register an absence for a person"))

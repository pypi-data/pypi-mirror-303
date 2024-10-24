"""
Status-indicator
================

Status indicators are dynamic pieces of information that should be used to
convey the status of a person, an object or a process. They do not require any
user actions to be updated, and are usually part of a larger component.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from django.utils.translation import gettext as _
#-
from .base import Node

class StatusIndicator(Node):
    """Status indicator component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        status : Literal['offline', 'online', 'away', 'do-not-disturb', 'busy',
                'unknown', 'error', 'success', 'warning', 'in-progress',
                'information', 'discovery', 'planet'] = \
                datafield(default=None)
        size : Literal['sm', 'lg'] = datafield(default=None)
        nolabel : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['status']:
            values['html_class'].add(f'nj-status-indicator--{values["status"]}')
        match values['status']:
            case 'offline':
                values['txt_label'] = _("Offline")
            case 'online':
                values['txt_label'] = _("Online")
            case 'away':
                values['txt_label'] = _("Away")
            case 'do-not-disturb':
                values['txt_label'] = _("Do not disturb")
            case 'busy':
                values['txt_label'] = _("Busy")
            case 'unknown':
                values['txt_label'] = _("Unknown")
            case 'error':
                values['txt_label'] = _("Error")
            case 'success':
                values['txt_label'] = _("Success")
            case 'warning':
                values['txt_label'] = _("Warning")
            case 'in-progress':
                values['txt_label'] = _("In progress")
            case 'information':
                values['txt_label'] = _("Information")
            case 'discovery':
                values['txt_label'] = _("Discovery")
            case 'planet':
                values['txt_label'] = _("Planet")
            case _:
                values['txt_label'] = _("Online")

        if values['size']:
            values['html_class'].add(f'nj-status-indicator--{values["size"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['nolabel']:
            template = """
<{astag} aria-hidden="true" class="nj-status-indicator {html_class}" {html_props}>
  <div class="nj-status-indicator__svg"></div>
</{astag}>
"""
        else:
            template = """
<{astag} class="nj-status-indicator {html_class}" {html_props}>
  <div class="nj-status-indicator__svg"></div>
  <p class="nj-status-indicator__text">{txt_label}</p>
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'StatusIndicator': StatusIndicator,
}

"""
Spinner
=======

See: https://www.engie.design/fluid-design-system/components/spinner/

Spinner allows the user to know when the system is in progress and when he will
end. The spinner is used to indicate the current status of a loading screen or
a loading data.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from django.utils.translation import gettext as _
#-
from .base import COLORS, Node

class Spinner(Node):
    """Spinner component
    """
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('spinner_kwargs',)

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        label : str = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)
        size : Literal['xxs', 'xs', 'sm', 'md'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['label'] is None:
            values['label'] = _("Loading...")

        if values['color']:
            values['html_class'].add(f'nj-spinner--{values["color"]}')

        if values['size']:
            values['html_class'].add(f'nj-spinner--{values["size"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} aria-live="polite" aria-atomic="true" class="nj-spinner {html_class}"
    {html_props}>
  {tmpl_label}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''

        if values['astag'] == 'span':
            template = '<span class="nj-sr-only">{label}</span>'
        else:
            template = '<p class="nj-sr-only">{label}</p>'

        return template.format(**values)


components = {
    'Spinner': Spinner,
}

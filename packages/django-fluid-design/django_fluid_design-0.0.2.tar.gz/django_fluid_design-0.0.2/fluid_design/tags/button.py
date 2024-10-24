"""
Button
======

See: https://www.engie.design/fluid-design-system/components/button/

Buttons allow users to interact with the product and trigger actions. They can
be of different sizes, colors and status.
In terms of accessibility, be mindful of people using assistive technologies:
don’t use links instead of buttons to trigger actions.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from django.utils.translation import gettext as _
#-
from .base import COLORS, Node

class Button(Node):
    """Button component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='button')
        disabled : bool = datafield(default=False)
        emphasis : Literal['subtle', 'minimal'] = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)
        size : Literal['xs', 'sm', 'lg', 'xl'] = datafield(default=None)
        isloading : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        context['icon_kwargs'] = {
            'html_class': 'nj-btn__icon nj-btn__icon--before',
        }

        values['txt_loading'] = _("Loading...")

        if values['disabled']:
            values['html_props'].append(('disabled', ''))

        if values['emphasis']:
            values['html_class'].add(f'nj-btn--{values["emphasis"]}')

        if values['color']:
            values['html_class'].add(f'nj-btn--{values["color"]}')

        if values['size']:
            values['html_class'].add(f'nj-btn--{values["size"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['isloading']:
            template = """
<{astag} class="nj-btn nj-btn--is-loading {html_class}" {html_props}>
  <div class="nj-spinner " aria-live="polite" aria-atomic="true">
    <p class="nj-sr-only">{txt_loading}</p>
  </div>
</{astag}>
"""
        else:
            template = """
<{astag} class="nj-btn {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'Button': Button,
}

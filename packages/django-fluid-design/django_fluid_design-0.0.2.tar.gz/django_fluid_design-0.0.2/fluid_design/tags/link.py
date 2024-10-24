"""
Link
====

See: https://www.engie.design/fluid-design-system/components/link/

Links are key elements for navigation. They should only be used for this
purpose, and not to trigger specific actions. For the latter case, use a button
instead. Different colors from our design system can be used to highlight
different categories of links.
To improve accessibility, we recommend to always use underscoring so that links
can easily be spotted by users. 
""" # pylint:disable=line-too-long
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from django.utils.translation import gettext as _
#-
from .base import Node

class Link(Node):
    """Link component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        icon_before : bool = datafield(default=False)
        size : Literal['sm'] = datafield(default=None)
        color : Literal['bold', 'contextual', 'grayed', 'contrast', 'inverse'] = \
                datafield(default=None)
        external : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_open'] = _("open in new tab")

        if values['color'] == 'contrast':
            values['color'] = 'high-contrast'
        if values['color']:
            values['html_class'].add(f'nj-link--{values["color"]}')

        if values['size']:
            values['html_class'].add(f'nj-link--{values["size"]}')

        if 'icon' in self.slots:
            values['html_class'].add('nj-link-icon')

            if values['icon_before']:
                values['html_class'].add('nj-link-icon--before')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['external']:
            template = """
<a target="_blank" class="nj-link nj-link-icon {html_class}" {html_props}>
  {child}
  <span class="nj-sr-only">&nbsp;({txt_open})</span>
  <span aria-hidden="true" class="material-icons">open_in_new</span>
</a>
"""
        elif 'icon' in self.slots:
            if values['icon_before']:
                template = """
<a class="nj-link {html_class}" {html_props}>
  {slot_icon}
  {child}
</a>
"""
            else:
                template = """
<a class="nj-link {html_class}" {html_props}>
  {child}
  {slot_icon}
</a>
"""
        else:
            template = """
<a class="nj-link {html_class}" {html_props}>
  {child}
</a>
"""
        return self.format(template, values, context)


components = {
    'Link': Link,
}

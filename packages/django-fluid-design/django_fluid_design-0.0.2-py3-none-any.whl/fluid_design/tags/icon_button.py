"""
Icon Button
===========

See: https://www.engie.design/fluid-design-system/components/icon-button/
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import COLORS, Node

class IconButton(Node):
    """IconButton component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='button')
        disabled : bool = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)
        size : Literal['2xs', 'xs', 'sm', 'lg', 'xl'] = datafield(default=None)
        material_icon : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['disabled']:
            values['html_props'].append(('disabled', ''))

        if values['color']:
            values['html_class'].add(f'nj-icon-btn--{values["color"]}')

        if values['size']:
            values['html_class'].add(f'nj-icon-btn--{values["size"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['label']:
            template = """
<{astag} class="nj-icon-btn {html_class}" {html_props}>
  <span class="nj-sr-only">{label}</span>
  {tmpl_icon}
</{astag}>
"""
        else:
            template = """
<{astag} class="nj-icon-btn {html_class}" {html_props}>
  {tmpl_icon}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon']:
            template = """
<span class="nj-icon-btn__icon nj-icon-material material-icons" aria-hidden="true">
  {material_icon}
</span>
"""
        else:
            return ''
        return self.format(template, values)


components = {
    'IconButton': IconButton,
}

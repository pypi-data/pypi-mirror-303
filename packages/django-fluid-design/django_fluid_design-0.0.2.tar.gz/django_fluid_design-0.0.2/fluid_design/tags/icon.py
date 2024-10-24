"""
Icon
====

Icons are symbols that represent objects and concepts visually. They help users
understand the message without text and should be as informative as possible.
They shouldn't be used to "decorate" the interface. They communicate messages in
the simplest way.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import COLORS, Node

class Icon(Node):
    """Icon component
    """
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('icon_kwargs',)

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='span')
        color : Literal[*COLORS] = datafield(default=None)
        size : Literal['sm', 'lg', 'xl', 'xxl'] = datafield(default=None)
        material : str = datafield(default=None)
        color_inherit : bool = datafield(default=False) # inherit color
        size_inherit : bool = datafield(default=False) # inherit color


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['size']:
            values['html_class'].add(f'nj-icon-material--{values["size"]}')

        if values['color']:
            values['html_class'].add(f'nj-icon-material--{values["color"]}')

        if values['color_inherit']:
            values['html_class'].add('nj-icon-material--color-inherit')

        if values['size_inherit']:
            values['html_class'].add('nj-icon-material--size-inherit')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['material']:
            template = """
<{astag} aria-hidden="true" class="material-icons nj-icon-material {html_class}"
    {html_props}>
  {material}
</{astag}>
{tmpl_label}
"""
        else:
            return ''

        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['label']:
            return ''

        template = '<span class="nj-sr-only">{label}</span>'
        return template.format(**values)


components = {
    'Icon': Icon,
}

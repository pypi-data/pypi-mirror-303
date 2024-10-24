"""
Badge
=====

See: https://www.engie.design/fluid-design-system/components/badge/

A badge should be used to bring a meaningful piece of information out. It may
either be textual or numerical. A badge may represent a status or a number of
unread notifications for example. Contrary to tags, badges cannot be
interactive. And multiple badges are not to be used side by side. A number of
variations are suggested here to help you use accessible badges.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import Node

class Badge(Node):
    """Badge component
    """
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('badge_kwargs',)

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='p')
        emphasis : Literal['subtle', 'minimal'] = datafield(default=None)
        color : Literal['danger', 'warning', 'success', 'information', \
            'discovery'] = datafield(default=None)
        size : Literal['sm', 'md', 'lg'] = datafield(default=None)
        uppercase : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['uppercase']:
            values['html_class'].add('nj-badge--uppercase')

        if values['size']:
            values['html_class'].add(f'nj-badge--{values["size"]}')

        if values['emphasis']:
            values['html_class'].add(f'nj-badge--{values["emphasis"]}')

        if values['color']:
            values['html_class'].add(f'nj-badge--{values["color"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-badge {html_class}" {html_props}>
  {label}
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'Badge': Badge,
}

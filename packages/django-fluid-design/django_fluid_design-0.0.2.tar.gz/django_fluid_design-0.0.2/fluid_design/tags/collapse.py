"""
Collapse
========

See: https://www.engie.design/fluid-design-system/components/collapse/

Collapses allow users to toggle the visibility of a content

How it works
------------

The collapse JavaScript plugin is used to show and hide content. Buttons or
anchors are used as triggers that are mapped to specific elements you toggle.
Collapsing an element will animate the height from its current value to 0.
Given how CSS handles animations, you cannot use padding on a .nj-collapse
element. Instead, use the class as an independent wrapping element.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import Node

class Collapse(Node):
    """Collapse component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['html_id']:
            values['html_props'].append(('id', values['html_id']))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-collapse {html_class}" {html_props}>
  <div class="nj-card nj-card__body">
    {child}
  </div>
</{astag}>
"""
        return self.format(template, values, context)


class CollapseButton(Node):
    """Collapse button component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        mode : Literal['default', 'anchor'] = datafield(default='default')
        target : str = datafield(default=None)
        controls : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['controls'] is None:
            if values['target'] and values['target'].startswith('#'):
                values['controls'] = values['target'][1:]


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<button class="nj-btn {html_class}" type="button" data-toggle="collapse"
    data-target="{target}" aria-expanded="false" aria-controls="{controls}"
    {html_props}>
  {child}
</button>
"""
        return self.format(template, values, context)


    def render_anchor(self, values, context):
        """Html output of the component
        """
        template = """
<a class="nj-btn {html_class}" role="button" data-toggle="collapse"
    href="{target}" aria-expanded="false" aria-controls="{controls}" {html_props}>
  {child}
</a>
"""
        return self.format(template, values, context)


components = {
    'CollapseBtn': CollapseButton,
    'Collapse': Collapse,
}

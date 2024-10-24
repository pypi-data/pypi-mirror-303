"""
Floating Action Button
======================

See: https://www.engie.design/fluid-design-system/components/fab/

Floating Action Buttons are just like buttons but they are not static. They
follow the journey of the user and display contextual actions at the perfect
moment. They are useful for mobile navigation. 
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Fab(Node):
    """Floating action button component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('menu',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        html_class_list : Set[str] = HtmlClassDescriptor()
        html_props_list : List[Tuple[str, str]] = HtmlPropsDescriptor()
        disabled : bool = datafield(default=False)
        placement : Literal['right'] = datafield(default=None)
        size : Literal['sm'] = datafield(default=None)
        material_icon : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['size']:
            values['html_class'].add(f'nj-fab--{values["size"]}')
            values['html_class_list'].add(f'nj-fab__actions--{values["size"]}')
        if values['placement']:
            values['html_props_wrapper'].append(('data-placement',
                    values['placement']))

        if values['disabled']:
            values['html_props'].append(('disabled', ''))


    def render_default(self, values, context):
        """Html output of the component
        """
        if 'menu' in self.slots:
            template = """
<div class="nj-fab-menu {html_class_wrapper}" {html_props_wrapper}>
  <button type="button" class="nj-fab {html_class}" {html_props}>
    {tmpl_icon}
    <span class="nj-sr-only">{child}</span>
  </button>
  <ul class="nj-fab__actions {html_class_list}" {html_props_list}>
    {slot_menu}
  </ul>
</div>
"""
        else:
            template = """
<button type="button" class="nj-fab {html_class}" {html_props}>
  {tmpl_icon}
  <span class="nj-sr-only">{child}</span>
</button>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon']:
            tmpl = """
<span aria-hidden="true" class="material-icons">{material_icon}</span>
"""
        else:
            return ''
        return self.format(tmpl, values)


class FabItem(Node):
    """Floating action menu component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        material_icon : str = datafield(default=None)


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li class="nj-fab__item">
  <button type="button" class="nj-fab nj-fab--light nj-fab--sm {html_class}"
      {html_props}>
    {tmpl_icon}
    <span class="nj-sr-only">{child}</span>
  </button>
</li>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon']:
            tmpl = """
<span aria-hidden="true" class="material-icons">{material_icon}</span>
"""
        else:
            return ''
        return self.format(tmpl, values)


components = {
    'Fab': Fab,
    'FabItem': FabItem,
}

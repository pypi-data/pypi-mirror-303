"""
Toggle
======

See: https://www.engie.design/fluid-design-system/components/toggle/

Use toggles when your users can turn something on or off instantly. For example,
if they need to enable or disabled the notifications. This component have been
in user interfaces for a long time so it should be used as expected. Keep in
mind that toggle should only be used when the user needs to decide between two
opposing states.

The toggle is an important element of the interface because the user often has
an interaction with it. This is why it must be visible at a glance if a switch
has been selected.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import FormNode
from .base_widgets import CustomCheckboxInput

class Toggle(FormNode):
    """Toggle component
    """
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('toggle_kwargs',)

    widget_class = CustomCheckboxInput

    @dataclass
    class Options(FormNode.Options):
        """Named arguments for the component
        """
        size : Literal['lg'] = datafield(default=None)
        material_icon : str = datafield(default=None)
        darkmode : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['size']:
            values['html_class_wrapper'].add(f'nj-toggle--{values["size"]}')

        if values['disabled']:
            values['html_class_wrapper'].add('nj-toggle--disabled')

        if values['label'] and (values['darkmode'] or values['material_icon']):
            values['html_props_wrapper'].append(('title', values['label']))


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """
        props['role'] = 'switch'


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-toggle {html_class_wrapper}" {html_props_wrapper}>
  <label for="{html_id}">
    {tmpl_element}
    <span class="nj-toggle__track"></span>
    {tmpl_icon}
    {tmpl_label}
  </label>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''

        if values['material_icon'] or values['darkmode']:
            tmpl = '<span class="nj-sr-only">{label}</span>'
        else:
            tmpl = '<span">{label}</span>'
        return self.format(tmpl, values)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if values['darkmode']:
            return """
<svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 16 16" class="nj-toggle__icon">
  <path d="M9.53 16h-.48a8 8 0 01-7.4-8.47A7.94 7.94 0 019.52 0h.94l-.64.6a7.71 7.71 0 00-2.06 8 7.6 7.6 0 006.3 5.23l.87.1-.7.52A7.77 7.77 0 019.53 16zM8.71.74a7.31 7.31 0 00.38 14.54 7.06 7.06 0 004-.94 8.35 8.35 0 01-6-5.55A8.48 8.48 0 018.71.74z"/>
</svg>
"""
        if values['material_icon']:
            tmpl = """
<span aria-hidden="true" class="nj-toggle__icon material-icons">
  {material_icon}
</span>
"""
            return self.format(tmpl, values)
        return ''


components = {
    'Toggle': Toggle,
}

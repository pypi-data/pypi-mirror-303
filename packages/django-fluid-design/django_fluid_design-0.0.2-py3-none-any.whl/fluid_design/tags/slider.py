"""
Slider
======

See: https://www.engie.design/fluid-design-system/components/slider/

A slider allows the user to slide a knob along a straight track to control or to
change a variable. Sliders can have icons on both ends of the bar, for example
when you want to change the brightness of your screen.
"""
from dataclasses import dataclass, field as datafield
#-
from .base import FormNode
from .base_widgets import CustomRangeInput

class Slider(FormNode):
    """Slider component
    """
    widget_class = CustomRangeInput

    @dataclass
    class Options(FormNode.Options):
        """Named arguments for the component
        """
        tooltip : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['disabled']:
            values['html_class_wrapper'].add('nj-slider--disabled')
        if values['tooltip']:
            values['html_props_wrapper'].append(('data-tooltip', 'true'))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-slider {html_class_wrapper}" {html_props_wrapper}>
  {tmpl_label}
  {tmpl_element}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''

        if values['required']:
            tmpl = """
<label for="{html_id}" class="{html_class_label}" {html_props_label}>
  {label}{label_suffix}
  <span class="nj-form-item__required-asterisk">*</span>
</label>
"""
        else:
            tmpl = """
<label for="{html_id}" class="{html_class_label}" {html_props_label}>
  {label}{label_suffix}
</label>
"""
        return self.format(tmpl, values)


components = {
    'Slider': Slider,
}

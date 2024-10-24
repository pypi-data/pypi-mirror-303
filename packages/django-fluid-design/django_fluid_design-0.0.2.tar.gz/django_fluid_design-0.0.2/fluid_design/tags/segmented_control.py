"""
Segmented control
=================

See: https://www.engie.design/fluid-design-system/components/segmented-control/

Segmented controls are helpful to show closely-related options users can choose
from. They can be used to switch views for example.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import clean_attr_value, Node

class SegmentedControl(Node):
    """Segmented control component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        mode : Literal['default', 'compact'] = datafield(default='default')
        value : str = datafield(default=None)
        size : Literal['sm', 'lg'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        context['segmented_control_button_kwargs'] = {}

        if values['mode'] == 'compact':
            context['segmented_control_button_kwargs']['compact'] = True

        if values['label']:
            values['html_props'].append(('aria-label', values['label']))

        if values['value']:
            values['html_props'].append(('data-value', values['value']))

            context['segmented_control_button_kwargs']['selected'] = values['value']

        if values['size']:
            values['html_class'].add(f'nj-segmented-control--{values["size"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-segmented-control {html_class}" role="group" {html_props}>
  {child}
</div>
"""
        return self.format(template, values, context)


    def render_compact(self, values, context):
        """Html output of the component
        """
        return self.render_default(values, context)


class SegmentedControlButton(Node):
    """Segmented control button component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."

    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('segmented_control_button_kwargs',)

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        value : str = datafield(default=None)
        selected : bool = datafield(default=False)
        compact : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        context['icon_icon_kwargs'] = {
            'html_class': 'nj-segmented-control-btn__icon',
        }


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        cleaned_child = clean_attr_value(values['child'])
        if not values['value']:
            values['value'] = cleaned_child
        if values['value'] == values['selected']:
            values['html_props'].append(('aria-pressed', 'true'))
        else:
            values['html_props'].append(('aria-pressed', 'false'))

        if values['compact']:
            values['html_props'].append(('title', cleaned_child))

        super().after_prepare(values, context)


    def render_default(self, values, context):
        """Html output of the component
        """
        if 'icon' in self.slots:
            if values['compact']:
                template = """
<button class="nj-segmented-control-btn {html_class}" type="button"
    data-value="{value}" {html_props}>
  {slot_icon}
  <span class="nj-sr-only">{child}</span>
</button>
"""
            else:
                template = """
<button class="nj-segmented-control-btn {html_class}" type="button"
    data-value="{value}" {html_props}>
  {slot_icon}
  <span>{child}</span>
</button>
"""
        else:
            template = """
<button class="nj-segmented-control-btn {html_class}" type="button"
    data-value="{value}" {html_props}>
  {child}
</button>
"""
        return self.format(template, values, context)


components = {
    'SegmentedControl': SegmentedControl,
    'SegmentedControlBtn': SegmentedControlButton,
}

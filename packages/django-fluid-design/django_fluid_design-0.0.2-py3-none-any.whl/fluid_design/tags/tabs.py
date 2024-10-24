"""
Tabs
====

See: https://www.engie.design/fluid-design-system/components/tabs/

Tabs organise content across different screens with a simple navigation.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from django.utils.translation import gettext as _
#-
from .base import Node

class Tabs(Node):
    """Tabs component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('buttons',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        variant : Literal['compact', 'spacious', 'stretched'] = \
                datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_buttons'] = _("Tab system label")

        if values['variant']:
            values['html_class'].add(f'nj-tab--{values["variant"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-tab {html_class}" {html_props}>
  <div class="nj-tab__items" role="tablist" aria-label="{txt_buttons}">
    {slot_buttons}
  </div>
  <div style="padding-top: var(--nj-semantic-size-spacing-16);">
    {child}
  </div>
</{astag}>
"""
        return self.format(template, values, context)


class TabsButton(Node):
    """Tabs button component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='button')
        active : bool = datafield(default=False)
        target : str = datafield(default=None)
        disabled : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['target']:
            values['html_props'].append(('aria-controls', values['target']))

        if values['active']:
            values['html_class'].add('nj-tab__item--active')
            values['html_props'].append(('aria-selected', 'true'))
            values['html_props'].append(('tabindex', '0'))
        else:
            values['html_props'].append(('aria-selected', 'false'))
            values['html_props'].append(('tabindex', '-1'))

        if values['disabled']:
            values['html_props'].append(('disabled', ''))

        if values['html_id']:
            values['html_props'].append(('id', values['html_id']))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-tab__item {html_class}" role="tab" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


class TabsPanel(Node):
    """Tabs panel component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        active : bool = datafield(default=False)
        trigger : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['trigger']:
            values['html_props'].append(('aria-labelledby', values['trigger']))

        if values['active']:
            values['html_class'].add('nj-tab__content--active')

        if values['html_id']:
            values['html_props'].append(('id', values['html_id']))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-tab__content {html_class}" role="tabpanel" tabindex="0"
    {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'Tab': Tabs,
    'T_Btn': TabsButton,
    'T_Panel': TabsPanel,
}

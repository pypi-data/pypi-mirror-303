"""
List
====

See: https://www.engie.design/fluid-design-system/components/list/

Lists are a flexible and powerful component for displaying a series of content.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import Node

class List(Node):
    """List component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='ul')
        size : Literal['sm', 'lg'] = datafield(default=None)
        border : bool = datafield(default=False)
        clickable : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['border']:
            values['html_class'].add('nj-list--has-border')

        if values['clickable']:
            context['listitem_kwargs'] = {
                'isoption': True,
            }

            values['html_props'].append(('role', 'listbox'))

        if values['size']:
            values['html_class'].add(f'nj-list--{values["size"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-list {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


class ListItem(Node):
    """List component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('prefix', 'suffix')
    "Named children."
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('listitem_kwargs',)

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='span')
        active : bool = datafield(default=False)
        border : bool = datafield(default=False)
        clickable : bool | Literal['a', 'button'] = datafield(default=None)
        disabled : bool = datafield(default=False)
        interactive : bool = datafield(default=False)
        navigation : bool = datafield(default=False)
        isoption : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        context['icon_kwargs'] = {
            'html_class': 'nj-list-item__icon',
        }
        context['suffix_badge_kwargs'] = {
            'html_class': 'nj-list-item__trailing',
        }
        context['suffix_icon_kwargs'] = {
            'html_class': 'nj-list-item__trailing',
        }
        context['suffix_tag_kwargs'] = {
            'html_class': 'nj-list-item__trailing',
        }
        context['suffix_toggle_kwargs'] = {
            'html_class_wrapper': 'nj-list-item__trailing',
        }

        if values['clickable']:
            if isinstance(values['clickable'], str):
                if values['isoption']:
                    values['html_props_wrapper'].append(('role', 'option'))

                if values['navigation']:
                    values['html_class_wrapper'].add('nj-list-item')
                    values['html_class_wrapper'].add('nj-list-item--navigation')

                if values['clickable'] == 'button' and values['disabled']:
                    values['html_props'].append(('disabled', ''))

                if values['border']:
                    values['html_class_wrapper'].add('nj-list__item--right-border')
            else:
                if values['isoption']:
                    values['html_props'].append(('role', 'option'))

                if values['interactive']:
                    values['html_class'].add('nj-list__item--interactive')
                    values['html_props'].append(('tabindex', '0'))

                if values['navigation']:
                    values['html_class'].add('nj-list-item')
                    values['html_class'].add('nj-list-item--navigation')

                if values['border']:
                    values['html_class'].add('nj-list__item--right-border')
        else:
            if values['border']:
                values['html_class'].add('nj-list__item--right-border')

        if values['active']:
            if values['clickable']:
                if isinstance(values['clickable'], str):
                    values['html_props_wrapper'].append(('aria-selected', 'true'))
                else:
                    values['html_props'].append(('aria-selected', 'true'))


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['clickable']:
            if isinstance(values['clickable'], str):
                template = """
<li class="nj-list__item {html_class_wrapper}" {html_props_wrapper}>
  <{clickable} class="nj-list__item-wrapper {html_class}" {html_props}>
    {slot_prefix}
    {tmpl_content}
    {slot_suffix}
  </{clickable}>
</li>
"""
            else:
                template = """
<li class="nj-list__item {html_class}" {html_props}>
  {slot_prefix}
  {tmpl_content}
  {slot_suffix}
</li>
"""
        else:
            template = """
<li class="nj-list__item {html_class}" {html_props}>
  {slot_prefix}
  {tmpl_content}
  {slot_suffix}
</li>
"""
        return self.format(template, values, context)


    def render_slot_suffix(self, values, context):
        """Render html of the slot.
        """
        if values['label']:
            tmpl = """
<span class="nj-list-item__secondary">{label}</span>
{child}
"""
            return tmpl.format(**values)

        return values['child']


    def render_tmpl_content(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['disabled'] and not isinstance(values['clickable'], str):
            tmpl = """
<button class="nj-list__item-wrapper" disabled>{child}</button>
"""
            return self.format(tmpl, values)

        if 'prefix' in self.slots or 'suffix' in self.slots:
            tmpl = """
<span class="nj-list-item__content">
  {child}
</span>
"""
            return self.format(tmpl, values)

        return values['child']


components = {
    'List': List,
    'Li': ListItem,
}

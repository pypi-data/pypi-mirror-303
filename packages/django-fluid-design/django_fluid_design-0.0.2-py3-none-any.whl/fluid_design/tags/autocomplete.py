"""
Autocomplete
============

See: https://www.engie.design/fluid-design-system/components/autocomplete/

Autocomplete provides automated assistance to fill in form field values. It
allows the user to have suggestions while typing in the field.
"""
from dataclasses import dataclass, field as datafield
import json
from typing import Dict, List, Set, Tuple
#-
#from django.utils.html import escape
from django.utils.translation import gettext as _
#-
from .base import FormNode, HtmlClassDescriptor, HtmlPropsDescriptor

class Autocomplete(FormNode):
    """Autocomplete component
    """
    @dataclass
    class Options(FormNode.Options):
        """Named arguments for the component
        """
        html_class_list : Set[str] = HtmlClassDescriptor()
        html_props_list : List[Tuple[str, str]] = HtmlPropsDescriptor()
        data : Dict = datafield(default=None)
        dataopt : Dict = datafield(default=None)
        instruction : str = datafield(default=None)
        list_label : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['instruction'] is None:
            values['instruction'] = _("Use the UP / DOWN arrows to navigate within "
                    "the suggestion list. Press Enter to select an option. On "
                    "touch devices, use swipe to navigate and double tap to select "
                    "an option")

        if values['data'] is not None:
            values['html_props_wrapper'].append(('data-list',
                    json.dumps(values['data'], separators=(',', ':'))))

        if values['dataopt']:
            values['html_props_wrapper'].append(('data-options',
                    json.dumps(values['dataopt'], separators=(',', ':'))))

        if values['list_label']:
            values['html_props_list'].append(('aria-label', values['list_label']))

        if values['label_position'] != 'floating':
            values['html_class_wrapper'].add('nj-form-item--static')


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """
        props['role'] = 'combobox'
        props['aria-autocomplete'] = 'list'
        props['aria-controls'].add(f'{props["id"]}-list')
        props['aria-expanded'] = 'false'
        props['autocomplete'] = 'off'
        if values['instruction']:
            props['aria-describedby'].add(
                    f'{props["id"]}-autocomplete-instructions')
        props['class'].add('nj-form-item__field')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
{tmpl_instruction}
<div class="nj-form-item nj-form-item--autocomplete {html_class_wrapper}"
    {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}

    <ul role="listbox" id="{html_id}-list" tabindex="-1" hidden
        class="nj-form-item__list nj-list-deprecated nj-list-deprecated--no-border nj-list-deprecated--sm {html_class_list}"
        {html_props_list}>
      <li aria-selected="false" role="option" tabindex="-1"
          class="nj-list-deprecated__item nj-list-deprecated__item--clickable"/>
    </ul>

    <span aria-hidden="true" class="nj-form-item__icon material-icons">
      keyboard_arrow_down
    </span>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_instruction(self, values, context):
        """Dynamically render a part of the template.
        """
        if not values['instruction']:
            return ''
        tmpl = """
<p id="{html_id}-autocomplete-instructions" hidden>{instruction}</p>
"""
        return self.format(tmpl, values)


components = {
    'Autocomplete': Autocomplete,
}

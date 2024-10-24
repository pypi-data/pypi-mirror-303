"""
Checkbox
========

See: https://www.engie.design/fluid-design-system/components/checkbox/

A checkbox is an input control that allows the user to give a feedback by
choosing several items from a list of options. For example, you can use
checkbox when user may have to select multiple options from a list of items, or
when an explicit action is required to apply the settings in your product.
""" # pylint:disable=line-too-long
from dataclasses import dataclass, field as datafield
import logging
from typing import List, Literal, Set, Tuple
#-
from .base import ChoiceSetNode, FormNode, HtmlClassDescriptor, HtmlPropsDescriptor

_logger = logging.getLogger(__name__)

class CheckboxSet(ChoiceSetNode):
    """Checkboxes inside fieldset component, multiselect choices
    """
    @dataclass
    class Options(ChoiceSetNode.Options):
        """Named arguments for the component.
        """
        html_class_item : Set[str] = HtmlClassDescriptor()
        html_props_item : List[Tuple[str, str]] = HtmlPropsDescriptor()
        exclude : str = datafield(default=None) # ; delimited list
        inline : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['inline']:
            values['html_class_item'].add('nj-checkbox--inline')


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<fieldset class="nj-checkbox-group {html_class}" {html_props}>
  <legend class="nj-checkbox-group__legend">
    {label}
    {tmpl_errors}
  </legend>
  {tmpl_items}
</fieldset>
"""
        else:
            template = """
<fieldset class="nj-checkbox-group {html_class}" {html_props}>
  <legend class="nj-checkbox-group__legend">{label}</legend>
  {tmpl_items}
</fieldset>
"""
        return self.format(template, values, context)


    def render_tmpl_items(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<div class="nj-checkbox {class}">
  <label for="{id}">
    <input type="checkbox" name="{name}" id="{id}" value="{value}" {props}>
    {child}
  </label>
</div>
"""
        excludes = values['exclude']
        if isinstance(excludes, str):
            excludes = [x.strip() for x in excludes.split(';')]
        elif excludes is None:
            excludes = []

        items = []
        for ii, (_, val, txt) in enumerate(self.choices()):
            options = {
                'id': f'{values["html_id"]}-{ii + 1}',
                'value': val,
                'child': txt.strip(),
                'name': self.bound_field.name,
                'class': values['html_class_item'],
            }
            props = []
            if self.check_test(val):
                props.append('checked')
            if val in excludes:
                options['class'] += ' nj-checkbox--disabled'
                props.append('disabled')
            if self.bound_field.errors:
                props.append('aria-invalid="true"')
                props.append(f'aria-describedby="{values["html_id"]}-errors"')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<span id="{id}-errors" class="nj-checkbox__error">
  {child}
</span>
"""
        child = '\n'.join(self.bound_field.errors)
        return template.format(child=child, id=values['html_id'])


class Checkbox(FormNode):
    """Checkbox component
    """
    @dataclass
    class Options(FormNode.Options):
        """Named arguments for the component.
        """
        size : Literal['lg', 'xl'] = datafield(default=None)
        success_text : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['label']:
            if values['disabled']:
                values['html_class'].add('nj-checkbox--disabled')

            if values['size']:
                values['html_class'].add(f'nj-checkbox--{values["size"]}')

            if self.bound_field.errors:
                values['html_class'].add('nj-checkbox--error')

        if values['success_text']:
            values['html_class'].add('nj-checkbox--success')


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """
        if not values['label']:
            if not self.bound_field.errors:
                props['class'].add('nj-checkbox')

            if values['size']:
                props['class'].add(f'nj-checkbox--{values["size"]}')

        if values['required']:
            props['required'] = True

        if values['success_text']:
            props['aria-describedby'].add(f'{values["html_id"]}-hint')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['label']:
            template = """
<div class="nj-checkbox {html_class}" {html_props}>
  <label for="{html_id}" class="{html_class_label}" {html_props_label}>
    {tmpl_element}
    <span class="nj-checkbox__label">{label}{tmpl_required}</span>
  </label>
  {tmpl_errors}
  {tmpl_help}
</div>
"""
        elif self.bound_field.errors:
            template = """
<div class="nj-checkbox {html_class}" {html_props}>
  {tmpl_element}
  {tmpl_errors}
  {tmpl_help}
</div>
"""
        else:
            template = """
{tmpl_element}
{tmpl_help}
"""

        return self.format(template, values, context)


    def render_tmpl_required(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['required']:
            return ''

        return '<span aria-hidden="true" class="nj-checkbox__required">*</span>'


    def render_tmpl_help(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['success_text']:
            tmpl = """
<div id="{html_id}-hint" class="nj-checkbox__subscript {html_class_help}"
    {html_props_help}>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--color-inherit nj-icon-material--sm">
    check
  </span>
  {success_text}
</div>
"""
        elif values['help_text']:
            tmpl = """
<div id="{html_id}-hint" class="nj-checkbox__subscript {html_class_help}"
    {html_props_help}>
  {help_text}
</div>
"""
        else:
            return ''
        return tmpl.format(**values)


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not self.bound_field.errors:
            return ''

        if values["label"]:
            tmpl = """
<div id="{id}-error" class="nj-checkbox__subscript">
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--color-inherit nj-icon-material--sm">
    warning
  </span>
  {child}
</div>
"""
        else:
            tmpl = """
<p id="{id}-error" class="nj-checkbox__error">
  <span aria-hidden="true" class="nj-checkbox__error-icon material-icons nj-icon-material nj-icon-material--color-inherit nj-icon-material--sm">
    warning
  </span>
  {child}
</p>
"""
        message = '. '.join(self.bound_field.errors).replace('..', '.')
        return tmpl.format(id=values['html_id'], child=message)


components = {
    'Checkbox': Checkbox,
    'CheckboxSet': CheckboxSet,
}

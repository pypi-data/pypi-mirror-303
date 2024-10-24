"""
Radio Button
============

See: https://www.engie.design/fluid-design-system/components/radio-button/ 

A radio button is an input control that allows the user to give a feedback by
choosing a single item from a list of options. For example, you can use radio
button when a user may have to select a single option from a list of items or
when an explicit action is required to apply the settings in your product.
""" # pylint:disable=line-too-long
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from .base import ChoiceSetNode, HtmlClassDescriptor, HtmlPropsDescriptor

class RadioSet(ChoiceSetNode):
    """Radio Button component
    """
    @dataclass
    class Options(ChoiceSetNode.Options):
        """Named arguments for the component
        """
        html_class_item : Set[str] = HtmlClassDescriptor()
        html_props_item : List[Tuple[str, str]] = HtmlPropsDescriptor()
        exclude : str = datafield(default=None)
        ignore : str = datafield(default=None)
        inline : str = datafield(default=False)
        size : Literal['lg', 'xl'] = datafield(default=False)
        noanime : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['inline']:
            values['html_class'].add('nj-radio-group--row')

        if values['disabled']:
            values['html_props'].append(('disabled', ''))

        if values['size']:
            values['html_class_item'].add(f'nj-radio--{values["size"]}')

        if values['required']:
            values['html_props_item'].append(('required', ''))

        if values['noanime']:
            values['html_class_item'].add('nj-radio--no-animation')


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<fieldset class="nj-radio-group nj-radio-group--has-error {html_class}"
    {html_props}>
  <legend class="nj-radio-group__legend">
    {label}
    {tmpl_required}
    {tmpl_errors}
  </legend>
  {tmpl_items}
</fieldset>
"""
        else:
            template = """
<fieldset class="nj-radio-group {html_class}" {html_props}>
  <legend class="nj-radio-group__legend">
    {label}
    {tmpl_required}
  </legend>
  {tmpl_items}
</fieldset>
"""
        return self.format(template, values, context)


    def render_tmpl_items(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<div class="nj-radio {class}">
  <label for="{id}">
    <input type="radio" name="{name}" id="{id}" value="{value}" {props}>
    {child}
  </label>
</div>
"""
        excludes = values['exclude'] or []
        if isinstance(excludes, str):
            excludes = [x.strip() for x in excludes.split(';')]

        ignores = values['ignore'] or []
        if isinstance(ignores, str):
            ignores = [x.strip() for x in ignores.split(';')]

        items = []
        for ii, (_, val, txt) in enumerate(self.choices()):
            if val in ignores:
                continue

            options = {
                'id': f'{values["html_id"]}-{ii + 1}',
                'value': val,
                'child': txt,
                'name': self.bound_field.name,
                'class': values['html_class_item'],
            }
            props = []
            if values['html_props_item']:
                props.append(values['html_props_item'])
            if self.check_test(val):
                props.append('checked')
            if val in excludes:
                props.append('disabled')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<p class="nj-radio-group__error-message">
  <span aria-hidden="true" class="nj-icon-material material-icons">
    warning
  </span>
  {child}
</p>
"""
        child = '\n'.join(self.bound_field.errors)
        return template.format(child=child, id=values['html_id'])


    def render_tmpl_required(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['required']:
            return ''

        return '<span aria-hidden="true" class="nj-radio-group__required">*</span>'


components = {
    'RadioSet': RadioSet,
}

"""
Form
====

See: https://www.engie.design/fluid-design-system/components/form/

Forms are used to send and collect data.
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from django.forms.widgets import (PasswordInput as PasswordWidget,
        Textarea as TextareaWidget)
from django.utils.translation import gettext as _
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, FormNode

class RenderIconTrait:
    """Render icon
    """
    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon']:
            template = """
<span class="nj-form-item__icon nj-icon-material material-icons" aria-hidden="true">
  {material_icon}
</span>
"""
        else:
            return ''
        return self.format(template, values) # pylint:disable=no-member


class RenderSuccessTrait:
    """Render success message
    """
    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context) # pylint:disable=no-member

        if values['success_text']:
            values['html_class_wrapper'].add('nj-form-item--success')


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """
        super().prepare_element_props(props, values, context) # pylint:disable=no-member

        if values['success_text']:
            props['aria-describedby'].add(f'{values["html_id"]}-hint')


    def render_tmpl_help(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['success_text']:
            tmpl = """
<p id="{html_id}-hint" class="nj-form-item__subscript {html_class_help}"
    {html_props_help}>
  <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">
    check
  </span>
  {success_text}
</p>
"""
        elif values['help_text']:
            tmpl = """
<p id="{html_id}-hint" class="nj-form-item__subscript {html_class_help}"
    {html_props_help}>
  {help_text}
</p>
"""
        else:
            return ''
        return tmpl.format(**values)


class TextInput(RenderIconTrait, RenderSuccessTrait, FormNode):
    """Form text item component
    """
    @dataclass
    class Options(FormNode.Options):
        """Named arguments for the component
        """
        size : Literal['sm', 'lg', 'xl'] = datafield(default=None)
        success_text : str = datafield(default=None)
        material_icon : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context)

        if values['size']:
            values['html_class_wrapper'].add(f'nj-form-item--{values["size"]}')

        if values['disabled']:
            values['html_class_wrapper'].add('nj-form-item--disabled')

        if values['label_position'] != 'floating':
            values['html_class_wrapper'].add('nj-form-item--static')


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """
        super().prepare_element_props(props, values, context)

        props['class'].add('nj-form-item__field')

        if values['required']:
            props['required'] = ''

        if values['label_position'] == 'floating':
            props['placeholder'] = ''


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--error {html_class_wrapper}"
    {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {tmpl_icon}
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item {html_class_wrapper}" {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {tmpl_icon}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


class PasswordInput(TextInput):
    """Form password item component
    """
    widget_class = PasswordWidget

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context)

        values['txt_hide'] = _("Hide password")
        values['txt_show'] = _("Show password")
        values['txt_hidden'] = _("Password is hidden")
        values['txt_visible'] = _("Password is visible")


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--error nj-form-item--password {html_class_wrapper}"
    {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    <button type="button" aria-pressed="false"
        class="nj-form-item__password-button nj-icon-btn nj-icon-btn--sm nj-icon-btn--tertiary">
      <span class="nj-sr-only" data-password-button-label-show="{txt_show}"
          data-password-button-label-hide="{txt_hide}"></span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        visibility
      </span>
    </button>
    <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite"
        aria-atomic="true" data-password-notice-is-visible="{txt_visible}"
        data-password-notice-is-hidden="{txt_hidden}"></p>
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item nj-form-item--password {html_class_wrapper}"
    {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    <button type="button" aria-pressed="false"
        class="nj-form-item__password-button nj-icon-btn nj-icon-btn--sm nj-icon-btn--tertiary">
      <span class="nj-sr-only" data-password-button-label-show="{txt_show}"
          data-password-button-label-hide="{txt_hide}"></span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        visibility
      </span>
    </button>
    <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite"
        aria-atomic="true" data-password-notice-is-visible="{txt_visible}"
        data-password-notice-is-hidden="{txt_hidden}"></p>
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


class Textarea(TextInput):
    """Form textarea item component
    """
    widget_class = TextareaWidget

    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--textarea nj-form-item--error {html_class_wrapper}"
    {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item nj-form-item--textarea {html_class_wrapper}"
    {html_props_wrapper}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


class NumberInput(RenderIconTrait, RenderSuccessTrait, FormNode):
    """Form number item component
    """
    @dataclass
    class Options(FormNode.Options):
        """Named arguments for the component
        """
        html_class_button : Set[str] = HtmlClassDescriptor()
        html_props_button : List[Tuple[str, str]] = HtmlPropsDescriptor()
        static : bool = datafield(default=False)
        size : Literal['sm', 'lg', 'xl'] = datafield(default=None)
        format : str = datafield(default=None)
        readonly : bool = datafield(default=False)
        success_text : str = datafield(default=None)
        material_icon : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        super().prepare(values, context)

        values['txt_decr'] = _("- Decrement")
        values['txt_incr'] = _("+ Increment")

        if values['static']:
            values['html_class_wrapper'].add('nj-form-item--static')

        if self.bound_field.errors:
            values['group_labelled_by'] = '{id} {id}-error'.format(
                    id=values['html_id'])
        elif self.bound_field.help_text:
            values['group_labelled_by'] = '{id} {id}-hint'.format(
                    id=values['html_id'])
        else:
            values['group_labelled_by'] = values['html_id']

        if values['disabled']:
            values['html_class_wrapper'].add('nj-form-item--disabled')
            values['html_props_button'].append(('disabled', ''))

        if values['readonly']:
            values['html_props_button'].append(('disabled', ''))

        if values['size']:
            values['html_class_wrapper'].add(f'nj-form-item--{values["size"]}')

        if values['format']:
            values['html_props_wrapper'].append(('data-live-zone-format',
                    values['format']))

        if values['label_position'] != 'floating':
            values['html_class_wrapper'].add('nj-form-item--static')


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """
        super().prepare_element_props(props, values, context)

        props['class'].add('nj-form-item__field')
        props['inputmode'] = 'numeric'

        if values['readonly']:
            props['readonly'] = ''


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--error nj-form-item--input-number {html_class_wrapper}"
    {html_props_wrapper}>
  <div aria-labelledby="{group_labelled_by}" class="nj-form-item__field-wrapper"
      role="group">
    {tmpl_decr}
    {tmpl_element}
    {tmpl_label}
    {tmpl_incr}
    <div aria-atomic="true" aria-live="polite" class="nj-sr-only"></div>
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item nj-form-item--input-number {html_class_wrapper}"
    {html_props_wrapper}>
  <div aria-labelledby="{group_labelled_by}" class="nj-form-item__field-wrapper"
      role="group">
    {tmpl_decr}
    {tmpl_element}
    {tmpl_label}
    {tmpl_incr}
    <div aria-atomic="true" aria-live="polite" class="nj-sr-only"></div>
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_decr(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<button type="button"
    class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button {html_class_button}"
    {html_props_button}>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
    remove
  </span>
  <span class="nj-sr-only">{txt_decr}</span>
</button>
"""
        return self.format(template, values)


    def render_tmpl_incr(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<button type="button"
    class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button {html_class_button}"
    {html_props_button}>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
    add
  </span>
  <span class="nj-sr-only">{txt_incr}</span>
</button>
"""
        return self.format(template, values)


components = {
    'NumberInput': NumberInput,
    'PasswordInput': PasswordInput,
    'TextInput': TextInput,
    'Textarea': Textarea,
}

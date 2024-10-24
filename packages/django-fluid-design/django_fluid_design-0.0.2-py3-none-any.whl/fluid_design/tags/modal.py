"""
Modal
=====

See: https://www.engie.design/fluid-design-system/components/modal/

Modal allows you to add dialogs to your site for lightboxes, user notifications,
or completely custom content.
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from django.utils.translation import gettext as _
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, Node
from .button import Button

class Modal(Node):
    """Modal component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('title', 'footer', 'icon', 'description')
    "Named children."

    default_slot_tags = {
        'title': 'h1',
        'description': 'p',
    }

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        mode : Literal['default', 'information', 'spinner'] = \
                datafield(default='default')
        html_class_dialog : Set[str] = HtmlClassDescriptor()
        html_props_dialog : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_footer : Set[str] = HtmlClassDescriptor()
        html_props_footer : List[Tuple[str, str]] = HtmlPropsDescriptor()
        appendto : str = datafield(default=None)
        size : Literal['sm'] = datafield(default=None)
        vcenter : bool = datafield(default=False)
        fcenter : bool = datafield(default=False)
        fade : bool = datafield(default=False)
        close_text : str = datafield(default=None)
        close_btn : bool = datafield(default=True)
        fit_viewport : bool = datafield(default=False)
        role : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_loading'] = _("Loading...")
        if values['role']:
            values['html_props'].append(('role', values['role']))
        else:
            values['html_props'].append(('role', 'alertDialog'))

        context['icon_spinner_kwargs'] = {
            'html_class': 'nj-modal__loading-spinner',
        }

        if values['close_text'] is None:
            values['close_text'] = _("Close the modal")

        if values['appendto']:
            values['html_props'].append(('data-appendTo', values['appendto']))

        if values['vcenter']:
            values['html_class'].add('nj-modal--vertical-centered')

        match values['mode']:
            case 'information':
                values['html_class'].add('nj-modal--information')

                context['icon_icon_kwargs'] = {
                    'html_class': 'nj-modal__icon',
                    'size': 'xxl',
                }
            case 'spinner':
                values['html_class'].add('nj-modal--information')

        if values['size']:
            values['html_class_dialog'].add(f'nj-modal--{values["size"]}')

        if values['fcenter'] and 'footer' in self.slots:
            self.slots['footer'].rawopts.html_class.add(
                    'nj-modal__footer--centered')

        if 'title' in self.slots:
            values['html_props'].append(('aria-labelledby',
                    f'{values["html_id"]}-title'))

        if values['fade']:
            values['html_class'].add('fade')

        if values['fit_viewport']:
            values['html_class'].add('nj-modal--fit-viewport')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['close_btn']:
            template = """
<div class="nj-modal {html_class}" id="{html_id}" {html_props}>
  <div class="nj-modal__dialog {html_class_dialog}" role="document"
      {html_props_dialog}>
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        {slot_title}

        {% IconButton type="button" html_class="nj-modal__close" color="secondary" size="sm" data-dismiss="modal" material_icon="close" label=close_text %}
      </div>
      <div class="nj-modal__body">
        {slot_description}
        {child}
      </div>
      {slot_footer}
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="nj-modal {html_class}" id="{html_id}" {html_props}>
  <div class="nj-modal__dialog {html_class_dialog}" role="document"
      {html_props_dialog}>
    <div class="nj-modal__content">
      <div class="nj-modal__body">
        {slot_title}
        {slot_description}
        {child}
      </div>
      {slot_footer}
    </div>
  </div>
</div>
"""
        return self.format(template, values, context, is_template=True)


    def render_information(self, values, context):
        """Html output of the component
        """
        if values['close_btn']:
            template = """
<div class="nj-modal {html_class}" id="{html_id}" {html_props}>
  <div class="nj-modal__dialog {html_class_dialog}" role="document"
      {html_props_dialog}>
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        {% IconButton type="button" html_class="nj-modal__close" color="secondary" size="sm" data-dismiss="modal" material_icon="close" label=close_text %}
      </div>
      <div class="nj-modal__body">
        {slot_icon}
        {slot_title}
        {slot_description}
        {child}
      </div>
      {slot_footer}
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="nj-modal {html_class}" id="{html_id}" {html_props}>
  <div class="nj-modal__dialog {html_class_dialog}" role="document"
      {html_props_dialog}>
    <div class="nj-modal__content">
      <div class="nj-modal__body">
        {slot_icon}
        {slot_title}
        {slot_description}
        {child}
      </div>
      {slot_footer}
    </div>
  </div>
</div>
"""
        return self.format(template, values, context, is_template=True)


    def render_spinner(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-modal {html_class}" id="{html_id}" {html_props}>
  <div class="nj-modal__dialog {html_class_dialog}" role="document"
      {html_props_dialog}>
    <div class="nj-modal__content">
      <div class="nj-modal__body">
        <div class="nj-spinner nj-modal__loading-spinner nj-spinner--md"
            role="status">
          <span class="nj-sr-only">{txt_loading}</span>
        </div>
        {slot_title}
        {slot_description}
        {child}
      </div>
      {slot_footer}
    </div>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_slot_title(self, values, context):
        """Render html of the slot.
        """
        if values['mode'] == 'default':
            template = """
<{astag} id="{node_id}-title" class="nj-modal__title {html_class}" {html_props}>
  {slot_icon}
  {child}
</{astag}>
"""
        else:
            template = """
<{astag} id="{node_id}-title" class="nj-modal__title {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


    def render_slot_footer(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<div class="nj-modal__footer {html_class}" {html_props}>
  {child}
</div>
"""
        return tmpl.format(**values)


    def render_slot_description(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<{astag} class="nj-modal__description {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return tmpl.format(**values)


class ModalButton(Button):
    """Modal trigger button component
    """
    @dataclass
    class Options(Button.Options):
        """Named arguments for the component
        """
        modal : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context)

        values['html_props'].append(('data-toggle', 'modal'))
        values['html_props'].append(('data-target', values['modal']))


class ModalButtonDismiss(Button):
    """Modal close button component
    """
    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context)

        values['html_props'].append(('data-dismiss', 'modal'))


components = {
    'Modal': Modal,
    'ModalBtn': ModalButton,
    'ModalCloseBtn': ModalButtonDismiss,
}

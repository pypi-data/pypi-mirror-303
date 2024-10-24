"""
Toast
=====

See: https://www.engie.design/fluid-design-system/components/toast/

Toasts are non-modal dialogs used as a way to provide feedback following user
action. They are typically composed of a short message appearing at the bottom
of the screen, to make them as discreet as possible.
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from django.utils.translation import gettext as _
#-
from .base import COLORS, HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Toast(Node):
    """Toast component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_button : Set[str] = HtmlClassDescriptor()
        html_props_button : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_gauge : Set[str] = HtmlClassDescriptor()
        html_props_gauge : List[Tuple[str, str]] = HtmlPropsDescriptor()
        target : str = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)
        btncolor : Literal[*COLORS] = datafield(default=None)
        gauge : int = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        context['icon_icon_kwargs'] = {
            'html_class': 'nj-toast__icon',
        }

        values['txt_close'] = _("Close notification")
        values['txt_gauge'] = _("The toast will be automatically closed in "
                "%(gauge)ss")

        if values['color']:
            values['html_class'].add(f'nj-toast--{values["color"]}')

        if values['btncolor']:
            values['html_class_button'].add(f'nj-icon-btn--{values["btncolor"]}')

        if values['gauge']:
            values['txt_gauge'] = values['txt_gauge'] % {'gauge': values['gauge']}
            if values['gauge'] != 5:
                values['html_props_gauge'].append(
                        ('style', f'animation-duration: {values["gauge"]}s;'))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-toast {html_class}" {html_props}>
  <div class="nj-toast__body">
    {slot_icon}
    <div class="nj-toast__content">
      {child}
    </div>
  </div>
  {tmpl_closebtn}
  {tmpl_gauge}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_closebtn(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['target']:
            return ''

        template = """
<div class="nj-toast__action">
  <button type="button" class="nj-icon-btn nj-icon-btn--sm {html_class_button}"
      aria-describedby="{target}" {html_props_button}>
    <span class="nj-sr-only">{txt_close}</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons nj-icon-material">
      close
    </span>
  </button>
</div>
"""
        return self.format(template, values)


    def render_tmpl_gauge(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['gauge'] is None:
            return ''

        template = """
<div class="nj-toast__gauge">
  <div class="nj-toast__gauge-bar {html_class_gauge}" {html_props_gauge}>
    <p class="nj-sr-only">{txt_gauge}</p>
  </div>
</div>
"""
        return self.format(template, values)



class ToastText(Node):
    """Toast text component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='p')


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['html_id']:
            values['html_props'].append(('id', values['html_id']))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-toast__text {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


class ToastTitle(Node):
    """Toast title component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='p')


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['html_id']:
            values['html_props'].append(('id', values['html_id']))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-toast__title {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


class ToastContainer(Node):
    """Toast component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        fullwidth  : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['label']:
            values['html_props'].append(('aria-label', values['label']))

        if values['fullwidth']:
            values['html_class'].add('nj-toast__container--full-width')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-toast__container {html_class}" role="region" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'Toast': Toast,
    'ToastText': ToastText,
    'ToastTitle': ToastTitle,
    'ToastContainer': ToastContainer,
}

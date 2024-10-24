"""
Inline Message
==============

See: https://www.engie.design/fluid-design-system/components/inline-message/
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from django.utils.translation import gettext as _
#-
from . base import HtmlClassDescriptor, HtmlPropsDescriptor, Node

class InlineMessage(Node):
    """Inline message component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('title',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_icon : Set[str] = HtmlClassDescriptor()
        html_props_icon : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_close : Set[str] = HtmlClassDescriptor()
        html_props_close : List[Tuple[str, str]] = HtmlPropsDescriptor()
        color : Literal['error', 'information', 'success', 'warning', 'fatal',
                'discovery', 'planet'] = datafield(default=None)
        icon : str = datafield(default=True)
        close : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_close'] = _("Hide message")

        if values['color'] == 'fatal':
            values['color'] = 'fatal-error'

        if values['color'] != 'error':
            values['html_class'].add(f'nj-inline-message--{values["color"]}')
        if values['color'] == 'fatal-error':
            values['html_class_close'].add('nj-icon-btn--inverse')
        if values['color']:
            values['html_class_icon'].add(f'nj-status-indicator--{values["color"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-inline-message {html_class}" {html_props}>
  {tmpl_icon}
  <div class="nj-inline-message__content">
   <h4 class="nj-inline-message__title">{slot_title}</h4>
   <p class="nj-inline-message__body">{child}</p>
  </div>
  {tmpl_close}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['icon']:
            return ''
        if values['color'] == 'fatal-error':
            return ''

        tmpl = """
<div class="nj-inline-message__status nj-status-indicator {html_class_icon}"
    aria-hidden="true" {html_props_icon}>
  <div class="nj-status-indicator__svg"></div>
</div>
"""
        return tmpl.format(**values)


    def render_tmpl_close(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['close']:
            return ''

        tmpl = """
<button class="nj-inline-message__close nj-icon-btn {html_class_close}"
    {html_props_close}>
  <span class="nj-sr-only">{txt_close}</span>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
</button>
"""
        return tmpl.format(**values)


components = {
    'Message': InlineMessage,
}

"""
Footer
======

See: https://www.engie.design/fluid-design-system/components/footer/

Footer is mainly used for links and legal information.
"""
from dataclasses import dataclass, field as datafield
from .base import Node

class Footer(Node):
    """Footer component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('banner', 'menu', 'social')
    "Named children."

    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<footer class="nj-footer {html_class}" role="contentinfo" {html_props}>
  <div class="container">
    {slot_banner}
    {slot_menu}
    {tmpl_child}
    {slot_social}
  </div>
</footer>
"""
        return self.format(template, values, context)


    def render_slot_banner(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<div class="nj-footer__baseline {html_class}" {html_props}>
  {child}
</div>
"""
        return tmpl.format(**values)


    def render_slot_menu(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<div class="nj-footer__menu {html_class}" {html_props}>
  {child}
</div>
"""
        return tmpl.format(**values)


    def render_slot_social(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<ul class="nj-footer__social {html_class}" {html_props}>
  {child}
</ul>
"""
        return tmpl.format(**values)


    def render_tmpl_child(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['child']:
            return ''

        template = """
<ul class="nj-footer__links">
  {child}
</ul>
"""
        return self.format(template, values)


class FooterLink(Node):
    """Footer link component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='a')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li>
  <{astag} class="nj-link nj-link--contextual {html_class}" {html_props}>
    {child}
  </{astag}>
</li>
"""
        return self.format(template, values, context)


class FooterSocial(Node):
    """Footer social link component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='a')


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['html_id']:
            values['html_props'].append(('id', values['html_id']))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li>
  <{astag} class="nj-footer__social-link {html_class}" {html_props}>
    {child}
  </{astag}>
</li>
"""
        return self.format(template, values, context)


class FooterSocialImage(Node):
    """Footer social img component
    """
    def render_default(self, values, context):
        """Html output of the component
        """
        template = '<img class="nj-footer__social-icon {html_class}" {html_props}>'
        return self.format(template, values)


class FooterMenuSection(Node):
    """Footer menu section component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-footer__menu-section {html_class}" {html_props}>
  {tmpl_label}
  <ul class="nj-footer__links-list">
    {child}
  </ul>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['label']:
            return ''
        template = '<h2 class="nj-footer__links-list-title">{label}</h2>'
        return self.format(template, values)


components = {
    'Footer': Footer,
    'FooterLink': FooterLink,
    'FooterSocial': FooterSocial,
    'FooterSocialImage': FooterSocialImage,
    'FooterMenu': FooterMenuSection,
}

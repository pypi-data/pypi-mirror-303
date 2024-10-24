"""
Tag
===

See: https://www.engie.design/fluid-design-system/components/tag/

Tags are used to show the criteria used to filter information. They can be
combined and used in every color of ENGIE’s palette.
Tags are used to visually label UI objects and elements for quick recognition.
For example, we can use them on cards, on tables, on form, etc. 
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from django.utils.translation import gettext as _
#-
from .base import COLORS, HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Tag(Node):
    """Tag component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('tag_kwargs',)

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_child : Set[str] = HtmlClassDescriptor()
        html_props_child : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_button : Set[str] = HtmlClassDescriptor()
        html_props_button : List[Tuple[str, str]] = HtmlPropsDescriptor()
        delete : bool = datafield(default=False)
        disabled : bool = datafield(default=False)
        size : Literal['xs', 'sm', 'lg'] = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)
        material_icon : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_remove'] = _("Remove tag")

        if values['size']:
            values['html_class'].add(f'nj-tag--{values["size"]}')

        if values['color']:
            values['html_class'].add(f'nj-tag--{values["color"]}')

        if values['disabled']:
            values['html_class'].add('nj-tag--disabled')
            values['child_tag'] = 'a'
            values['html_class_child'].add('nj-tag__text')
            values['html_props_child'].append(('role', 'link'))
            values['html_props_child'].append(('aria-disabled', 'true'))
        else:
            values['child_tag'] = 'p'
            values['html_class_child'].add('nj-tag__text')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-tag {html_class}" {html_props}>
  <{child_tag} class="{html_class_child}" {html_props_child}>{child}</{child_tag}>
  {tmpl_icon}
  {tmpl_delete}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon']:
            tmpl = """
<span class="nj-tag__icon nj-icon-material material-icons" aria-hidden="true">
  {material_icon}
</span>
"""
        else:
            return ''
        return tmpl.format(**values)


    def render_tmpl_delete(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['delete']:
            return ''

        template = """
<button type="button"
    class="nj-tag__close nj-icon-btn nj-icon-btn--2xs {html_class_button}"
    {html_props_button}>
  <span class="nj-sr-only">{txt_remove} {child}</span>
  <span aria-hidden="true"
      class="nj-icon-btn__icon nj-icon-material material-icons">
    close
  </span>
</button>
"""
        return template.format(**values)


components = {
    'Tag': Tag,
}

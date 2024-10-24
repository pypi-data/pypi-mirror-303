"""
Breadcrumb
==========

See: https://www.engie.design/fluid-design-system/components/breadcrumb/

Breadcrumbs should be used as soon as you structure information hierarchically.
Breadcrumbs provide users with their current location, help them find related
content and serve as secondary navigation.
""" # pylint:disable=line-too-long
from dataclasses import dataclass, field as datafield
from typing import List, Set, Tuple
#-
from django.utils.translation import gettext as _
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Breadcrumb(Node):
    """Breadcrumb component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='nav')


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_breadcrumb'] = _("breadcrumb")
        if values['astag'] != 'nav':
            values['html_props'].append(('role', 'navigation'))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} aria-label="{txt_breadcrumb}" {props}>
  <ol class="nj-breadcrumb">
    {child}
  </ol>
</{astag}>
"""
        return self.format(template, values)


class BreadcrumbItem(Node):
    """Breadcrumb item
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        html_class_link : Set[str] = HtmlClassDescriptor()
        html_props_link : List[Tuple[str, str]] = HtmlPropsDescriptor()
        href : str = datafield(default='#')
        current : bool = datafield(default=False)
        material_icon : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['current']:
            values['html_props'].append(('aria-current', 'page'))

        if values['material_icon']:
            values['html_class_link'].add('nj-link-icon')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li class="nj-breadcrumb__item {html_class}" {html_props}>{tmpl_item}</li>
"""
        return self.format(template, values, context)


    def render_tmpl_item(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['current']:
            return values['child']

        template = """
<a href="{href}" class="nj-link nj-link--sm nj-link--grayed {html_class_link}"
    {html_props_link}>
  {tmpl_icon}
  {tmpl_child}
</a>
"""
        return self.format(template, values, context)


    def render_tmpl_child(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon'] and values['child']:
            return f'<span class="nj-sr-only">{values["child"]}</span>'
        return values['child']


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['material_icon']:
            tmpl = """
<span aria-hidden="true" class="material-icons">{material_icon}</span>
"""
        else:
            return ''
        return self.format(tmpl, values)


class BreadcrumbMore(Node):
    """Breadcrumb has more items
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        label : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['label'] is None:
            values['label'] = _("Show hidden items")


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li class="nj-breadcrumb__see-more {html_class}" {html_props}>
  <button>
    <span class="nj-sr-only">{label}</span>
  </button>
</li>
"""
        return self.format(template, values, context)


components = {
    'Breadcrumb': Breadcrumb,
    'BreadcrumbItem': BreadcrumbItem,
    'BreadcrumbMore': BreadcrumbMore,
}

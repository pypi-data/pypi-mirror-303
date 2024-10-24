"""
Navbar
======

See: https://www.engie.design/fluid-design-system/components/navbar/

The navbar helps users know where they are on the product and quickly access
other pages and features at any moment. This version is useful for application
websites with few sections.

Please check also the Header component for more possibilities.
"""
from dataclasses import dataclass, field as datafield
import os
import re
from typing import List, Literal, Set, Tuple
#-
from django.utils.translation import gettext as _
#-
from .base import COLORS, HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Navbar(Node):
    """Navbar component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('after',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        mode : Literal['collapsible', 'simple', 'container'] = \
                datafield(default='collapsible')
        astag : str = datafield(default='nav')
        html_class_logo : Set[str] = HtmlClassDescriptor()
        html_props_logo : List[Tuple[str, str]] = HtmlPropsDescriptor()
        href : str = datafield(default='/')
        logo_src : str = datafield(default=None)
        logo_alt : str = datafield(default='home')
        logo_width : int = datafield(default=None)
        logo_height : int = datafield(default=None)
        expand : Literal['xl'] = datafield(default=None)
        transparent : bool = datafield(default=False)
        size : Literal['sm'] = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['size']:
            values['html_class'].add(f'nj-navbar--{values["size"]}')

        if values['color']:
            values['html_class'].add(f'nj-navbar--{values["color"]}')

        if values['transparent']:
            values['html_class'].add('nj-navbar--transparent')
        else:
            values['html_class'].add('nj-navbar--shadow')

        if values['expand']:
            if isinstance(values['expand'], str):
                values['html_class'].add(f'nj-navbar--expand-{values["expand"]}')
            else:
                values['html_class'].add('nj-navbar--expand')


    def render_collapsible(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-navbar {html_class}" {html_props}>
  {tmpl_logo}
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse"
      data-target="#{html_id}">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="{html_id}">
    <ul class="nj-navbar__nav">
      {child}
    </ul>
    {slot_after}
  </div>
</{astag}>
"""
        return self.format(template, values, context)


    def render_container(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-navbar {html_class}" {html_props}>
  <div class="container">
    {tmpl_logo}
    <button class="nj-navbar__toggler" type="button" data-toggle="collapse"
        data-target="#{html_id}">
      <span class="nj-navbar__toggler-icon material-icons">menu</span>
    </button>
    <div class="nj-navbar--collapse nj-collapse" id="{html_id}">
      <ul class="nj-navbar__nav">
        {child}
      </ul>
      {slot_after}
    </div>
  </div>
</{astag}>
"""
        return self.format(template, values, context)


    def render_simple(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-navbar {html_class}" {html_props}>
  {tmpl_logo}
  <ul class="nj-navbar__nav">
    {child}
  </ul>
  {slot_after}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_logo(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['logo_src']:
            return ''

        _, fileext = os.path.splitext(values['logo_src'])
        fileext = re.split('[#?]', fileext, 1)[0]
        if fileext == '.svg':
            tpl_image = """
<svg class="nj-navbar__logo" aria-label="{logo_alt}">
  <use href="{logo_src}" />
</svg>
"""
        else:
            tpl_image = """
<img class="nj-navbar__logo" src="{logo_src}" alt="{logo_alt}"
    width="{logo_width}" height="{logo_height}">
"""

        template = '<a class="nj-navbar__brand" href="{href}">{tpl_image}</a>'
        return template.format(**values, tpl_image=tpl_image)


class NavbarMenu(Node):
    """Navbar item component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        astag : str = datafield(default='a')
        active : bool = datafield(default=False)
        disabled : bool = datafield(default=False)
        icon : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['icon']:
            values['html_class'].add('nj-navbar__nav-link--icon')

        if values['active']:
            values['html_class'].add('active')

        if values['disabled']:
            values['html_class'].add('disabled')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li class="nj-navbar__nav-item">
  <{astag} class="nj-navbar__nav-link {html_class}" {html_props}>
    {child}
  </{astag}>
</li>
"""
        return self.format(template, values, context)


class NavbarSearch(Node):
    """Navbar search form component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_form : Set[str] = HtmlClassDescriptor()
        html_props_form : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_icon : Set[str] = HtmlClassDescriptor()
        html_props_icon : List[Tuple[str, str]] = HtmlPropsDescriptor()
        action : str = datafield(default=None)
        method : str = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_search'] = _("Search")
        values['txt_placeholder'] = _("Enter your query...")
        values['txt_close'] = _("Close")

        if values['action']:
            values['html_props_form'].append(('action', values['action']))
        if values['method']:
            values['html_props_form'].append(('method', values['method']))

        if values['color']:
            values['html_class_icon'].add(f'nj-icon-material--{values["color"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<form class="nj-navbar__search nj-collapse {html_class_form}" id="{html_id}"
    {html_props_form}>
  <input class="nj-form-control nj-navbar__search-input {html_class}" type="text"
      id="{html_id}-input" placeholder="{txt_placeholder}" {html_props}>
  <button type="submit" class="nj-btn nj-navbar__search-button">
    {txt_search}
  </button>
  <a href="#" aria-label="{txt_close}" data-dismiss="#{html_id}"
      class="nj-navbar__nav-link nj-navbar__nav-link--icon nj-collapse-inline__close">
    <span aria-hidden="true" class="material-icons nj-icon-material {html_class_icon}"
        {html_props_icon}>
      close
    </span>
  </a>
</form>
"""
        return self.format(template, values)


class NavbarSearchIcon(Node):
    """Navbar search button component for navbar search form
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_icon : Set[str] = HtmlClassDescriptor()
        html_props_icon : List[Tuple[str, str]] = HtmlPropsDescriptor()
        target : str = datafield(default=None)
        color : Literal[*COLORS] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['color']:
            values['html_class_icon'].add(f'nj-icon-material--{values["color"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li class="nj-navbar__nav-item">
  <a class="nj-navbar__nav-link nj-navbar__nav-link--icon {html_class}"
      data-toggle="collapse" href="#{target}" aria-expanded="false"
      aria-controls="{target}" {html_props}>
    <span aria-hidden="true" class="material-icons nj-icon-material {html_class_icon}"
        {html_props_icon}>
      search
    </span>
  </a>
</li>
"""
        return self.format(template, values)


components = {
    'Navbar': Navbar,
    'N_Menu': NavbarMenu,
    'N_MenuSearch': NavbarSearchIcon,
    'N_Search': NavbarSearch,
}

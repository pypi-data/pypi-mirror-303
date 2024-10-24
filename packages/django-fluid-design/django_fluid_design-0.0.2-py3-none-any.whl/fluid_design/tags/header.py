"""
Header
======

See: https://www.engie.design/fluid-design-system/components/header/

The header is a structuring element of ENGIE's identity. It is the main
navigation of a website. This version is primarily intended for the corporate
website with many sections.
Please check also the Navbar component for a more compact version.
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
from django.utils.translation import gettext as _
#-
from .base import COLORS, HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Header(Node):
    """Header component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('head_first', 'head_last', 'search')
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='header')
        fixed : bool = datafield(default=False)
        size : Literal['sm'] = datafield(default=None)
        scroll : Literal['sm'] = datafield(default=None)
        expand : Literal['lg'] = datafield(default=None)
        href : str = datafield(default='#')
        logo_alt : str = datafield(default='')
        logo_src : str = datafield(default=None)
        logo_width : int = datafield(default='')
        logo_height : int = datafield(default=48)
        logosm_src : str = datafield(default=None)
        logosm_width : int = datafield(default='')
        logosm_height : int = datafield(default=32)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['logosm_src'] is None:
            values['logosm_src'] = values['logo_src']

        if values['fixed']:
            values['html_class'].add('nj-header--fixed')

        if values['size']:
            values['html_class'].add(f'nj-header--{values["size"]}')

        if values['scroll']:
            values['html_class'].add(f'nj-header--scroll-{values["scroll"]}')

        if values['expand']:
            values['html_class'].add(f'nj-header--expand-{values["expand"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-header {html_class}" {html_props}>
  <div class="nj-header__group">
    {tmpl_head}
    <nav class="container">
      <div class="nj-header__nav-burger" aria-label="menu"
          aria-expanded="false">
        <button><div></div></button>
      </div>
      {tmpl_head_logosm}
      <ul class="nj-header__nav nj-header__nav--panel">
        {child}
      </ul>
      {slot_search}
    </nav>
  </div>
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_head(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not (values['logo_src'] or 'head_first' in self.slots or\
                'head_last' in self.slots):
            return ''

        tmpl = """
<div class="nj-header__head">
  {slot_head_first}
  {tmpl_head_logo}
  {slot_head_last}
</div>
"""
        return self.format(tmpl, values, context)


    def render_tmpl_head_logo(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['logo_src']:
            return ''

        tmpl = """
<a href="{href}" class="nj-header__logo">
  <img src="{logo_src}" alt="{logo_alt}" width="{logo_width}"
      height="{logo_height}">
</a>
"""
        return tmpl.format(**values)


    def render_tmpl_head_logosm(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['logosm_src']:
            return ''

        tmpl = """
<div class="nj-header__nav-logo--reduced">
  <a href="{href}">
    <img src="{logosm_src}" alt="{logo_alt}" width="{logosm_width}"
        height="{logosm_height}">
  </a>
</div>
"""
        return tmpl.format(**values)


class HeaderHeadLink(Node):
    """Header language link component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='a')
        active : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['active']:
            values['html_class'].add('nj-header__head-link--active')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-link nj-link--contextual nj-header__head-link {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values)


class HeaderMenu(Node):
    """Header nav item component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='a')
        active : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['active']:
            values['html_class'].add('active')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['child']:
            template = """
<li class="nj-header__nav-item {html_class_wrapper}" {html_props_wrapper}>
  <{astag} class="nj-header__nav-link {html_class}" {html_props}>
    {label}
    <span class="nj-header__menu-arrow-right material-icons nj-icon-material"
        aria-hidden="true">
      keyboard_arrow_right
    </span>
  </{astag}>
  <div class="nj-header__menu nj-header__nav--panel">
    {child}
  </div>
</li>
"""
        else:
            template = """
<li class="nj-header__nav-item {html_class_wrapper}" {html_props_wrapper}>
  <{astag} class="nj-header__nav-link {html_class}" {html_props}>
    {label}
  </{astag}>
</li>
"""
        return self.format(template, values, context)


class HeaderMenuTag(HeaderMenu):
    """Header nav item as Tag component
    """
    @dataclass
    class Options(HeaderMenu.Options):
        """Named arguments for the component.
        """
        html_class_tag : Set[str] = HtmlClassDescriptor()
        html_props_tag : List[Tuple[str, str]] = HtmlPropsDescriptor()
        color : Literal[*COLORS] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context)

        if values['color']:
            values['html_class_tag'].add(f'nj-tag--{values["color"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['child']:
            template = """
<li class="nj-header__nav-item {html_class_wrapper}" {html_props_wrapper}>
  <div class="nj-tag {html_class_tag}" {html_props_tag}>
    <{astag} class="nj-tag__link {html_class}" {html_props}>
      {label}
      <span class="nj-header__menu-arrow-right material-icons nj-icon-material"
          aria-hidden="true">
        keyboard_arrow_right
      </span>
    </{astag}>
  </div>
  <div class="nj-header__menu nj-header__nav--panel">
    {child}
  </div>
</li>
"""
        else:
            template = """
<li class="nj-header__nav-item {html_class_wrapper}" {html_props_wrapper}>
  <div class="nj-tag {html_class_tag}" {html_props_tag}>
    <{astag} class="nj-tag__link {html_class}" {html_props}>
      {label}
    </{astag}>
  </div>
</li>
"""
        return self.format(template, values)


class HeaderSubmenu(Node):
    """Header submenu navigation component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<ul class="nj-header__sub-nav">
  <li>
    <a href="#" class="nj-header__menu-title" aria-label="open"
        aria-expanded="false">
      {label}
      <span class="nj-header__menu-arrow-right material-icons" aria-hidden="true">
        keyboard_arrow_right
      </span>
    </a>
    <ul class="nj-header__nav--panel">
      <li>
        <a class="nj-header__menu-return">
          <span class="nj-header__menu-arrow-left material-icons"
              aria-hidden="true">
            keyboard_arrow_left
          </span>
          {label}
        </a>
      </li>
      {child}
    </ul>
  </li>
</ul>
"""
        return self.format(template, values)


class HeaderSubmenuReturn(Node):
    """Menu item to return to parent menu
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        astag : str = datafield(default='a')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-header__menu-return {html_class}" {html_props}>
  <span aria-hidden="true" class="nj-header__menu-arrow-left material-icons md-24">
    keyboard_arrow_left
  </span>
  {label}
</{astag}>
"""
        return self.format(template, values, context)


class HeaderMenuLink(Node):
    """Header nav item component
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
  <{astag} class="nj-header__menu-link nj-link nj-link--contextual {html_class}"
      {html_props}>
    {child}
  </{astag}>
</li>
"""
        return self.format(template, values)


class HeaderSearch(Node):
    """Header search component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        html_class_form : Set[str] = HtmlClassDescriptor()
        html_props_form : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_icon : Set[str] = HtmlClassDescriptor()
        html_props_icon : List[Tuple[str, str]] = HtmlPropsDescriptor()
        action : str = datafield(default=None)
        method : str = datafield(default=None)
        color : Literal[*COLORS] = datafield(default='brand')


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_open_search'] = _("Open the search field")
        values['txt_close_search'] = _("Close the search field")
        values['txt_search'] = _("Search")
        values['txt_placeholder'] = _("Enter your query...")

        if values['action']:
            values['html_props_form'].append(('action', values['action']))
        if values['method']:
            values['html_props_form'].append(('method', values['method']))

        if values['color']:
            values['html_class_icon'].add(f'nj-icon-btn--{values["color"]}')

        if values['html_id'] is None:
            values['html_id'] = self.default_id()


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-header__search-icon">
  <button type="button" data-toggle="collapse" data-target="#{html_id}"
      aria-expanded="false" aria-controls="{html_id}"
      class="nj-icon-btn nj-icon-btn--sm {html_class_icon}" {html_props_icon}>
    <span class="nj-sr-only">
      {txt_open_search}
    </span>
    <span class="nj-icon-btn__icon material-icons" aria-hidden="true">
      search
    </span>
  </button>
</div>
<form class="nj-header__search nj-collapse {html_class_form}" id="{html_id}"
    {html_props_form}>
  <input class="nj-form-control nj-header__search-input {html_class}" type="text"
      id="{html_id}-input" placeholder="{txt_placeholder}" {html_props}>
  <button type="submit" class="nj-btn">{txt_search}</button>
  <div class="nj-header__close">
    <button type="button" data-toggle="collapse" data-target="#{html_id}"
        aria-expanded="false" aria-controls="{html_id}"
        class="nj-icon-btn nj-icon-btn--sm {html_class_icon}" {html_props_icon}>
      <span class="nj-sr-only">
        {txt_close_search}
      </span>
      <span class="nj-icon-btn__icon material-icons" aria-hidden="true">
        close
      </span>
    </a>
  </div>
</form>
"""
        return self.format(template, values)


components = {
    'Header': Header,
    'H_HeadLink': HeaderHeadLink,
    'H_Menu': HeaderMenu,
    'H_MenuTag': HeaderMenuTag,
    'H_Link': HeaderMenuLink,
    'H_Submenu': HeaderSubmenu,
    'H_SubmenuReturn': HeaderSubmenuReturn,
    'H_Search': HeaderSearch,
}

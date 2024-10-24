"""
Sidebar
=======

See: https://www.engie.design/fluid-design-system/components/sidebar/

Sidebar can contain the entire content of the product and allows users a quick
access to a specific piece of content. The left arrow allows the user to retract
or expand the sidebar.
"""
from dataclasses import dataclass, field as datafield
#-
from .base import Node

class Sidebar(Node):
    """Sidebar component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('footer',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        href : str = datafield(default='#')
        logo_alt : str = datafield(default=None)
        logo_src : str = datafield(default=None)
        logo_width : int = datafield(default=100)
        logo_height : int = datafield(default=None)
        logosm_src : str = datafield(default=None)
        logosm_width : int = datafield(default=None)
        logosm_height : int = datafield(default=36)
        folded : bool = datafield(default=False)
        nomotion : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['logosm_src'] is None:
            values['logosm_src'] = values['logo_src']

        if values['folded']:
            values['html_class'].add('nj-sidebar--folded')

        if values['nomotion']:
            values['html_class'].add('nj-sidebar--no-motion')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-sidebar {html_class}" data-close-on-interact-out="true"
    id="{html_id}" {html_props}>
  {tmpl_logo}
  <nav class="nj-sidebar__navigation">
    <ul class="nj-list nj-list--sm">
      {child}
    </ul>
  </nav>
  {slot_footer}
  <ul class="nj-sidebar__collapse nj-list nj-list--sm">
    <li class="nj-list__item nj-list-item nj-list-item--navigation">
      <button data-toggle="sidebar" class="nj-list__item-wrapper"
          data-target="#{html_id}" aria-pressed="false">
        <span aria-hidden="true"
            class="material-icons nj-icon-material nj-list-item__icon nj-sidebar__fold-btn">
          chevron_left
        </span>
        <span class="nj-list-item__content">Close</span>
      </button>
    </li>
  </ul>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_logo(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['logo_src']:
            return ''

        link_props = []
        logo_props = []
        logosm_props = []

        if values['logo_alt']:
            link_props.append(('title', values['logo_alt']))
            logo_props.append(('alt', values['logo_alt']))
            logosm_props.append(('alt', values['logo_alt']))


        if values['href']:
            link_props.append(('href', values['href']))

        if values['logo_src']:
            logo_props.append(('src', values['logo_src']))
        if values['logo_width']:
            logo_props.append(('width', values['logo_width']))
        if values['logo_height']:
            logo_props.append(('height', values['logo_height']))
        if values['logosm_src']:
            logosm_props.append(('src', values['logosm_src']))
        if values['logosm_width']:
            logosm_props.append(('width', values['logosm_width']))
        if values['logosm_height']:
            logosm_props.append(('height', values['logosm_height']))

        link_props=self.join_attributes(self.prune_attributes(link_props))
        logo_props=self.join_attributes(self.prune_attributes(logo_props))
        logosm_props=self.join_attributes(self.prune_attributes(logosm_props))

        template = """
<a class="nj-sidebar__brand" {link_props}>
  <img class="nj-sidebar__logo" {logo_props}>
  <img class="nj-sidebar__logo--folded" {logosm_props}>
</a>
"""
        return template.format(link_props=link_props, logo_props=logo_props,
                logosm_props=logosm_props)


    def render_slot_footer(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<nav class="nj-sidebar__navigation nj-sidebar__navigation--footer {html_class}"
    {html_props}>
  <ul class="nj-list nj-list--sm">
    <div class="nj-sidebar__divider"></div>
    {child}
  </ul>
</nav>
"""
        return self.format(template, values)


class SidebarMenu(Node):
    """Sidebar menu component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        href : str = datafield(default='#')
        badge : int = datafield(default=None)
        arrow : bool = datafield(default=False)
        current : bool = datafield(default=False)

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        context['icon_kwargs'] = {
            'html_class': 'nj-list-item__icon',
        }

        if values['current']:
            values['html_props'].append(('aria-selected', 'true'))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<li class="nj-list__item nj-list-item nj-list-item--navigation {html_class}"
    {html_props}>
  <a href="{href}" class="nj-list__item-wrapper">
    {slot_icon}
    <span class="nj-list-item__content">{child}</span>
    {tmpl_after}
  </a>
</li>
"""
        return self.format(template, values, context)


    def render_tmpl_after(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['badge']:
            template = """
<p class="nj-badge nj-list-item__trailing">{badge}</p>
"""
        elif values['arrow']:
            template = """
<span aria-hidden="true"
    class="material-icons nj-icon-material nj-list-item__trailing">
  chevron_right
</span>
"""
        else:
            return ''

        return self.format(template, values)


class SidebarContent(Node):
    """Sidebar menu component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        nopush : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['nopush']:
            values['html_class'].add('nj-sidebar-content--nopush')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-sidebar-content {html_class}" {html_props}>
  {child}
</div>
"""
        return self.format(template, values, context)


components = {
    'Sidebar': Sidebar,
    'S_Menu': SidebarMenu,
    'S_Content': SidebarContent,
}

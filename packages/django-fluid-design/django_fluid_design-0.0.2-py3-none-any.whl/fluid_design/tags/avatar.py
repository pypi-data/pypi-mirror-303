"""
Avatar
======

See: https://www.engie.design/fluid-design-system/components/avatar/

Avatars are used to display a person's picture or initials. Avatars may help in
creating an emotional connection to the product and in validating that the
experience is indeed tailored for the current user.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from django.utils.translation import gettext as _
#-
from .base import Node

class Avatar(Node):
    """Avatar component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        mode : Literal['default', 'minimal'] = datafield(default='default')
        size : Literal['sm', 'lg', 'xl'] = datafield(default=None)
        initial : str = datafield(default=False)
        src : str = datafield(default=None)
        alt : str = datafield(default=None)
        clickable : bool = datafield(default=False)
        badge : int = datafield(default=0)
        badge_unit : str = datafield(default=None)
        status : Literal['offline', 'away', 'busy', 'online'] = \
                datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['badge_unit'] is None:
            values['badge_unit'] = _("notifications")

        if not values['src']:
            if values['initial']:
                values['html_class'].add('nj-avatar--initials')
            else:
                values['html_class'].add('nj-avatar--default-icon')

        if values['size']:
            values['html_class'].add(f'nj-avatar--{values["size"]}')

        if values['clickable']:
            values['html_class'].add('nj-avatar--clickable')
            if values['astag'] == 'div':
                values['astag'] = 'button'


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-avatar {html_class}" {html_props}>
  {tmpl_picture}
  {tmpl_initial}
  {tmpl_child}
  {tmpl_badge}
  {tmpl_status}
</{astag}>
"""
        return self.format(template, values, context)


    def render_minimal(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-avatar {html_class}" {html_props}>
  <div class="nj-avatar__picture">
    <img src="{src}" alt="{alt}">
  </div>
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_child(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['child']:
            return ''
        tmpl = '<p class="nj-sr-only">{child}</p>'
        return tmpl.format(**values)


    def render_tmpl_picture(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['src']:
            return ''
        tmpl = """
<img class="nj-avatar__picture" src="{src}" alt="{alt}">
"""
        return tmpl.format(**values)


    def render_tmpl_initial(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['initial']:
            return ''
        tmpl = """
<span class="nj-avatar__initials" aria-hidden="true">{initial}</span>
"""
        return tmpl.format(**values)


    def render_tmpl_badge(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['badge']:
            return ''
        if values['size'] == 'sm':
            return ''

        badge_class = []

        if values['size'] == 'xl':
            badge_class.append('nj-badge--lg')

        tmpl = """
<p class="nj-badge nj-badge--information {badge_class}">
  {badge} <span class="nj-sr-only">{badge_unit}</span>
</p>
"""
        return tmpl.format(badge_class=' '.join(badge_class), **values)


    def render_tmpl_status(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['status']:
            return ''

        status_class = []

        match values['status']:
            case 'offline':
                status_class.append('nj-status-indicator--offline')
                txt_status = _("Offline")
            case 'away':
                status_class.append('nj-status-indicator--away')
                txt_status = _("Away")
            case 'busy':
                status_class.append('nj-status-indicator--in-progress')
                txt_status = _("In progress")
            case _:
                status_class.append('nj-status-indicator--online')
                txt_status = _("Online")

        if values['size'] == 'xl':
            status_class.append('nj-status-indicator--lg')
        elif values['size'] != 'lg':
            status_class.append('nj-status-indicator--sm')

        tmpl = """
<div class="nj-status-indicator {status_class}">
  <div class="nj-status-indicator__svg"></div>
  <p class="nj-status-indicator__text nj-sr-only">{txt_status}</p>
</div>
"""
        return tmpl.format(status_class=' '.join(status_class),
                txt_status=txt_status, **values)


class AvatarMore(Node):
    """Avatar more items component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        size : Literal['sm', 'lg', 'xl'] = datafield(default=None)
        clickable : bool = datafield(default=False)
        count : int = datafield(default=0)
        alt : str = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['size']:
            values['html_class'].add(f'nj-avatar--{values["size"]}')

        if values['alt'] is None:
            values['alt'] = _("Show {count} more user profiles")\
                    .format(count=values['count'])

        if values['clickable']:
            values['html_class'].add('nj-avatar--clickable')
            if values['astag'] == 'div':
                values['astag'] = 'button'


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['clickable']:
            template = """
<{astag} class="nj-avatar nj-avatar--remaining-count {html_class}" {html_props}>
  {tmpl_count}
</{astag}>
"""
        else:
            template = """
<{astag} class="nj-avatar nj-avatar--remaining-count {html_class}" {html_props}>
  {tmpl_count}
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_count(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if values['alt']:
            tmpl = """
<span aria-hidden="true">+{count}</span>
<span class="nj-sr-only">{alt}</span>
"""
        else:
            tmpl = '+{count}'
        return self.format(tmpl, values)


class AvatarList(Node):
    """Avatar list component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component.
        """
        variant : Literal['compact'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['variant']:
            values['html_class'].add(f'nj-avatar-list--{values["variant"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-avatar-list {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'AvatarList': AvatarList,
    'Avatar': Avatar,
    'AvatarMore': AvatarMore,
}

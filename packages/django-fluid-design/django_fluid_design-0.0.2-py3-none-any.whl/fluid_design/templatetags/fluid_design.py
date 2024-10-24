"""Template tags provided by fluid_design module.

Provides:
 - svg for loading svg file
 - fluid_design_assets for loading css/js files
 - built-in template tags (you can make your own) for Fluid Design System
   components

"""
import logging
import os
import re
#-
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
#-
from ..tags import (
    autocomplete,
    avatar,
    badge,
    base,
    breadcrumb,
    button,
    card,
    checkbox,
    collapse,
    fab,
    footer,
    form_item,
    grid,
    header,
    icon,
    icon_button,
    inline_message,
    link,
    list_,
    modal,
    navbar,
    pagination,
    progress,
    radio_set,
    segmented_control,
    sidebar,
    skeleton,
    slider,
    spinner,
    stamp,
    status_indicator,
    table,
    tabs,
    tag,
    toast,
    toggle,
)

FLUID_DESIGN_TAGS = {
    **autocomplete.components,
    **avatar.components,
    **badge.components,
    **base.components,
    **breadcrumb.components,
    **button.components,
    **card.components,
    **checkbox.components,
    **collapse.components,
    **fab.components,
    **footer.components,
    **form_item.components,
    **grid.components,
    **header.components,
    **icon.components,
    **icon_button.components,
    **inline_message.components,
    **link.components,
    **list_.components,
    **modal.components,
    **navbar.components,
    **pagination.components,
    **progress.components,
    **radio_set.components,
    **segmented_control.components,
    **sidebar.components,
    **skeleton.components,
    **slider.components,
    **spinner.components,
    **stamp.components,
    **status_indicator.components,
    **table.components,
    **tabs.components,
    **tag.components,
    **toast.components,
    **toggle.components,
}

_logger = logging.getLogger(__name__)

register = template.Library()

class TagParser:
    """Parse arguments of Django template tags.
    """
    def __init__(self, tags):
        self.tags = tags

    def __call__(self, parser, token):
        params = token.split_contents()
        tagname = params.pop(0)

        args = []
        kwargs = {}
        for param in params:
            if '=' in param:
                key, val = param.split('=', 1)
            else:
                key, val = (None, param)

            if val[0] in ('"', "'"):
                val = val.strip('"\'')
            else:
                val = base.VariableInVariable(val, parser)

            if key:
                kwargs[key] = val
            else:
                args.append(val)

        cls = self.tags[tagname]

        if getattr(cls, 'WANT_CHILDREN', False):
            nodelist = parser.parse(('end' + tagname,))
            parser.delete_first_token()
            args.insert(0, nodelist)

        return cls(*args, parser=parser, **kwargs)


@register.simple_tag
def svg(path):
    """This template tag will load svg files located in settings.SVG_DIRS.
    """
    # Security test.
    if not path or not re.match(r'^\w.*\.svg$', path):
        return ''
    for dirname in settings.SVG_DIRS:
        if not os.path.exists(dirname/path):
            continue
        return mark_safe(open(dirname/path, 'r', encoding='utf-8').read())
    return ''


@register.simple_tag
def fluid_design_assets():
    """This template tag will inject Fluid Design System css/js files.

    Don't forget to run collectstatic!
    """
    if settings.DEBUG:
        suffix = ''
    else:
        suffix = '' # already minified
    tmpl = """
<link rel="stylesheet" type="text/css" href="{baseurl}fluid_design/fluid-design-system{suffix}.css">
<script src="{baseurl}fluid_design/fluid-design-system{suffix}.js"></script>
""" # pylint:disable=line-too-long
    return mark_safe(tmpl.format(baseurl=settings.STATIC_URL, suffix=suffix))


_parser = TagParser(FLUID_DESIGN_TAGS)
for name in FLUID_DESIGN_TAGS:
    register.tag(name, _parser)

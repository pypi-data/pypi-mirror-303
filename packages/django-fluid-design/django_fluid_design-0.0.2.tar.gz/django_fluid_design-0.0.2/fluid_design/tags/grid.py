"""
Grid
====

See: https://www.engie.design/fluid-design-system/components/grid/

All about the grid! Grid systems are used to create perfect layouts. Our grid
system is based on the Bootstrap v4 grid. Use the mobile-first flexbox grid to
build layouts of all shapes and sizes with a twelve column system, five default
responsive tiers, Sass variables and mixins, and dozens of predefined classes.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import Node

class Grid(Node):
    """Grid component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="container {html_class}" {html_props}>{child}</{astag}>
"""
        return self.format(template, values)


class GridRow(Node):
    """Grid row component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        gutter : bool = datafield(default=True)
        align_col : Literal['start', 'center', 'end', 'around', 'between'] = \
            datafield(default=None)
        align_sm : Literal['start', 'center', 'end', 'around', 'between'] = \
            datafield(default=None)
        align_md : Literal['start', 'center', 'end', 'around', 'between'] = \
            datafield(default=None)
        align_lg : Literal['start', 'center', 'end', 'around', 'between'] = \
            datafield(default=None)
        valign_col : Literal['start', 'center', 'end'] = datafield(default=None)
        valign_sm : Literal['start', 'center', 'end'] = datafield(default=None)
        valign_md : Literal['start', 'center', 'end'] = datafield(default=None)
        valign_lg : Literal['start', 'center', 'end'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        for size in ('col', 'sm', 'md', 'lg'):
            align = values[f'align_{size}']
            if align:
                if size == 'col':
                    prefix = 'justify-content'
                else:
                    prefix = f'justify-content-{size}'
                values['html_class'].add(f'{prefix}-{align}')

            valign = values[f'valign_{size}']
            if valign:
                if size == 'col':
                    prefix = 'align-items'
                else:
                    prefix = f'align-items-{size}'
                values['html_class'].add(f'{prefix}-{valign}')

        if not values['gutter']:
            values['html_class'].add('no-gutters')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="row {html_class}" {html_props}>{child}</{astag}>
"""
        return self.format(template, values)


class GridColumn(Node):
    """Grid column component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        order : int = datafield(default=None)
        col : int | Literal['fill', 'shrink'] = datafield(default=None)
        sm : int | Literal['fill', 'shrink'] = datafield(default=None)
        md : int | Literal['fill', 'shrink'] = datafield(default=None)
        lg : int | Literal['fill', 'shrink'] = datafield(default=None)
        xl : int | Literal['fill', 'shrink'] = datafield(default=None)
        offset_col : int = datafield(default=None)
        offset_sm : int = datafield(default=None)
        offset_md : int = datafield(default=None)
        offset_lg : int = datafield(default=None)
        offset_xl : int = datafield(default=None)
        ml_col : int | Literal['auto'] = datafield(default=None)
        ml_sm : int | Literal['auto'] = datafield(default=None)
        ml_md : int | Literal['auto'] = datafield(default=None)
        ml_lg : int | Literal['auto'] = datafield(default=None)
        ml_xl : int | Literal['auto'] = datafield(default=None)
        mr_col : int | Literal['auto'] = datafield(default=None)
        mr_sm : int | Literal['auto'] = datafield(default=None)
        mr_md : int | Literal['auto'] = datafield(default=None)
        mr_lg : int | Literal['auto'] = datafield(default=None)
        mr_xl : int | Literal['auto'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        has_size_class = False

        for size in ('col', 'sm', 'md', 'lg', 'xl'):
            width = values[size]

            if size == 'col':
                prefix = 'col'
            else:
                prefix = f'col-{size}'

            if width == 'fill':
                values['html_class'].add(prefix)
                has_size_class = True
            elif width == 'shrink':
                values['html_class'].add(f'{prefix}-auto')
                has_size_class = True
            elif width:
                values['html_class'].add(f'{prefix}-{width}')
                has_size_class = True

            offset = values[f'offset_{size}']
            if offset:
                if size == 'col':
                    prefix = 'offset'
                else:
                    prefix = f'offset-{size}'

                values['html_class'].add(f'{prefix}-{offset}')

            margin_left = values[f'ml_{size}']
            if margin_left:
                if size == 'col':
                    prefix = 'ml'
                else:
                    prefix = f'ml-{size}'

                values['html_class'].add(f'{prefix}-{margin_left}')

            margin_right = values[f'mr_{size}']
            if margin_right:
                if size == 'col':
                    prefix = 'mr'
                else:
                    prefix = f'mr-{size}'

                values['html_class'].add(f'{prefix}-{margin_right}')

        if not has_size_class:
            values['html_class'].add('col')

        order = values['order']
        if order:
            values['html_class'].add(f'order-{order}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = '<{astag} class="{html_class}" {html_props}>{child}</{astag}>'
        return self.format(template, values)


components = {
    'Grid': Grid,
    'Row': GridRow,
    'Col': GridColumn,
}

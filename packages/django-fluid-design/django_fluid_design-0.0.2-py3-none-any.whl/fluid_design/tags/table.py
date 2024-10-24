"""
Table
=====

See: https://www.engie.design/fluid-design-system/components/table/

Data table is used to display and organise all the data set. A data table is
used to compare and analyze data sets.The data informations are always
displayed in row and column.
"""
from dataclasses import dataclass, field as datafield
from typing import Literal
#-
from .base import Node

class Table(Node):
    """Table component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        variant : Literal['striped', 'hover'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['variant']:
            values['html_class'].add(f'nj-table--{values["variant"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<table class="nj-table {html_class}" {html_props}>
  {tmpl_label}
  {child}
</table>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['label']:
            return self.format('<caption>{label}</caption>', values)
        return ''


components = {
    'Table': Table,
}

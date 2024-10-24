"""
Stamp
=====

See: https://www.engie.design/fluid-design-system/components/stamp/

Stamp is a special brand identity component for Act with ENGIE operation
"""
from dataclasses import dataclass, field as datafield
from typing import List, Set, Tuple
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Stamp(Node):
    """Stamp component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_circle : Set[str] = HtmlClassDescriptor()
        html_props_circle : List[Tuple[str, str]] = HtmlPropsDescriptor()
        gradient : bool = datafield(default=False)
        shadow : bool = datafield(default=False)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['label_parts'] = values['label'].split(' ', 3)
        if values['gradient']:
            values['html_props_circle'].append(('fill',
                    f"url(#{values['html_id']}-gradient)"))
        else:
            values['html_props_circle'].append(('fill', '#fff'))

        if values['shadow']:
            values['html_class'].add('nj-stamp--shadow')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp {html_class}" {html_props}>
  <defs>
    {tmpl_gradient}
    <mask id="{html_id}-mask" x="0" y="0" width="100%" height="100%">
      <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
      <text class="nj-stamp__text" y="67" transform="translate(85)">
        {tmpl_label1}
        {tmpl_label2}
        {tmpl_label3}
      </text>
    </mask>
  </defs>
  <circle cx="85" cy="85" r="85" mask="url(#{html_id}-mask)" {html_props_circle}/>
</svg>
"""
        return self.format(template, values, context)


    def render_tmpl_gradient(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if values['gradient']:
            stops = []
            grads = [x for x in values['gradient'].split(' ') if x.strip()]
            for ii, grad in enumerate(grads):
                pos = int(ii / (len(grads) - 1) * 100)
                stops.append(f'<stop offset="{pos}%" stop-color="{grad}"/>')
            values['stops'] = '\n'.join(stops)
            template = """
<linearGradient id="{html_id}-gradient" x1="0" x2="1" y1="0" y2="1">
  {stops}
</linearGradient>
"""
            return self.format(template, values)
        return ''


    def render_tmpl_label1(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if len(values['label_parts']) > 0:
            label = values['label_parts'][0]
            return f'<tspan x="0" text-anchor="middle">{label}</tspan>'
        return ''


    def render_tmpl_label2(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if len(values['label_parts']) > 1:
            label = values['label_parts'][1]
            return f'<tspan x="0" text-anchor="middle" dy="28">{label}</tspan>'
        return ''


    def render_tmpl_label3(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if len(values['label_parts']) > 2:
            label = values['label_parts'][2]
            return f'<tspan x="0" text-anchor="middle" dy="28">{label}</tspan>'
        return ''


components = {
    'Stamp': Stamp,
}

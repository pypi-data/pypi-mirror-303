"""
Progress bar
============

See: https://www.engie.design/fluid-design-system/components/progress/

Progress bars allow users to know their task was successfully launched and the
system progresses towards task completion. They are a representation of a
progress status that evolves over time. As a general rule of thumb, use progress
bars when task completion takes longer than 1 second.
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, Node

class ProgressBar(Node):
    """Progress bar component
    """
    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_indicator : Set[str] = HtmlClassDescriptor()
        html_props_indicator : List[Tuple[str, str]] = HtmlPropsDescriptor()
        current : int = datafield(default=0)
        min : int = datafield(default=0)
        max : int = datafield(default=100)
        text_position : bool | Literal['right'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if values['label']:
            values['html_props'].append(('aria-label', values['label']))

        values['current'] = max(values['current'], 0)
        values['min'] = max(values['min'], 0)
        values['max'] = max(values['max'], 0)

        percent = values['current'] * 100 / (values['max'] - values['min'])
        if int(percent) == percent:
            percent = int(percent)
        else:
            percent = round(percent, 2)
        values['percent'] = percent

        if percent:
            values['html_props_indicator'].append(('style', f'width: {percent}%'))
        else:
            values['html_props_indicator'].append(('style', 'width: 0'))
        values['html_props'].append(('aria-valuenow', values['current']))
        values['html_props'].append(('aria-valuemin', values['min']))
        values['html_props'].append(('aria-valuemax', values['max']))

        if isinstance(values['text_position'], str):
            values['html_class'].add(
                    f'nj-progress--has-{values["text_position"]}-description')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-progress {html_class}" role="progressbar" {html_props}>
  <div class="nj-progress__bar">
    <div class="nj-progress__indicator {html_class_indicator}"
        {html_props_indicator}>
    </div>
  </div>
  {tmpl_description}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_description(self, values, context):
        """Dynamically render a part of the component's template
        """
        if not values['text_position']:
            return ''

        template = '<div class="nj-progress__description">{percent}%</div>'
        return template.format(**values)


components = {
    'Progress': ProgressBar,
}

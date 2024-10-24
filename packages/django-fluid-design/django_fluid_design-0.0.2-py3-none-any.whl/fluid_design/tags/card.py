"""
Card
====

See: https://www.engie.design/fluid-design-system/components/card/

Cards help bring hierarchy and visual consistency to the information displayed
on a page, especially when the content is heterogenous. They are excellent ways
to display rich media content like images or videos or to highlight
action-required elements.
"""
from dataclasses import dataclass, field as datafield
from typing import List, Literal, Set, Tuple
#-
from .base import HtmlClassDescriptor, HtmlPropsDescriptor, Node

class Card(Node):
    """Card component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('date', 'details', 'description', 'growth', 'header', 'image',
            'number', 'price', 'subtitle', 'title')
    "Named children."

    default_slot_tags = {
        'title': 'h4',
        'subtitle': 'h4',
    }

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        mode : Literal['default', 'cover'] = datafield(default='default')
        html_class_body : Set[str] = HtmlClassDescriptor()
        html_props_body : List[Tuple[str, str]] = HtmlPropsDescriptor()
        border : bool = datafield(default=False)
        variant : Literal['horizontal'] = datafield(default=None)
        align : Literal['center'] = datafield(default=None)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['border']:
            values['html_class'].add('nj-card--border')

        if values['variant']:
            values['html_class'].add(f'nj-card--{values["variant"]}')

        if values['align']:
            values['html_class_body'].add(f'text-{values["align"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-card {html_class}" {html_props}>
  {slot_image}
  {slot_header}
  <div class="nj-card__body {html_class_body}" {html_props_body}>
    {slot_details}
    {slot_title}
    {slot_subtitle}
    {slot_price}
    {child}
    {slot_number}
    {slot_growth}
    {slot_date}
  </div>
</{astag}>
"""
        return self.format(template, values, context)


    def render_cover(self, values, context):
        """Html output of the component
        """
        template = """
<a class="nj-card nj-card--cover {html_class}" {html_props}>
  <div class="nj-card__body {html_class_body}" {html_props_body}>
    <div class="nj-card__overlay">
      {slot_title}
      <span class="material-icons" aria-hidden="true">arrow_forward</span>
      {slot_description}
    </div>
  </div>
</a>
"""
        return self.format(template, values, context)


    def render_slot_title(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<{astag} class="nj-card__title {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return tmpl.format(**values)


    def render_slot_subtitle(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<{astag} class="nj-card__subtitle {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return tmpl.format(**values)


    def render_slot_header(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<div class="nj-card__header {html_class}" {html_props}>{child}</div>
"""
        return tmpl.format(**values)


    def render_slot_description(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<p class="nj-card__description {html_class}" {html_props}>
  {child}
</p>
"""
        return tmpl.format(**values)


    def render_slot_details(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<{astag} class="nj-card__details {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return tmpl.format(**values)


    def render_slot_image(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<{astag} class="nj-card__img-wrapper {html_class}" {html_props}>
  {child}
</{astag}>
"""
        return tmpl.format(**values)


    def render_slot_price(self, values, context):
        """Render html of the slot.
        """
        tmpl = '<div class="nj-card__price {html_class}" {html_props}>{child}</div>'
        return tmpl.format(**values)


    def render_slot_number(self, values, context):
        """Render html of the slot.
        """
        tmpl = '<p class="nj-card__number {html_class}" {html_props}>{child}</p>'
        return tmpl.format(**values)


    def render_slot_growth(self, values, context):
        """Render html of the slot.
        """
        tmpl = '<p class="nj-card__growth {html_class}" {html_props}>{child}</p>'
        return tmpl.format(**values)


    def render_slot_date(self, values, context):
        """Render html of the slot.
        """
        tmpl = '<p class="nj-card__date {html_class}" {html_props}>{child}</p>'
        return tmpl.format(**values)


class CardImage(Node):
    """Card img component
    """
    def render_default(self, values, context):
        """Html output of the component
        """
        template = '<img class="nj-card__img {html_class}" {html_props}>'
        return self.format(template, values)


class CardList(Node):
    """Card list component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        variant : Literal['columns', 'deck'] = datafield(default='deck')


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['variant']:
            values['html_class'].add(f'nj-card-{values["variant"]}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = '<div class="{html_class}" {html_props}>{child}</div>'
        return self.format(template, values)


components = {
    'Card': Card,
    'CardList': CardList,
    'CardImage': CardImage,
}

"""Base classes for fluid_design Template Tags.
"""
from dataclasses import dataclass, field as datafield, fields as datafields
import html
import logging
import re
from typing import List, Literal, Sequence, Set, Tuple
from uuid import uuid4
#-
from django import template
from django.template.base import TextNode # pylint:disable=unused-import
from django.template.base import FilterExpression, NodeList, Variable
from django.template.base import VariableDoesNotExist
from django.utils.html import strip_tags
from django.utils.translation import gettext as _
from lxml import etree
#-
from .base_widgets import CustomCheckboxInput, CustomTextarea, CustomTextInput

_logger = logging.getLogger(__name__)

SLOT_NAME_PATTERN = re.compile(r'{(tmpl|slot)_(\w+)}')
TMPL_MULTI_PATTERN = re.compile(r'(?P<name>\w+)_(?P<index>\d+)$')
VARIABLE_IN_ARG = re.compile(r'{{([\w.:|\'"]+)}}')

COLORS = ('primary', 'secondary', 'tertiary', 'destructive', 'inverse', 'brand',
        'blue', 'blue-corporate', 'green', 'grey', 'lime', 'orange', 'pink',
        'purple', 'red', 'teal', 'ultramarine', 'white', 'yellow')

def var_eval(value, context):
    """Evaluate argument passed to our Template Tag.
    """
    if isinstance(value, (VariableInVariable, FilterExpression, Variable)):
        try:
            return value.resolve(context)
        except VariableDoesNotExist:
            _logger.error("Missing variable %s", repr(value))
            return ''

    if isinstance(value, str):
        for match in VARIABLE_IN_ARG.finditer(value):
            parsed = Variable(match.group(1)).resolve(context)
            value = value.replace(match.group(0), str(parsed))

    return value


def get_props(rawprops, context):
    """Parse arguments passed to Template Tag as html attributes.
    """
    props = [(key, var_eval(val, context)) for key, val in rawprops]
    # Ignore properties with falsy value except empty string.
    return [x for x in props if (x[1] is not None and x[1] is not False) \
            or x[1] == '']


def modify_svg(xml, props):
    """Modify xml attributes of an svg image.
    """
    # pylint:disable=c-extension-no-member
    root = etree.fromstring(xml)
    for attr, value in props.items():
        if attr == 'style':
            value = ';'.join(f'{x}:{y}' for x, y in value.items())
        root.attrib[attr] = value
    return etree.tostring(root).decode()


def clean_attr_value(value):
    """Strip html of its tags and prepare it to be used as html attribute value.
    """
    value = strip_tags(value).strip().replace('\n', ' ')
    return html.escape(re.sub(r'\s\s+', ' ', value))


class HtmlClassDescriptor:
    """Property descriptor for html class names, converts string to list
    """
    _key = None

    def __set__(self, obj, value):
        if isinstance(value, str):
            # not intuitive but we append if a string was set
            values = value.split()
            try:
                getattr(obj, self._key).update(values)
            except AttributeError:
                # trying to set initial value
                setattr(obj, self._key, set(values))
        elif value is None:
            # default value
            setattr(obj, self._key, set())
        else:
            setattr(obj, self._key, value)


    def __set_name__(self, owner, name):
        self._key = f'_{name}'


    def __get__(self, obj, owner):
        if obj is None:
            return None
        return getattr(obj, self._key)


class HtmlPropsDescriptor:
    """Property descriptor for html props, convers string to key value pairs
    """
    _key = None

    def __set__(self, obj, value):
        if isinstance(value, str):
            # not intuitive but we append if a string was set
            split = [tuple(x.split(':')) for x in value.split(';')]
            try:
                getattr(obj, self._key).extend(split)
            except AttributeError:
                # trying to set initial value
                setattr(obj, self._key, split)
        elif value is None:
            # default value
            setattr(obj, self._key, [])
        else:
            setattr(obj, self._key, value)


    def __set_name__(self, owner, name):
        self._key = f'_{name}'


    def __get__(self, obj, owner):
        if obj is None:
            return None
        return getattr(obj, self._key)


class VariableInVariable:
    """Evaluate expressions in tag parameters
    """
    def __init__(self, value, parser):
        self.value = value
        self.parser = parser


    def resolve(self, context):
        """Resolve stored param
        """
        value = self.value
        for match in VARIABLE_IN_ARG.finditer(value):
            expr = FilterExpression(match.group(1), self.parser)
            parsed = expr.resolve(context)
            value = value.replace(match.group(0), parsed)
        return Variable(value).resolve(context)


    def __repr__(self):
        return f"VariableInVariable('{self.value}')"


class IgnoreMissing(dict):
    """String formatting but the variables are optional.
    """
    def __missing__(self, key):
        """Replacement string for missing variables.
        """
        return '{' + key + '}'


class DummyNodeList:
    """Fake Django template node.
    """
    def __init__(self, text):
        self.text = text
        self.attrs = {}


    def get_nodes_by_type(self, type_):
        """Dummy method that returns empty.
        """
        return []


    def render(self, context):
        """Return the passed in string.
        """
        return self.text


class Slot(template.Node):
    """Implements slots.

    This component's functionality is very simple, so there is no need to inherit
    from the Node class below.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    name = None

    @dataclass
    class Options():
        """Named arguments for the component
        """
        astag : str = datafield(default=None)
        html_id : str = datafield(default=None)
        html_class : Set[str] = HtmlClassDescriptor()
        html_props : List[Tuple[str, str]] = HtmlPropsDescriptor()
        label : str = datafield(default='')


    def __init__(self, *args, parser=None, **kwargs):
        # First argument sent by templatetag is children nodes.
        self.nodelist = args[0]
        # Second required argument is the slot's name.
        self.name = args[1]

        opts_keys = [x.name for x in datafields(self.Options)]
        self.rawopts = self.Options()
        self.rawopts = self.Options(**{key: val for key, val in kwargs.items() \
                if key in opts_keys})
        self.rawopts.html_props.extend([(key, val) for key, val in kwargs.items() \
                if key not in opts_keys])


class Node(template.Node):
    """Base class for all fluid_design tags.
    """
    WANT_CHILDREN = False
    "Template Tag needs closing end tag."
    SLOTS = ()
    "Named children."

    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ()

    default_slot_tags = {}

    context = None
    # Parent parser that was used to render this Node, when our template needs
    # Django templatetags we will clone the parser instance.
    parser = None

    @dataclass
    class Options():
        """Named arguments for the component
        """
        mode : str = datafield(default='default')
        astag : str = datafield(default='div')
        html_id : str = datafield(default=None)
        html_class : Set[str] = HtmlClassDescriptor()
        html_props : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_wrapper : Set[str] = HtmlClassDescriptor()
        html_props_wrapper : List[Tuple[str, str]] = HtmlPropsDescriptor()
        label : str = datafield(default='')
        label_suffix : str = datafield(default='')


    def __init__(self, *args, parser=None, **kwargs):
        if self.WANT_CHILDREN:
            self.nodelist = args[0]
            slots = self.nodelist.get_nodes_by_type(Slot)
            for slot in slots:
                self.nodelist.remove(slot)
            self.slots = {s.name: s for s in slots}

            self.args = args[1:]
        else:
            self.nodelist = NodeList()
            self.slots = {}
            self.args = args

        self.parser = parser

        opts_keys = [x.name for x in datafields(self.Options)]
        self.rawopts = self.Options()
        self.rawopts = self.Options(**{key: val for key, val in kwargs.items() \
                if key in opts_keys})
        self.rawopts.html_props.extend([(key, val) for key, val in kwargs.items() \
                if key not in opts_keys])


    def render(self, context):
        """Render the Template Tag as html.
        """
        opts_keys = [x.name for x in datafields(self.Options)]
        # Create local context.
        context.push({})
        # Parent Tags can set the arguments of their children Tags.
        # You can also set them to children Tags in specific slot.
        myslot = context.get('slot')
        for drop in self.CATCH_PROPS:
            if drop in context:
                for key, val in context[drop].items():
                    if key in opts_keys:
                        setattr(self.rawopts, key, val)
            if myslot and f'{myslot}_{drop}' in context:
                for key, val in context[f'{myslot}_{drop}'].items():
                    if key in opts_keys:
                        setattr(self.rawopts, key, val)

        values = {}
        self.before_prepare(values, context)
        self.prepare(values, context)

        if self.nodelist:
            values['child'] = self.nodelist.render(context).strip()
        else:
            values['child'] = ''

        self.after_prepare(values, context)

        method = getattr(self, f'render_{values["mode"]}', None)
        if not method:
            raise NotImplementedError(
                    f"Method is missing: render_{values['mode']}")

        result = method(values, context) # pylint:disable=not-callable
        # Destroy local context.
        context.pop()
        return result


    def tmpl(self, name, values, context, slots):
        """Render individual templates.

        We don't return values like we do in javascript, not needed.
        """
        slot_name = f'tmpl_{name}'
        if slot_name in slots:
            return

        method = getattr(self, f'render_tmpl_{name}')
        slots[slot_name] = method(values, context)


    def slot(self, name, values, context, slots):
        """Render individual slots.
        """
        # We don't return values like we do in javascript, not needed.
        slot_name = f'slot_{name}'
        if slot_name in slots:
            return

        slot = self.slots.get(name)
        if slot:
            # Create slot local context.
            # Use context to tell slot's children in which slot they are, for
            # example when catching props from parent tags.
            context.push({'slot': name})

            tag = var_eval(slot.rawopts.astag, context)
            if tag is None:
                tag = self.default_slot_tags.get(name, 'div')

            method = getattr(self, f'render_slot_{name}', None)
            if method:
                slot_values = {
                    'mode': values['mode'],
                    'astag': tag,
                    'label': var_eval(slot.rawopts.label, context),
                    'html_id': var_eval(slot.rawopts.html_id, context),
                    'node_id': values['html_id'],
                    'html_class': slot.rawopts.html_class,
                    'html_props': get_props(slot.rawopts.html_props, context),
                }
                self.after_prepare(slot_values, context)

                slot_values['child'] = slot.nodelist.render(context).strip()

                slots[slot_name] = method(slot_values, context) # pylint:disable=not-callable
            else:
                slots[slot_name] = slot.nodelist.render(context)

            # Destroy slot local context.
            context.pop()
        else:
            slots[slot_name] = ''


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        for key in [x.name for x in datafields(self.Options)]:
            if key.startswith('html_props'):
                values[key] = get_props(getattr(self.rawopts, key), context)
            elif key.startswith('html_class'):
                values[key] = getattr(self.rawopts, key)
            else:
                values[key] = var_eval(getattr(self.rawopts, key), context)


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        newvalues = {}
        for key in values:
            if key.startswith('html_props'):
                newvalues[f'{key}_raw'] = list(self.prune_attributes(values[key]))
                newvalues[key] = self.join_attributes(self.prune_attributes(
                        values[key]))
            elif key.startswith('html_class'):
                newvalues[key] = ' '.join(sorted(values[key]))
        values.update(newvalues)


    def prune_attributes(self, attrs):
        """Cleanup duplicate html attributes.
        """
        added_props = set()

        def _clean_attributes():
            for prop in reversed(attrs):
                prop_name = prop[0]
                if prop_name in added_props:
                    continue
                added_props.add(prop_name)
                yield prop

        return reversed(list(_clean_attributes()))


    def join_attributes(self, attrs):
        """Format html attributes.
        """
        result = []
        for att, val in sorted(attrs):
            if val is None or val is False:
                continue
            if val is True:
                result.append(att)
            else:
                val = html.escape(str(val))
                result.append(f'{att}="{val}"')
        return ' '.join(result)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """


    def eval(self, value, context):
        """Evaluate argument passed to our Template Tag.
        """
        return var_eval(value, context)


    def format(self, tpl, values, context=None, is_template=False):
        """Apply the prepared values to the templates.
        """
        if context:
            # Assume the caller want to tell us there is sub-templates.
            slots = {}
            for typ, nam in SLOT_NAME_PATTERN.findall(tpl):
                method = getattr(self, typ)
                method(nam, values, context, slots)
            if slots:
                tpl = tpl.format_map(IgnoreMissing(slots))

        try:
            result = tpl.format_map(IgnoreMissing(values))
        except ValueError:
            _logger.exception("Trying to render template:\n%s\nwith %s", tpl,
                    values)
            return ''

        if is_template:
            # We are hacking Django template engine
            tokens = template.base.Lexer(result).tokenize()
            # Trying to clone parser
            parser = template.base.Parser(tokens, origin=self.parser.origin)
            parser.libraries = self.parser.libraries
            parser.tags = self.parser.tags
            parser.filters = self.parser.filters
            # Render to string
            context.push(values)
            result = parser.parse().render(context)
            context.pop()
        return result


    def set_child_props(self, context, name, slot=None, **kwargs):
        """Use context to set arguments for all children Template Tags.
        """
        if slot:
            name = f'{slot}_{name}'
        context.setdefault(name, {})
        context[name].update(kwargs)


    def default_id(self, prefix='node'):
        """Generate unique html id.
        """
        return f'{prefix}-{uuid4().hex}'


class FormNode(Node):
    """Base class for form field tags.

    The first argument to the tag is the Django form field.
    """
    bound_field = None
    bound_value = None
    widget_class = None
    _choices = None

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_id :str = datafield(default=None)
        html_class_label : Set[str] = HtmlClassDescriptor()
        html_props_label : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_help : Set[str] = HtmlClassDescriptor()
        html_props_help : List[Tuple[str, str]] = HtmlPropsDescriptor()
        label : str = datafield(default=None)
        label_position : Literal['static', 'floating'] = datafield(
                default='static')
        help_text: str = datafield(default=None)
        hidden : bool = datafield(default=False)
        disabled : bool = datafield(default=False)
        required : bool = datafield(default=None)
        widget : str = datafield(default=None)


    def widget_kwargs(self):
        """Get Django form widget kwargs
        """
        return {}


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        super().before_prepare(values, context)
        self.bound_field = var_eval(self.args[0], context)
        self.bound_value = self.bound_field.value()

        if values['html_id'] is None:
            values['html_id'] = self.bound_field.id_for_label
        if values['label'] is None:
            values['label'] = self.bound_field.label
        if values['help_text'] is None:
            values['help_text'] = self.bound_field.help_text
        if values['required'] is None:
            values['required'] = self.bound_field.field.required


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """


    def choices(self):
        """Get Django form field choices.
        """
        if self._choices is not None:
            return self._choices
        self._choices = []

        choices = None
        try:
            # Get choices from form widget
            choices = self.bound_field.field.widget.choices
        except AttributeError:
            pass
        if choices is None:
            # Get choices from form field
            try:
                choices = self.bound_field.field.choices
            except AttributeError:
                pass
        if choices is None:
            # Construct new choices
            # Assume we are dealing with BooleanField
            default_truthy = self.bound_value or 'on'
            label = self.bound_field.label
            choices = (('', label), (default_truthy, label))

        for option_value, option_label in choices:
            if option_value is None:
                option_value = ''

            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                subchoices = option_label
            else:
                group_name = None
                subchoices = [(option_value, option_label)]

            for subvalue, sublabel in subchoices:
                self._choices.append((group_name, subvalue, sublabel))
        return self._choices


    def render_tmpl_element(self, values, context):
        """Render django form field.
        """
        bound_field = self.bound_field

        attrs = dict(values['html_props_raw'])
        attrs['id'] = values['html_id']
        attrs['class'] = set(bound_field.field.widget.attrs.get('class', '')\
            .split())
        attrs['aria-controls'] = set()
        attrs['aria-describedby'] = set()

        if bound_field.errors:
            attrs['aria-invalid'] = 'true'
            attrs['aria-describedby'].add(f'{attrs["id"]}-error')
        if values['help_text']:
            attrs['aria-describedby'].add(f'{attrs["id"]}-hint')

        self.prepare_element_props(attrs, values, context)
        if attrs['class']:
            attrs['class'] = ' '.join(sorted(attrs['class']))
        else:
            del attrs['class']
        if attrs['aria-controls']:
            attrs['aria-controls'] = ' '.join(sorted(attrs['aria-controls']))
        else:
            del attrs['aria-controls']
        if attrs['aria-describedby']:
            attrs['aria-describedby'] = ' '.join(sorted(attrs['aria-describedby']))
        else:
            del attrs['aria-describedby']

        if values['disabled']:
            attrs['disabled'] = True

        if values['hidden']:
            return bound_field.as_hidden(attrs=attrs)

        match values['widget']:
            case 'input':
                widget = CustomTextInput(attrs=attrs, **self.widget_kwargs())
            case 'textarea':
                widget = CustomTextarea(attrs=attrs, **self.widget_kwargs())
            case _:
                if self.widget_class:
                    widget = self.widget_class(attrs=attrs, **self.widget_kwargs()) # pylint:disable=not-callable
                else:
                    return bound_field.as_widget(attrs=attrs)
        return bound_field.as_widget(widget=widget, attrs=attrs)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''
        if values['required']:
            tmpl = """
<label for="{html_id}" class="nj-form-item__label {html_class_label}"
    {html_props_label}>
  {label}{label_suffix}
  <span aria-hidden="true" class="nj-form-item__required-asterisk">*</span>
</label>
"""
        else:
            tmpl = """
<label for="{html_id}" class="nj-form-item__label {html_class_label}"
    {html_props_label}>
  {label}{label_suffix}
</label>
"""
        return self.format(tmpl, values)


    def render_tmpl_help(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['help_text']:
            return ''

        tmpl = """
<p id="{html_id}-hint" class="nj-form-item__subscript {html_class_help}"
    {html_props_help}>
  {help_text}
</p>
"""
        return tmpl.format(**values)


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template.
        """
        tmpl = """
<p id="{id}-error" class="nj-form-item__subscript">
  <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">
    warning
  </span>
  {child}
</p>
"""
        message = '. '.join(self.bound_field.errors).replace('..', '.')
        return tmpl.format(id=values['html_id'], child=message)


class ChoiceSetNode(FormNode):
    """Base class for form field with multiple choices (in a fieldset).

    The first argument to the tag is the Django form field.
    """
    widget_class = CustomCheckboxInput

    def widget_kwargs(self):
        return {'check_text': self.check_test}


    def check_test(self, value):
        """ Test checked attribute

        check_test is a callable that takes a value and returns True if the
        checkbox should be checked for that value.
        """
        if not value:
            return False
        if isinstance(self.bound_value, str):
            return value == self.bound_value
        if isinstance(self.bound_value, Sequence):
            return value in self.bound_value
        return False


class DumbFormNode(Node):
    """For rendering html elements without the associated Django form fields.

    Experimental.
    """
    SLOTS = ('help', 'icon')
    "Named children."

    @dataclass
    class Options(Node.Options):
        """Named arguments for the component
        """
        html_class_label : Set[str] = HtmlClassDescriptor()
        html_props_label : List[Tuple[str, str]] = HtmlPropsDescriptor()
        html_class_help : Set[str] = HtmlClassDescriptor()
        html_props_help : List[Tuple[str, str]] = HtmlPropsDescriptor()
        hidden : bool = datafield(default=False)
        disabled : bool = datafield(default=False)
        required : bool = datafield(default=False)


    def element(self, values, context):
        """Render html of the form control.
        """
        attrs = dict(values['html_props_raw'])
        attrs['class'] = []
        if 'help' in self.slots:
            attrs['aria-describedby'] = values['html_id'] + '-hint'

        self.prepare_element_props(attrs, values, context)
        attrs['class'] = ' '.join(attrs['class'])

        if values['hidden']:
            attrs.pop('type')
            props = self.join_attributes(self.prune_attributes(attrs))
            return f'<input type="hidden" {props}>'

        return self.render_form_control(attrs, context)


    def render_form_control(self, values, context):
        """Default to rendering input, need to be overridden by subclass.
        """
        props = self.join_attributes(self.prune_attributes(values))
        return f'<input {props}>'


    def after_prepare(self, values, context):
        """Post-process the values for rendering templates.
        """
        values['element'] = self.element(values, context)
        super().after_prepare(values, context)


    def prepare_element_props(self, props, values, context):
        """Prepare html attributes for rendering the form element.
        """


    def render_slot_help(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<div id="{html_id}-hint" class="bx--form__helper-text {html_class_help}"
    {html_props_help}>
  {child}
</div>
"""
        return tmpl.format(**values)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    class="bx--btn__icon {class}" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true" {props}>
  {child}
</svg>
"""
        return tmpl.format(**values)


class Image(Node):
    """Generic img with catch props
    """
    WANT_CHILDREN = False
    "Template Tag needs closing end tag."
    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ('image_kwargs',)

    def render_default(self, values, context):
        """Html output of the component
        """
        tmpl = '<img class="{html_class}" {html_props}>'
        return self.format(tmpl, values)


components = {
    'Image': Image,
    'Slot': Slot,
}

from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class RangeSliderWidget(forms.Widget):
    template_name = 'slider.html'

    def __init__(self, name_html_elements=None, attrs=None):
        super().__init__(attrs)
        self.name_slider = name_html_elements['slider_name']
        self.min_input = name_html_elements['min_input']
        self.max_input = name_html_elements['max_input']

    def render(self, name, value, attrs=None):
        super().render(name, value, attrs)
        context = {
            'name_slider': self.name_slider,
            'min_slider_input': self.min_input,
            'max_slider_input': self.max_input
        }
        return mark_safe(render_to_string(self.template_name, context))

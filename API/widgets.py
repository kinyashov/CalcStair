from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class RangeSliderWidget(forms.Widget):
    template_name = 'slider.html'

    def __init__(self, id_html_elements=None, attrs=None):
        super().__init__(attrs)
        self.id_html_elements = id_html_elements

    def render(self, name, value, attrs=None):
        super().render(name, value, attrs)
        context = {
            'slider_name': self.id_html_elements['slider_name'],
            'min_slider_input': self.id_html_elements['min_input'],
            'max_slider_input': self.id_html_elements['max_input']
        }
        return mark_safe(render_to_string(self.template_name, context))

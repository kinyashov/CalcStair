from django.forms import Widget
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class RangeSliderWidget(Widget, minimum=0, maximum=100):
    template_name = 'slider.html'
    min_input = None
    max_input = None

    class Media:
        js = (
            'js/slider.js',
        )

    def render(self, name, value, attrs=None):
        context = {
            'url': '/'
        }
        return mark_safe(render_to_string(self.template_name, context))
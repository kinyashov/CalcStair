from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from .models import Stair


class RangeSliderWidget(forms.Widget):
    template_name = 'slider.html'

    def __init__(self, name_slider, min_input, max_input, min_value=0, max_value=100, attrs=None):
        super().__init__(attrs)
        self.name_slider = name_slider
        self.min_input = min_input
        self.max_input = max_input
        self.min_value = min_value
        self.max_value = max_value

    def render(self, name, value, attrs=None):
        super().render(name, value, attrs)
        context = {
            'name_slider': self.name_slider,
            'min_slider_input': self.min_input,
            'max_slider_input': self.max_input,
            'min_slider_value': self.min_value,
            'max_slider_value': self.max_value
        }
        return mark_safe(render_to_string(self.template_name, context))


class SliderField(forms.Field):

    def __init__(self, *, name_slider, min_input, max_input, min_value=0, max_value=100, **kwargs):
        self.widget = RangeSliderWidget(name_slider=name_slider,
                                        min_value=min_value,
                                        max_value=max_value,
                                        min_input=min_input,
                                        max_input=max_input)
        super().__init__(**kwargs)

    def validate(self, value):
        pass


class StairForm(forms.ModelForm):
    height = SliderField(name_slider='height_stair',
                         min_value=600,
                         max_value=3600,
                         min_input='min_height',
                         max_input='max_height',
                         label='Диапазон высоты лестницы')
    marsh = SliderField(name_slider='stair_marsh',
                        min_value=550,
                        max_value=1300,
                        min_input='min_marsh',
                        max_input='max_marsh',
                        label='Диапазон ширины марша')
    width_step = SliderField(name_slider='width_step',
                             min_value=100,
                             max_value=350,
                             min_input='min_width_step',
                             max_input='max_width_step',
                             label='Диапазон ширины ступени')
    width_top_step = SliderField(name_slider='width_top_step',
                                 min_value=40,
                                 max_value=300,
                                 min_input='min_width_top_step',
                                 max_input='max_width_top_step',
                                 label='Диапазон ширины верхней ступени')

    class Meta:
        model = Stair
        fields = "__all__"

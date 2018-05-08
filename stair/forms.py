from django.forms import models, fields

from .widgets import RangeSliderWidget


LIST_OF_HTML_ELEMENTS = ['slider_name', 'min_input', 'max_input']


class SliderFormField(fields.Field):

    def __init__(self, **kwargs):

        # извлекаем переменные для виджета
        # чистим kwargs для передачи родителю
        for_widget = {}
        for k in list(kwargs):
            if k in LIST_OF_HTML_ELEMENTS:
                for_widget[k] = kwargs[k]
                del kwargs[k]
        self.widget = RangeSliderWidget(id_html_elements=for_widget)
        super(SliderFormField, self).__init__(**kwargs)

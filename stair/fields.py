from django.db.models.fields import NullBooleanField
from django.utils.text import camel_case_to_spaces

from .forms import SliderFormField


class SliderField(NullBooleanField):
    empty_strings_allowed = False

    @property
    def id_html_elements(self):
        # преобразование имени объекта с помощью джанго-утилиты
        model_name = camel_case_to_spaces(self.model._meta.object_name).replace(' ', '_')
        slider_name = f"id_{model_name}"
        # TODO: получать значение pk
        min_input = f"{model_name}-0-min"
        max_input = f"{model_name}-0-max"
        return slider_name, min_input, max_input

    def formfield(self):
        slider_name, min_input, max_input = self.id_html_elements
        defaults = {'form_class': SliderFormField,
                    'slider_name': slider_name,
                    'min_input': min_input,
                    'max_input': max_input}
        return super().formfield(**defaults)

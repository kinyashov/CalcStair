from django.db.models.fields import NullBooleanField

from .forms import SliderFormField


class SliderField(NullBooleanField):
    empty_strings_allowed = False

    @property
    def id_html_elements(self):
        model_name = self.model._meta.model_name
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

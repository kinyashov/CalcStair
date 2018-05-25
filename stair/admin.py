from django.contrib import admin
from django.db import models
from django import forms

from .models import (Stair, Turn, Fence, TrackSupport, Material, Tint,
                     Height, WidthMarsh, MinWidthStep, MinWidthTopStep)


class SliderInline(admin.TabularInline):
    can_delete = False
    template = 'admin/tabular.html'


class HeightRangeInline(SliderInline):
    model = Height


class WidthMarshInline(SliderInline):
    model = WidthMarsh


class MinWidthStepInline(SliderInline):
    model = MinWidthStep


class MinWidthTopStepInline(SliderInline):
    model = MinWidthTopStep


# родителский класс для работы с объектами
class ObjectAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'created_at', 'modified_at')

    # общая функция для всех классов, которые имеют поле created_by
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class TurnAdmin(ObjectAdmin):
    pass


class FenceAdmin(ObjectAdmin):
    pass


class TrackSupportAdmin(ObjectAdmin):
    pass


class MaterialAdmin(ObjectAdmin):
    pass


class TintAdmin(ObjectAdmin):
    pass


class StairAdmin(ObjectAdmin):
    inlines = [
        HeightRangeInline, WidthMarshInline, MinWidthStepInline, MinWidthTopStepInline
    ]
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


admin.site.register(Stair, StairAdmin)
admin.site.register(Turn, TurnAdmin)
admin.site.register(Fence, FenceAdmin)
admin.site.register(TrackSupport, TrackSupportAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Tint, TintAdmin)
admin.site.register(Height)
admin.site.register(WidthMarsh)
admin.site.register(MinWidthStep)
admin.site.register(MinWidthTopStep)

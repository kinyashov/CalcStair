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


class StairAdmin(admin.ModelAdmin):
    inlines = [
        HeightRangeInline, WidthMarshInline, MinWidthStepInline, MinWidthTopStepInline
    ]
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


admin.site.register(Stair, StairAdmin)
admin.site.register(Turn)
admin.site.register(Fence)
admin.site.register(TrackSupport)
admin.site.register(Material)
admin.site.register(Tint)
admin.site.register(Height)
admin.site.register(WidthMarsh)
admin.site.register(MinWidthStep)
admin.site.register(MinWidthTopStep)

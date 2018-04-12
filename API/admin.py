from django.contrib import admin
from django.db import models
from django import forms

from .models import (
    Stair, Turn, Fence, TrackSupport, Material, Tint,
    HeightRange, WidthMarsh, MinWidthStep, MinWidthTopStep
)


class HeightRangeInline(admin.TabularInline):
    model = HeightRange


class WidthMarshInline(admin.TabularInline):
    model = WidthMarsh


class MinWidthStepInline(admin.TabularInline):
    model = MinWidthStep


class MinWidthTopStepInline(admin.TabularInline):
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
admin.site.register(HeightRange)
admin.site.register(WidthMarsh)
admin.site.register(MinWidthStep)
admin.site.register(MinWidthTopStep)

from django.contrib import admin
from django.db import models
from django import forms

from .models import Stair, Turn, Fence, TrackSupport, Material, Tint
from .forms import StairForm


class StairAdmin(admin.ModelAdmin):

    form = StairForm
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Высота лестницы', {
            'fields': (('min_height', 'max_height', 'step_height',), 'height')
        }),
        ('Ширина марша', {
            'fields': (('min_marsh', 'max_marsh', 'step_marsh'), 'marsh')
        }),
        ('Какие типы поворотов доступны', {
            'fields': ('type_turn',)
        }),
        ('Ширина ступеней', {
            'fields': (('min_width_step', 'max_width_step', 'step_width_step'), 'width_step',)
        }),
        ('Ширина верхней ступени', {
            'fields': (('min_width_top_step', 'max_width_top_step', 'step_width_top_step'), 'width_top_step',)
        }),
        ('Какие типы ограждений доступны', {
            'fields': ('type_fence',)
        }),
        ('Какие типы пристенного профиля доступны', {
            'fields': ('type_track_support',)
        }),
        ('Какие типы отделки доступны', {
            'fields': ('tint',)
        }),
        ('Какие материалы доступны', {
            'fields': ('material_stair',)
        }),
        ('Какие дополнительные элементы доступны', {
            'fields': ('visible_first_marsh', 'visible_invitation_step', 'visible_riser', 'patina', 'brush')
        }),
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


admin.site.register(Stair, StairAdmin)
admin.site.register(Turn)
admin.site.register(Fence)
admin.site.register(TrackSupport)
admin.site.register(Material)
admin.site.register(Tint)

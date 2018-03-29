from django.contrib import admin
from django.db import models
from django import forms

from .models import Stair, Turn, Fence, TrackSupport, Material, Tint
from .forms import StairForm


class StairAdmin(admin.ModelAdmin):

    form = StairForm
    fields = ('title',
              ('min_height', 'max_height'),
              'height',
              'step_height',
              ('min_marsh', 'max_marsh'),
              'marsh',
              'step_marsh',
              'type_turn',
              ('min_width_step', 'max_width_step'),
              'width_step',
              ('min_width_top_step', 'max_width_top_step'),
              'width_top_step',
              'visible_first_marsh',
              'visible_invitation_step',
              'type_fence',
              'visible_riser',
              'type_track_support',
              'material_stair',
              'tint',
              'patina',
              'brush')

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


admin.site.register(Stair, StairAdmin)
admin.site.register(Turn)
admin.site.register(Fence)
admin.site.register(TrackSupport)
admin.site.register(Material)
admin.site.register(Tint)

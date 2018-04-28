from rest_framework import serializers

from .models import *


class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = ('min', 'max', 'step')


class StairSerializer(serializers.ModelSerializer):
    height = HeightSerializer

    class Meta:
        model = Stair
        fields = ('title', 'height')

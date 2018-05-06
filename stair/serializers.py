from rest_framework import serializers

from .models import *


class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = ('min', 'max', 'step')


class WidthMarshSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidthMarsh
        fields = ('min', 'max', 'step')


class MinWidthStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinWidthStep
        fields = ('min', 'max', 'step')


class MinWidthTopStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinWidthTopStep
        fields = ('min', 'max', 'step')


class StairSerializer(serializers.ModelSerializer):
    height = HeightSerializer()
    width_marsh = WidthMarshSerializer()
    min_width_step = MinWidthStepSerializer()
    min_width_top_step = MinWidthTopStepSerializer()

    class Meta:
        model = Stair
        fields = ('title',
                  'height',
                  'width_marsh',
                  'min_width_step',
                  'min_width_top_step')

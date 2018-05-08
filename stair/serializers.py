from rest_framework import serializers

from .models import *


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class FenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fence
        fields = '__all__'


class TrackSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackSupport
        fields = '__all__'


class TintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tint
        fields = '__all__'


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
    fences = FenceSerializer(many=True)
    track_supports = TrackSupportSerializer(many=True)
    materials = MaterialSerializer(many=True)
    tints = TintSerializer(many=True)

    class Meta:
        model = Stair
        fields = ('title',
                  'height',
                  'width_marsh',
                  'min_width_step',
                  'min_width_top_step',
                  'fences',
                  'track_supports',
                  'materials',
                  'tints')

from rest_framework import serializers

from .models import *


class StairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stair
        fields = "__all__"

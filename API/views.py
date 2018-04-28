from .models import Stair
from .serializers import StairSerializer
from rest_framework import generics


class StairList(generics.ListCreateAPIView):
    queryset = Stair.objects.all()
    serializer_class = StairSerializer


class StairDetail(generics.RetrieveAPIView):
    queryset = Stair.objects.all()
    serializer_class = StairSerializer

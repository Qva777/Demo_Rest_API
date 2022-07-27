from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializers, CarListSerializers
from .models import Car


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializers


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()
    # permission_classes =


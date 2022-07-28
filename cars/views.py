from django.shortcuts import render
from rest_framework import generics

from .permissions import IsOwnerOrReadOnly
from .serializers import CarDetailSerializers, CarListSerializers
from .models import Car
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#new
# class CsrfExemptSessionAuthentication(SessionAuthentication):
#
#     def enforce_csrf(self, request):
#         return
#
#
# authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
#new

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializers


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.all()



class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Может изменять значения полей, только тот юзер который создал его"""
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)

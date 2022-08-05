from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Car
from .serializers import CarDetailSerializers, CarListSerializers
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly





class CarCreateView(generics.CreateAPIView):
    """Создание машины"""
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CarDetailSerializers


class CarListView(generics.ListAPIView):
    """Информация про все машины"""
    serializer_class = CarListSerializers
    queryset = Car.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )



class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную машину"""

    # authentication_classes = [BasicAuthentication]
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()
    permission_classes = (IsAdminOrReadOnly, )



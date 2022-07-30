from rest_framework import generics

# from .permissions import IsOwnerOrReadOnly
from .serializers import CarDetailSerializers, CarListSerializers
from .models import Car


class CarCreateView(generics.CreateAPIView):
    """Создание машины"""
    serializer_class = CarDetailSerializers


class CarListView(generics.ListAPIView):
    """Информация про все машины"""
    serializer_class = CarListSerializers
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную машину"""
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)



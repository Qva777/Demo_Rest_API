from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),

]

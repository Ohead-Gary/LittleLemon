from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BokkingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_class = [permissions.IsAuthenticated]
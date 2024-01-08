from django.shortcuts import render 
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSrializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSrializer
    permision_classes = [permissions.IsAuthenticated]

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

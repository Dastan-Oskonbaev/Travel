from rest_framework import generics, permissions

from .models import Region, Place, Hotels, Restaurants, Attractions
from .serializers import RegionSerializer, PlaceDetailSerializer, HotelsDetailSerializer, RestaurantsDetailSerializer, \
    AttractionsDetailSerializer


class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]


class PlaceDetailView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer
    permission_classes = [permissions.AllowAny]


class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsDetailSerializer
    permission_classes = [permissions.AllowAny]


class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsDetailSerializer
    permission_classes = [permissions.AllowAny]


class AttractionsDetailView(generics.RetrieveAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsDetailSerializer
    permission_classes = [permissions.AllowAny]





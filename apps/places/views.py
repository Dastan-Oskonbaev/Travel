from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Region, Place, Hotels, Restaurants, Attractions, Events
from .serializers import (RegionSerializer, PlaceDetailSerializer, HotelsDetailSerializer,
                          RestaurantsDetailSerializer, AttractionsDetailSerializer, EventsSerializer)


class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]


class PlaceDetailView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer
    permission_classes = [permissions.AllowAny]


class PlaceDestroyView(generics.DestroyAPIView):
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


class EventsFilteredList(generics.ListAPIView):
    serializer_class = EventsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        place_id = self.kwargs['place_id']
        start_date = self.request.query_params.get('start_date')
        category_id = self.request.query_params.get('category_id')

        place = get_object_or_404(Place, pk=place_id)
        events_queryset = Events.objects.filter(place=place)

        if start_date:
            events_queryset = events_queryset.filter(date=start_date)

        if category_id:
            events_queryset = events_queryset.filter(category_id=category_id)

        return events_queryset


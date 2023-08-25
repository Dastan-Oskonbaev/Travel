from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import (Favorite, FavoritePlaces, FavoriteHotels, FavoriteRestaurants, FavoriteAttractions)

from .serializers import (
    FavoritePlacesSerializer,
    FavoriteHotelsSerializer,
    FavoriteRestaurantsSerializer,
    FavoriteAttractionsSerializer, FavoriteSerializer
)

from apps.places.models import Place, Hotels, Restaurants, Attractions


class AddToFavoritePlaceView(generics.CreateAPIView):
    serializer_class = FavoritePlacesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        place_id = self.request.data.get('place_id')

        try:
            favorite = Favorite.objects.get(customer=user)
        except Favorite.DoesNotExist:
            favorite = Favorite.objects.create(customer=user)

        try:
            place = Place.objects.get(pk=place_id)
        except Place.DoesNotExist:
            raise ValidationError({"detail": "Place not found."})

        favorite_places, created = FavoritePlaces.objects.get_or_create(favorite=favorite, place=place)
        favorite_places.save()

        serializer = self.serializer_class(favorite_places)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddToFavoriteHotelView(generics.CreateAPIView):
    serializer_class = FavoriteHotelsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        hotel_id = self.request.data.get('hotel_id')

        try:
            favorite = Favorite.objects.get(customer=user)
        except Favorite.DoesNotExist:
            favorite = Favorite.objects.create(customer=user)

        try:
            hotel = Hotels.objects.get(pk=hotel_id)
        except Hotels.DoesNotExist:
            raise ValidationError({"detail": "Hotel not found."})

        favorite_hotels, created = FavoriteHotels.objects.get_or_create(favorite=favorite, hotel=hotel)
        favorite_hotels.save()

        serializer = self.serializer_class(favorite_hotels)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddToFavoriteRestaurantView(generics.CreateAPIView):
    serializer_class = FavoriteRestaurantsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        restaurant_id = self.request.data.get('restaurant_id')

        try:
            favorite = Favorite.objects.get(customer=user)
        except Favorite.DoesNotExist:
            favorite = Favorite.objects.create(customer=user)

        try:
            restaurant = Restaurants.objects.get(pk=restaurant_id)
        except Place.DoesNotExist:
            raise ValidationError({"detail": "Restaurant not found."})

        favorite_restaurants, created = FavoriteRestaurants.objects.get_or_create(favorite=favorite, restaurant=restaurant)
        favorite_restaurants.save()

        serializer = self.serializer_class(favorite_restaurants)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddToFavoriteAttractionView(generics.CreateAPIView):
    serializer_class = FavoriteAttractionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        attraction_id = self.request.data.get('attraction_id')

        try:
            favorite = Favorite.objects.get(customer=user)
        except Favorite.DoesNotExist:
            favorite = Favorite.objects.create(customer=user)

        try:
            attraction = Attractions.objects.get(pk=attraction_id)
        except Place.DoesNotExist:
            raise ValidationError({"detail": "Attraction not found."})

        favorite_attractions, created = FavoriteAttractions.objects.get_or_create(favorite=favorite, attraction=attraction)
        favorite_attractions.save()

        serializer = self.serializer_class(favorite_attractions)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewFavorite(generics.RetrieveAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        try:
            favorite = Favorite.objects.get(customer=user)
            return favorite
        except Favorite.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is not None:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"detail": "Favorite not found."}, status=404)


class RemoveFromFavoritePlaceView(generics.DestroyAPIView):
    serializer_class = FavoritePlacesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavoritePlaces.objects.filter(favorite__customer=user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {
            'favorite__customer': self.request.user,
            'place_id': self.kwargs['pk']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class RemoveFromFavoriteHotelView(generics.DestroyAPIView):
    serializer_class = FavoriteHotelsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavoriteHotels.objects.filter(favorite__customer=user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {
            'favorite__customer': self.request.user,
            'hotel_id': self.kwargs['pk']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class RemoveFromFavoriteRestaurantView(generics.DestroyAPIView):
    serializer_class = FavoriteRestaurantsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavoriteRestaurants.objects.filter(favorite__customer=user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {
            'favorite__customer': self.request.user,
            'restaurant_id': self.kwargs['pk']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class RemoveFromFavoriteAttractionView(generics.DestroyAPIView):
    serializer_class = FavoriteAttractionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavoriteAttractions.objects.filter(favorite__customer=user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {
            'favorite__customer': self.request.user,
            'attraction_id': self.kwargs['pk']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj

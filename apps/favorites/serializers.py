from rest_framework import serializers
from .models import Favorite, FavoritePlaces, FavoriteHotels, FavoriteRestaurants, FavoriteAttractions


class FavoritePlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePlaces
        fields = ('place_id',)


class FavoriteHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteHotels
        fields = ('hotel_id',)


class FavoriteRestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurants
        fields = ('restaurant_id',)


class FavoriteAttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAttractions
        fields = ('attraction_id',)


class FavPlacesSerializer(serializers.ModelSerializer):
    place_name = serializers.SerializerMethodField()
    place_id = serializers.SerializerMethodField()

    class Meta:
        model = FavoritePlaces
        fields = ('place_id','place_name',)

    def get_place_id(self, obj):
        return obj.place.pk

    def get_place_name(self, obj):
        return obj.place.name


class FavHotelsSerializer(serializers.ModelSerializer):
    hotel_id = serializers.SerializerMethodField()
    hotel_name = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteHotels
        fields = ('hotel_id', 'hotel_name',)


    def get_hotel_id(self, obj):
        return obj.hotel.id

    def get_hotel_name(self, obj):
        return obj.hotel.name


class FavRestaurantsSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.SerializerMethodField()
    restaurant_name = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteRestaurants
        fields = ('restaurant_id', 'restaurant_name',)

    def get_restaurant_id(self, obj):
        return obj.restaurant.id

    def get_restaurant_name(self, obj):
        return obj.restaurant.name


class FavAttractionsSerializer(serializers.ModelSerializer):
    attraction_id = serializers.SerializerMethodField()
    attraction_name = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteAttractions
        fields = ('attraction_id', 'attraction_name',)

    def get_attraction_id(self, obj):
        return obj.attraction.id

    def get_attraction_name(self, obj):
        return obj.attraction.name


class FavoriteSerializer(serializers.ModelSerializer):
    favorite_places = FavPlacesSerializer(many=True, read_only=True)
    favorite_hotels = FavHotelsSerializer(many=True, read_only=True)
    favorite_restaurants = FavRestaurantsSerializer(many=True, read_only=True)
    favorite_attractions = FavAttractionsSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = (
            'favorite_places',
            'favorite_hotels',
            'favorite_restaurants',
            'favorite_attractions',
        )

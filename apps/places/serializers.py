from rest_framework import serializers

from .models import (Region, WhatToTry, WhatToTryImage, Place, PlaceImage, Hotels, HotelsImage, Restaurants,
                     RestaurantsImage, EventsCategory, Attractions, AttractionsImage, Events)
from apps.reviews.serializers import ReviewSerializer


class WhatToTryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatToTryImage
        fields = (
            'id',
            'image'
        )


class WhatToTrySerializer(serializers.ModelSerializer):
    image = WhatToTryImageSerializer(many=True, required=False)

    class Meta:
        model = WhatToTry
        fields = (
            'name',
            'description',
            'region',
            'image'
        )


class PlaceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaceImage
        fields = (
            'id',
            'image'
        )


class PlacesSerializer(serializers.ModelSerializer):
    image = PlaceImageSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = (
            'name',
            'description',
            'region',
            'image',
            'average_rating',
        )


class RegionSerializer(serializers.ModelSerializer):
    what_to_try = WhatToTrySerializer(many=True,)
    places = PlacesSerializer(many=True,)

    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'photo',
            'description',
            'what_to_try',
            'places',
        )


class HotelsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelsImage
        fields = (
            'id',
            'image'
        )


class HotelsDetailSerializer(serializers.ModelSerializer):
    image = HotelsImageSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Hotels
        fields = (
            'image',
            'name',
            'description',
            'place',
            'bedrooms',
            'bathrooms',
            'car_parking',
            'pets',
            'price',
            'kitchen',
            'conditioner',
            'washer',
            'tv_netflix',
            'wifi',
            'balcony',
            'garden',
            'car_rent',
            'hairdryer',
            'iron_board',
            'pool',
            'gym',
            'game_room',
            'address',
            'phone_number',
            'reviews',
            'average_rating',
        )


class HotelsSerializer(serializers.ModelSerializer):
    image = HotelsImageSerializer(many=True, required=False)

    class Meta:
        model = Hotels
        fields = (
            'name',
            'image',
        )


class RestaurantsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantsImage
        fields = (
            'id',
            'image'
        )


class RestaurantsDetailSerializer(serializers.ModelSerializer):
    image = RestaurantsImageSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Restaurants
        fields = (
            'image',
            'reviews',
            'name',
            'description',
            'place',
            'price_range',
            'specialized_menu',
            'meal_time',
            'website',
            'address',
            'email',
            'phone_number',
        )


class RestaurantsSerializer(serializers.ModelSerializer):
    image = RestaurantsImageSerializer(many=True, required=False)

    class Meta:
        model = Restaurants
        fields = (
            'name',
            'image',
        )


class EventsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsCategory
        fields = (
            'id',
            'name',
        )


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
            'id',
            'category',
            'place',
            'name',
            'date',
            'address',
            'poster'
        )


class AttractionsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionsImage
        fields = (
            'id',
            'image'
        )


class AttractionsDetailSerializer(serializers.ModelSerializer):
    image = AttractionsImageSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Attractions
        fields = (
            'image',
            'name',
            'description',
            'place',
            'contacts',
            'reviews',
            'average_rating',
        )


class AttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = (
            'name',
        )


class PlaceDetailSerializer(serializers.ModelSerializer):
    hotels = HotelsSerializer(many=True, required=False)
    restaurants = RestaurantsSerializer(many=True, required=False)
    events = EventsSerializer(many=True, required=False)
    attractions = AttractionsSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'description',
            'region',
            'hotels',
            'restaurants',
            'events',
            'attractions',
            'reviews',
            'average_rating',
        )


class PlaceSerializer(serializers.ModelSerializer):
    events = EventsSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = '__all__'

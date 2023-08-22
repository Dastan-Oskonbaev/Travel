from rest_framework import serializers

from .models import (Region, WhatToTry, WhatToTryImage, Place, PlaceImage, Hotels, HotelsImage, Restaurants,
                     RestaurantsImage,  EventsCategory, Events, Attractions, AttractionsImage)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'name',
            'photo',
            'description'
        )


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



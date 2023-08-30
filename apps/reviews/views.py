from django.utils.translation import gettext_lazy as _

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from .models import Review, Rating, RestaurantRating
from .serializers import ReviewSerializer, RatingSerializer, RestaurantRatingSerializer
from apps.places.models import Restaurants

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewDestroyView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        if request.user != self.get_object().author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        return super().delete(request, *args, **kwargs)


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        content_type_name = self.request.data.get('content_type_name')
        object_id = self.request.data.get('object_id')

        existing_rating = Rating.objects.filter(
            user=user,
            content_type__model=content_type_name,
            object_id=object_id
        ).first()
        if existing_rating:
            raise ValidationError(_("You have already rated this content."))

        serializer.save(user=user)


class RestaurantRatingCreateView(generics.CreateAPIView):
    queryset = RestaurantRating.objects.all()
    serializer_class = RestaurantRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        restaurant = serializer.validated_data['restaurant']
        user = self.request.user
        existing_rating = RestaurantRating.objects.filter(restaurant=restaurant, user=user).exists()

        if existing_rating:
            return Response({"detail": "You have already voted for this restaurant."},
                            status=status.HTTP_400_BAD_REQUEST)

        nutrition = serializer.validated_data.get('nutrition')
        service = serializer.validated_data.get('service')
        price_quality = serializer.validated_data.get('price_quality')
        atmosphere = serializer.validated_data.get('atmosphere')

        avg_rating = (nutrition + service + price_quality + atmosphere) / 4

        serializer.save(user=user, restaurant=restaurant, rating=avg_rating)

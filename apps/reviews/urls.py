from django.urls import path

from .views import ReviewCreateView, ReviewDestroyView, RatingCreateView, RestaurantRatingCreateView


urlpatterns = [
    path('', ReviewCreateView.as_view()),
    path('<int:pk>', ReviewDestroyView.as_view()),
    path('rating/', RatingCreateView.as_view()),
    path('restaurant-rating/', RestaurantRatingCreateView.as_view()),
]

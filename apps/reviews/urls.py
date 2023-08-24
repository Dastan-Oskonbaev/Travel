from django.urls import path

from .views import ReviewCreateView, ReviewDestroyView, RatingCreateView


urlpatterns = [
    path('', ReviewCreateView.as_view()),
    path('<int:pk>', ReviewDestroyView.as_view()),
    path('rating/', RatingCreateView.as_view()),
]

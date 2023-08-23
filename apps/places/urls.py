from django.urls import path
from .views import RegionDetailView, PlaceDetailView, HotelDetailView, RestaurantDetailView, AttractionsDetailView

urlpatterns = [
    path('region_detail/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),
    path('place_detail/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    path('hotel_detail/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(),  name='restaurant-detail'),
    path('attractions_detail/<int:pk>/', AttractionsDetailView.as_view(), name='attractions-detail'),
]
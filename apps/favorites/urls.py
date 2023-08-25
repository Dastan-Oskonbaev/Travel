from django.urls import path
from .views import AddToFavoritePlaceView, AddToFavoriteHotelView, AddToFavoriteRestaurantView, \
    AddToFavoriteAttractionView, ViewFavorite, RemoveFromFavoritePlaceView, RemoveFromFavoriteHotelView, \
    RemoveFromFavoriteRestaurantView, RemoveFromFavoriteAttractionView

urlpatterns = [
    path('add-to-favorite-place/', AddToFavoritePlaceView.as_view(), name='add-to-favorite-place'),
    path('add-to-favorite-hotel/', AddToFavoriteHotelView.as_view(), name='add-to-favorite-hotel'),
    path('add-to-favorite-restaurant/', AddToFavoriteRestaurantView.as_view(), name='add-to-favorite-restaurant'),
    path('add-to-favorite-attraction/', AddToFavoriteAttractionView.as_view(), name='add-to-favorite-attraction'),
    path('favorites-view/', ViewFavorite.as_view(), name='favorite-view'),
    path('remove-from-favorite-place/<int:pk>/', RemoveFromFavoritePlaceView.as_view(), name='remove-from-favorite-place'),
    path('remove-from-favorite-hotel/<int:pk>/', RemoveFromFavoriteHotelView.as_view(), name='remove-from-favorite-hotel'),
    path('remove-from-favorite-restaurant/<int:pk>/', RemoveFromFavoriteRestaurantView.as_view(), name='remove-from-favorite-restaurant'),
    path('remove-from-favorite-attraction/<int:pk>/', RemoveFromFavoriteAttractionView.as_view(), name='remove-from-favorite-attraction'),
]

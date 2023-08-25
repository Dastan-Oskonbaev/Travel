from django.urls import path, include


from .views import CultureCategoryListView, CultureListView, CultureCategoryDetailView

urlpatterns = [
    path('culture_categories_list/', CultureCategoryListView.as_view(), name='culture_category_list'),
    path('culture_categories_detail/<int:pk>/', CultureCategoryDetailView.as_view(), name='culture_category_detail'),
    path('cultures_list/', CultureListView.as_view(), name='culture_list'),
]

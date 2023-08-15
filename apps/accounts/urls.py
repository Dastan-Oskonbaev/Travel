from django.urls import path, include

from rest_framework import routers

from .views import CustomUserViewSet

router = routers.DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += router.urls
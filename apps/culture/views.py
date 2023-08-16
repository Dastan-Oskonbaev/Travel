from django.shortcuts import render

from rest_framework import generics, permissions

from .models import CultureCategory, Culture
from .serializers import CultureCategorySerializer, CultureSerializer, CultureCategoryListSerializer


class CultureCategoryListView(generics.ListAPIView):
    queryset = CultureCategory.objects.all()
    serializer_class = CultureCategoryListSerializer
    permission_classes = [permissions.AllowAny]


class CultureCategoryDetailView(generics.RetrieveAPIView):
    queryset = CultureCategory.objects.all()
    serializer_class = CultureCategorySerializer
    permission_classes = [permissions.AllowAny]


class CultureListView(generics.ListAPIView):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    permission_classes = [permissions.AllowAny]

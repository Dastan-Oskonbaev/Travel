from django.urls import path
from .views import WhatToTryListView

urlpatterns = [
    path('what-to-try/by-region/<int:region_id>/', WhatToTryListView.as_view(), name='what-to-try-by-region'),
]
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import WhatToTry, Region
from .serializers import WhatToTrySerializer, RegionSerializer


class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.object.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]


class WhatToTryListView(generics.ListAPIView):
    serializer_class = WhatToTrySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        queryset = WhatToTry.objects.filter(region_id=region_id)
        return queryset






from rest_framework import viewsets

from .models import CustomUser
from .permissions import IsOwnerOrReadOnly
from .serializers import CustomUserSerializer, UserUpdateSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return self.serializer_class

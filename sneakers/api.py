from rest_framework import viewsets, permissions

from sneakers.models import Sneakers
from sneakers.serializers import SneakersSerializer


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneakers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SneakersSerializer


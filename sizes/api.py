from rest_framework import viewsets, permissions

from sizes.models import Sizes
from sizes.serializers import SizesSerializer


class SizesViewSet(viewsets.ModelViewSet):
    queryset = Sizes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SizesSerializer

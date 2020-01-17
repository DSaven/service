from rest_framework import viewsets, permissions

from colors.models import Colors
from colors.serializers import ColorsSerializer


class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ColorsSerializer

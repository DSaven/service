from django.http import HttpResponse
from rest_framework import viewsets, permissions

from sneakers_colors_sizes_rel.models import SneakersColorsSizesRel
from sneakers_colors_sizes_rel.serializers import SneakersColorsSizesRelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from sneakers.models import Sneakers
from colors.models import Colors
from sizes.models import Sizes


class SneakersColorsSizesRelViewSet(viewsets.ModelViewSet):
    queryset = SneakersColorsSizesRel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SneakersColorsSizesRelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id_sneaker', 'id_color', 'id_size',)


class SneakersColorsSizesRelSearch(viewsets.ModelViewSet):

    class Process:
        name = ''
        color = ''
        size = ''

        def get(self, requestName, requestColor, requestSize):
            self.name = requestName.GET.get("name", '') or ""
            self.color = requestColor.GET.get("color", '') or ""
            self.size = requestSize.GET.get("size", '') or ""

        def sqlName(self):
            if self.name == '':
                sql_name = SneakersColorsSizesRel.objects.all()
            else:
                sql_name = SneakersColorsSizesRel.objects.filter(id_sneaker__name=self.name)
            return sql_name

        def sqlColor(self):
            if self.color == '':
                sql_color = self.sqlName()
            else:
                sql_color = self.sqlName().objects.filter(id_sneaker__color=self.color)
            return sql_color

    process = Process()

    if process.size == '':
        queryset = process.sqlColor()
    else:
        queryset = process.sqlColor().filter(id_sneaker__size=process.size)

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SneakersColorsSizesRelSerializer

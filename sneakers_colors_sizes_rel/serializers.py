from rest_framework import serializers
from sneakers_colors_sizes_rel.models import SneakersColorsSizesRel


class SneakersColorsSizesRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SneakersColorsSizesRel
        fields = "__all__"


class SearchSerializer(serializers.Serializer):
    color_name = serializers.CharField()
    sneaker_name = serializers.CharField()
    size_name = serializers.CharField()

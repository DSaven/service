from rest_framework import serializers
from sizes.models import Sizes


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = "__all__"

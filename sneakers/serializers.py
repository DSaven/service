from rest_framework import serializers
from sneakers.models import Sneakers


class SneakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneakers
        fields = "__all__"

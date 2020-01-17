import json

from django.shortcuts import render
import requests
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.
from sneakers_colors_sizes_rel.serializers import SearchSerializer


class SearchViewSet(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer = SearchSerializer(data=request.data)
        response = requests.post()
        return Response(response.json())

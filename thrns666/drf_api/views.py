from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_api.serializers import MarshalliteSerializer
from mainsite.models import Product


class MarshalliteAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = MarshalliteSerializer


class UserAPIView(APIView):
    def get(self, request):
        return Response({'name': 'Henka'})

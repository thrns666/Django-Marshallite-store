from django.shortcuts import render
from rest_framework import generics
from drf_api.serializers import MarshalliteSerializer
from mainsite.models import Product


class MarshalliteAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = MarshalliteSerializer

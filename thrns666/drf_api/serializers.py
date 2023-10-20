from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from mainsite.models import Product
from orders.models import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'availability', 'price', 'cat')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['pk', 'first_name', 'phone', 'email', 'created']


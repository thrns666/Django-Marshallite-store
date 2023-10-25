from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from mainsite.models import Product
from orders.models import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'availability', 'price', 'cat')


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Order
        fields = ALL_FIELDS


from rest_framework import serializers
from mainsite.models import Product


class MarshalliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'availability', 'price', 'cat')


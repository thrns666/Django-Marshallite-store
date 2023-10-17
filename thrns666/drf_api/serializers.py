from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from mainsite.models import Product
from orders.models import Order


class MarshalliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'availability', 'price', 'cat')


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    phone = serializers.CharField(max_length=17)
    created = serializers.DateTimeField(read_only=True)
    paid = serializers.BooleanField(default=False)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('title', instance.first_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.paid = validated_data.get('paid', instance.paid)
        instance.save()
        return instance

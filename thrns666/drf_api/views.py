from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_api.serializers import MarshalliteSerializer, OrderSerializer
from mainsite.models import Product
from orders.models import Order


class MarshalliteAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = MarshalliteSerializer


class UserAPIView(APIView):
    def get(self, request):
        order_list = Order.objects.all()
        return Response({'name': OrderSerializer(order_list, many=True).data})

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'order': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Expected pk, pk not define in request.'})

        try:
            instance = Order.objects.get(pk=pk)
        except:
            return Response({'error': 'Model with defined pk not allowed.'})

        serializer = OrderSerializer(data=request.data, instance=instance, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'edited': OrderSerializer(instance).data})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Expected pk, pk not define in request.'})

        try:
            order = Order.objects.get(pk=pk)
            order.delete()
        except Order.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)

        return Response({'deleted': f'order {pk} was deleted'}, status=status.HTTP_204_NO_CONTENT)

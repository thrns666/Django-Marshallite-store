from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from drf_api.serializers import ProductSerializer, OrderSerializer
from mainsite.models import Product, SubCategories
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()

    @action(methods=['get'], detail=False, url_path='categories')
    def categories_list(self, request):
        cat_list = SubCategories.objects.all()
        return Response({'categories': cat_list.values()}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='categories/(?P<cat_id>[^/.]+)')
    def categories(self, request, cat_id):
        if cat_id.isdigit():
            cat = int(cat_id)
        else:
            return Response(
                {'error': 'Category id symbol cannot be interpreted to integer digit'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            prod_list = Product.objects.filter(cat_id=cat).values()
            cat_name = SubCategories.objects.get(id=cat).name
        except:
            return Response({'error': 'Category id is out of range'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'products': {cat_name: prod_list}})

from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from drf_api.serializers import MarshalliteSerializer, OrderSerializer
from mainsite.models import Product, SubCategories
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = MarshalliteSerializer

    @action(methods=['get'], detail=False, url_path='categories/(?P<cat_id>[^/.]+)')
    def categories(self, request, cat_id):
        # print(self.kwargs)
        # cat_id = self.kwargs.get('cat_id', None)
        cat = cat_id

        if not cat:
            Response({'error': 'wrong cat id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            prod_list = Product.objects.filter(cat_id=cat)
            cat_name = SubCategories.objects.get(id=cat).title
        except:
            return Response({'error': 'wrong category id'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'products': {cat_name: prod_list}})

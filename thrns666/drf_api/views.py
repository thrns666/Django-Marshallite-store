from rest_framework import generics, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from drf_api.serializers import ProductSerializer, OrderSerializer
from mainsite.models import Product, SubCategories
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['get'], detail=False, url_path='user/(?P<user_id>[^/.]+)')
    def order_user_list(self, request, user_id):
        print(user_id)
        if user_id.isdigit():
            user = int(user_id)
            print(user)
        else:
            return Response(
                {'error': 'User id symbol cannot be interpreted to integer digit'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # if auth and is superuser; if not - permission denide; for auth simple user another method, maybe.
            order_list = Order.objects.filter(user_id=user).values()
        except:
            return Response({'error': 'User id is out of range'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'user_id': user, 'orders': order_list}, status=status.HTTP_200_OK)


class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    permission_classes = ('IsAuthenticatedReadOnly', )

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

        return Response({'products': {cat_name: prod_list}}, status=status.HTTP_200_OK)

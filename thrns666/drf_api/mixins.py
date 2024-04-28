from django.db.models import QuerySet
from rest_framework import mixins
from rest_framework.response import Response

from orders.models import Order


class APIListMixin(mixins.ListModelMixin):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        print(request.user.id)
        queryset = self.get_queryset().filter(user=request.user.id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

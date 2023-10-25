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

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from django.urls import path
from drf_api.views import *

urlpatterns = [
    path('v1/product-list/', MarshalliteAPIView.as_view(), name='api_list'),
    path('v1/orders/', OrderAPIList.as_view(), name='test'),
    path('v1/orders/<int:pk>/', OrderAPIDetailView.as_view(), name='put_test')
]
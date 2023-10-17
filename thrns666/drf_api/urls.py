from django.urls import path
from drf_api.views import MarshalliteAPIView, UserAPIView

urlpatterns = [
    path('v1/product-list/', MarshalliteAPIView.as_view(), name='api_list'),
    path('v1/order-list', UserAPIView.as_view(), name='test'),
    path('v1/order-list/<int:pk>/', UserAPIView.as_view(), name='put_test')
]
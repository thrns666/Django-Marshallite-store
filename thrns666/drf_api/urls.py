from django.urls import path
from drf_api.views import MarshalliteAPIView, UserAPIView

urlpatterns = [
    path('v1/product-list/', MarshalliteAPIView.as_view(), name='api_list'),
    path('v1/user-api-test', UserAPIView.as_view(), name='test')
]
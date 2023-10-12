from django.urls import path
from drf_api.views import MarshalliteAPIView

urlpatterns = [
    path('product-list/', MarshalliteAPIView.as_view(), name='api_list')
]
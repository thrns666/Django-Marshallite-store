from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from thrns666 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('marshallite_cart.urls')),
    path('order/', include('orders.urls')),
    path('api/', include('drf_api.urls')),
    path('', include('mainsite.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

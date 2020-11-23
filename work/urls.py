from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from app.basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/', include('app.basic.urls')),
    path('inventory/', include('app.inventory.urls')),
    path('finance/', include('app.finance.urls')),
    path('user/', include('app.user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root, name='api_root'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

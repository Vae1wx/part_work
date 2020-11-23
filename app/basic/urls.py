from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SupplierViewSet



router = DefaultRouter()
router.register(r'root', SupplierViewSet)

urlpatterns = [
    path('basic/<int:pk>/', views.SupplierDetail.as_view()),
    path('basic/', views.SuppliertList.as_view(), name='basic_list'),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls



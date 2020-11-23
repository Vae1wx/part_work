from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InventoryViewSet
from django.urls import include



router = DefaultRouter()
router.register(r'', InventoryViewSet)

urlpatterns = [
    path('inventory/<int:pk>/', views.InventorytList.as_view(),
         name='inventory'),
    path('inventory_list/', views.InventorytList.as_view(), name='inventory_list'),

    path('stockInOrder/', views.StockInOrdertList.as_view(),
         name='stockInOrder_list'),
    path('stockInOrder/<int:pk>/', views.StockInOrderDetail.as_view()),

    path('stockInProduct/', views.StockInProductList.as_view(),
         name='stockInProduct_list'),
    path('stockInProduct/<int:pk>/', views.StockInProductDetail.as_view()),

    path('stockOutOrder/', views.StockInProductList.as_view(),
         name='stockOutOrder_list'),
    path('stockOutOrder/<int:pk>/', views.StockInProductDetail.as_view()),

    path('stockOutProduct/', views.StockOutSquareProductList.as_view(),
         name='stockOutProduct_list'),
    path('stockOutProduct/<int:pk>/', views.StockOutSquareProductDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls



from django.urls import path
from . import views


urlpatterns = [
    path('collectionOrder/<int:pk>/', views.CollectionOrderDetail.as_view(),
         name='collectionOrder'),
    path('collectionOrder/', views.CollectionOrderList.as_view(),
         name='collectionOrder_list'),

]




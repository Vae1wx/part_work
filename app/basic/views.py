from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
# Create your views here.

#   通用视图。


class SuppliertList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class SupplierViewSet(viewsets.ReadOnlyModelViewSet):
    # 此视图集自动提供“list”和“retrieve”操作。
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'basic_list': reverse('basic_list', request=request, format=format),
        'inventory_list': reverse('inventory_list', request=request, format=format),
        'stockInOrder_list': reverse('stockInOrder_list', request=request, format=format),
        'stockInProduct_list': reverse('stockInProduct_list', request=request, format=format),
        'stockOutOrder_list': reverse('stockOutOrder_list', request=request, format=format),
        'stockOutProduct_list': reverse('stockOutProduct_list', request=request, format=format),
        'collectionOrder_list': reverse('collectionOrder_list', request=request, format=format),
        'user_list': reverse('user', request=request, format=format)
    })

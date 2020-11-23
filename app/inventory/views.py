from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from .models import Inventory, StockInOrder, StockInProduct, StockOutOrder, StockOutSquareProduct
from .serializers import InventorySerializer, StockInOrderSerializer, StockInProductSerializer, StockOutOrderSerializer, StockOutSquareProductSerializer
from rest_framework.response import Response
from ..basic.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
# Create your views here.


class InventorytList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class StockInOrdertList(generics.ListCreateAPIView):
    queryset = StockInOrder.objects.all()
    serializer_class = StockInOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class StockInOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockInOrder.objects.all()
    serializer_class = StockInOrderSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class StockInProductList(generics.ListCreateAPIView):
    queryset = StockInProduct.objects.all()
    serializer_class = StockInProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class StockInProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockInProduct.objects.all()
    serializer_class = StockInProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class StockOutOrderList(generics.ListCreateAPIView):
    queryset = StockOutOrder.objects.all()
    serializer_class = StockOutOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class StockOutOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockOutOrder.objects.all()
    serializer_class = StockOutOrderSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class StockOutSquareProductList(generics.ListCreateAPIView):
    queryset = StockOutSquareProduct.objects.all()
    serializer_class = StockOutSquareProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class StockOutSquareProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockOutSquareProduct.objects.all()
    serializer_class = StockOutSquareProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]




# 分界线

class InventoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class StockInOrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockInOrder.objects.all()
    serializer_class = StockInOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class StockInProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockInProduct.objects.all()
    serializer_class = StockInProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

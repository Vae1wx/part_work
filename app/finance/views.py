from rest_framework import generics, permissions
from .models import CollectionOrder
from .serializers import CollectionOrderSerializer
from ..basic.permissions import IsOwnerOrReadOnly
# Create your views here.


class CollectionOrderList(generics.ListCreateAPIView):
    queryset = CollectionOrder.objects.all()
    serializer_class = CollectionOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CollectionOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectionOrder.objects.all()
    serializer_class = CollectionOrderSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]




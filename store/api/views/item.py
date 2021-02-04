from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from store.models import Supplier, Brand, Category, Item
from store.api.serializers import (
    SupplierSerializer, BrandSerializer, CategorySerializer, ItemSerializer)


class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

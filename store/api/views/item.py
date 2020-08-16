from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from store.models import Supplier
from store.api.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

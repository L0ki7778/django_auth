from rest_framework import generics
from market_app.models import Manufacturer, ManufacturerUser, Product
from .serializers import ManufacturerSerializer, ManufacturerUserSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated,AllowAny
from .permissions import IsStaffOrReadOnly,IsAdminForManufacturerDetailAccess,IsOwnerOrAdminForDetailAccess


class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes=[IsStaffOrReadOnly]


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    permission_classes = [IsAdminForManufacturerDetailAccess]
    serializer_class = ManufacturerSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ManufacturerUserList(generics.ListCreateAPIView):
    serializer_class = ManufacturerUserSerializer
    queryset = ManufacturerUser.objects.all()


class ManufacturerUserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManufacturerUserSerializer
    queryset = ManufacturerUser.objects.all()
    permission_classes = [IsOwnerOrAdminForDetailAccess]


class ManufacturerProductListCreate(generics.ListCreateAPIView):
    serializer_class = Product

    def get_queryset(self):
        manufacturer_id = self.kwargs['manufacturer_id']
        return Product.objects.filter(manufacturer_id=manufacturer_id)

    def perform_create(self, serializer):
        manufacturer_id = self.kwargs['manufacturer_id']
        serializer.save(manufacturer_id=manufacturer_id)

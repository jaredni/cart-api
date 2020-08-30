from django.conf.urls import include
from django.urls import path

from rest_framework import routers

from store.api import views

router = routers.SimpleRouter()

router.register(r'suppliers', views.SupplierViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
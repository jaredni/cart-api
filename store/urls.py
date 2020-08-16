from django.conf.urls import include
from django.urls import path

from rest_framework import routers

from store.api import views

router = routers.SimpleRouter()

router.register(r'suppliers', views.SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
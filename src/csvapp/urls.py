from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))

] 

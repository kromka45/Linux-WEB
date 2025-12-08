from rest_framework import routers
from django.urls import include, path
from .views import ModyViewSet


router = routers.DefaultRouter()

router.register(r'mods', ModyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),




]


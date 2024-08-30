from django.urls import include, path
from rest_framework import routers

from .views import(ProductViewSet, MovementsViewSet)


router = routers.DefaultRouter()
router.register(r'product', ProductViewSet )
router.register(r'movements', MovementsViewSet )


urlpatterns = [
    path('', include(router.urls))
]



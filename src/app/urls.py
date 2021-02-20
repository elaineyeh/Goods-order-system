from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.authentication.views import UserViewSet
from app.good.views import GoodViewSet
from app.order.views import OrderViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'goods', GoodViewSet)
router.register(r'order', OrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
]

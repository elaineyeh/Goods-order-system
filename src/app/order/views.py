from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import Order, OrderGood
from app.good.models import Good
from .serializers import OrderGoodSerializer, OrderSerializer

class OrderViewSet(mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        if request.user.is_authenticated and request.user.id == request.data["user"]:
            order = Order.objects.create(user=request.user)
            for good in request.data["goods"]:
                good_id = Good.objects.get(id=good["good"])
                good_id.stock = good_id.stock-good["amount"]
                if good_id.stock < 0:
                    return Response("Good aren't enough.", status=status.HTTP_400_BAD_REQUEST)
                good_id.save()
                OrderGood.objects.create(order=order, good=good_id, amount=good["amount"])
            return Response(status=status.HTTP_201_CREATED)
        raise PermissionDenied()

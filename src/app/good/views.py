from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .serializers import GoodSerializer
from .models import Good


class GoodViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (IsAuthenticated, )

    def partial_update(self, request, pk):
        good = Good.objects.get(pk=pk)
        if request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data, instance=good)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        raise PermissionDenied()

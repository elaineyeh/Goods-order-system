from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    @action(['GET'], False)
    def information(self, request):
        if request.user.is_authenticated:
            serializer = self.get_serializer(instance=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        raise PermissionDenied()

    def partial_update(self, request, pk):
        user = User.objects.get(pk=pk)
        if request.user.is_authenticated and request.user == user:
            serializer = self.get_serializer(data=request.data, instance=request.user)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise PermissionDenied()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serizlizer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

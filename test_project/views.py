from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import UserSerializers, KittyandHedgehogSerializers
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.generics import get_object_or_404

"""class UserView(APIView):
    def get(self, request, **data):
        user = User.objects.all()
        serializer = UserSerializers(
            instance=user,
            many=True
        )
        return Response(serializer.data)"""

"""    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


class UserView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class KittyandHedgehogView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = KittyandHedgehog.objects.all()
    serializer_class = KittyandHedgehogSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def peform_create(self, serializer):
        user = get_object_or_404(User, user_name = self.request.data.get('test_project_user.id'))
        return serializer.get(user=user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

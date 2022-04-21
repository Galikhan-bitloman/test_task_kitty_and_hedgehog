# std imports


from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.generics import get_object_or_404


from test_task_kitty_and_hedgehog.models import User
from test_task_kitty_and_hedgehog.serializers import UserSerializers, KittyandHedgehogSerializers


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

    def perform_create(self, serializer):
        user_name = self.request.data.get('owner')
        user = get_object_or_404(User, user_name=user_name)
        return serializer.get(user=user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

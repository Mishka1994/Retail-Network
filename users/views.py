from rest_framework import generics
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.create(
            username=request.data['username']
        )
        user.set_password(request.data['password'])
        user.save()

        return Response({'status': 200, 'result': 'Пользователь создан'})



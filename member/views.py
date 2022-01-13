import json

from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from member.models.user import User
from member.serializers import UserSerializer, ChangePasswordSerializer

from django.utils.translation import gettext_lazy as _


class UserView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    # url: GET/user/ => user detail

    # POST인 경우에는 authentication_class를 다르게 주기 위해
    def get_authenticators(self):
        if self.request.method == 'POST':
            self.authentication_classes = ()

        return super().get_authenticators()

    def get(self, request):
        user_obj = request.user
        serializer = UserSerializer(instance=user_obj)
        return Response(serializer.data, status=200)
        # return Response("test okok!!", status=200)

    # url: POST/user/ => 회원가입 기능
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    # url: PUT/user/ => user 정보 수정
    def patch(self, request):
        user_obj = request.user
        serialzier = UserSerializer(instance=user_obj, data=request.data, partial=True)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=200)
        else:
            return Response(serialzier.errors, status=400)

    # url: DELETE/user/ => user 정보 삭제
    def delete(self, request):
        user_obj = request.user
        user_obj.delete()
        return Response("Delete complete!!", status=200)


@api_view(['POST'])
def find_id(request):
    email = request.data.get('email', None)
    if User.objects.filter(email=email).exists():
        user_obj = User.objects.get(email=email)
        return Response(
            {
                "message": _(f"username: {user_obj.username}")
            },
            status=200,
        )

    else:
        return Response(
            {
                "user_not_found": _("Can't find any account matching with email"),
            },
            status=400,
        )


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def patch(self, request, *args, **kwargs):
        username = request.data.get('username')
        user_obj = User.objects.get(username=username)
        serializer = self.get_serializer(instance=user_obj, data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)

            return Response(
                {
                    "message": _("Password Change Success!")
                },
                status=200,
            )
        else:
            return Response(
                {
                    "user_not_found": _("Can't find any account matching with username"),
                },
                status=400,
            )

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)


# TODO JWT 어떻게 불러오지?
@api_view(['POST'])
def reset_pw(request):
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)

    # if User.objects.filter(username=username).exists():
    #     user_obj = User.objects.get(username=username)
    #     return Response("success!", status=200)
    # else:
    #     return Response(
    #         {
    #             "user_not_found": _("Can't find any account matching with username"),
    #         },
    #         status=400,
    #     )

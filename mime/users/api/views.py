# from django.contrib.auth import get_user_model
# from rest_framework import viewsets
# from rest_framework.views import generics
#
# from mime.users.api.serializers import UserSerializer
#
# User = get_user_model()
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # class UserViewSet(viewsets.ReadOnlyModelViewSet):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer

from rest_framework import generics
from .serilizers import  UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


from rest_framework import generics
from .serializers import  UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import mixins

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"}) 
    else:
        data = {
          "error": True,
          "errors": serializer.errors,          
        }
        return Response(data)

@api_view(["GET"])
def user_details(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["GET", "PUT"])
def user_update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True}) 
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response({"message": "Deleted"})


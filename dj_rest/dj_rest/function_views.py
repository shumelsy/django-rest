from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizers import UserSerializer


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


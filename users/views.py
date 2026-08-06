from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Tier
from .serializers import UserSerializer, TierSerializer

class TierView(APIView):
  def post(self, request):
    trier_obj = TierSerializer(data=request.data)
    if trier_obj.is_valid():
      trier_obj.save()
      message = {
        "sucess": "Tier sucessfully Created"
      }
      return Response(message, status=status.HTTP_200_OK)

    return Response(trier_obj.errors, status=status.HTTP_400_BAD_REQUEST)
  

    
# Create your views here.
class UserView(APIView):
  def post(self, request):
    user_obj = UserSerializer(data=request.data)

    if user_obj.is_valid():
      user_obj.save()
      message = {
        "sucess": "User sucessfully Created"
      }
      return Response(message, status=status.HTTP_200_OK)

    return Response(user_obj.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
      if id :
        try: 
          user_obj = User.objects.get(id=id)
        except User.DoesNotExist:
          message = {
            "error": "User Does not exist ... Check it"
          }
          return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer_obj = UserSerializer(user_obj)
        return Response(serializer_obj.data, status=status.HTTP_200_OK)

      user_objs = User.objects.all()
      serializer_objs = UserSerializer(user_objs, many=True)
      return Response(serializer_objs.data, status=status.HTTP_200_OK)

  def patch(self, request, id):
    try:
      user_obj = User.objects.get(id=id)
    except User.DoesNotExist:
      message = {"error": "User Not Exists"}
      return Response(message, status=status.HTTP_404_NOT_FOUND)

    
    serializer_obj = UserSerializer(user_obj, data=request.data)


    if serializer_obj.is_valid():
      serializer_obj.save()
      message = {
        "sucess": "User changes sucessfully Updated..."
      }
      return Response(message, status=status.HTTP_200_OK)

    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
 

    

    

    
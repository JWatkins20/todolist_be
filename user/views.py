from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import *
import json

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

@api_view(['GET'])
def get_list(request):
    user = request.user
    todolist = list(user.todolist.all().values())
    return Response({'todolist': todolist}, status=status.HTTP_200_OK)

@api_view(['POST'])
def edit_list(request):
    user = request.user
    edited_list = request.data['todolist']
    user.todolist.clear()
    for i in range(len(edited_list)):
        item = todoitem.objects.create(description=edited_list[i]['description'], index=edited_list[i]['id'])
        user.todolist.add(item)
    user.save()
    return Response(status=status.HTTP_200_OK)
    

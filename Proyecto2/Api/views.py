from django.shortcuts import render
from rest_framework import viewsets
from .models import UsuarioNuevo
from .serializers import UsuarioNuevoserializers
# Create your views here.


class UserNuevoViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioNuevoserializers
    queryset = UsuarioNuevo.objects.all()

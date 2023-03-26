from rest_framework import serializers
from .models import UsuarioNuevo


class UsuarioNuevoserializers(serializers.ModelSerializer):
    class Meta:
        model = UsuarioNuevo
        fields = '__all__'  #es una lista donde uno coloca ['nombre','telefono']



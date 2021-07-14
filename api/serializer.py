from rest_framework import serializers

# Serializers define the API representation.
from core.models import Noticia


class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

from rest_framework import viewsets

from api.serializer import NoticiaSerializer
from core.models import Noticia


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

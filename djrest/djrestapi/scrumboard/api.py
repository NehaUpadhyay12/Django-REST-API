from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import List, Card
from .serializer import ListSerializer, CardSerializer

class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permissions_classes = (permissions.IsAuthenticated,)

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permissions_classes = (permissions.IsAuthenticated,)
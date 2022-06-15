from .models import Games
from django_grpc_framework import generics
from serializers import GameProtoSerializer


class GameService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = Games.objects.all().order_by('-date_joined')
    serializer_class = GameProtoSerializer
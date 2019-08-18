from rest_framework import viewsets

from gamesapi.models.game_model import Game
from gamesapi.serializers import GameSerializer


class GameView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

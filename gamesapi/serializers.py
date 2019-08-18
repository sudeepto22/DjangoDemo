from rest_framework import serializers

from gamesapi.models.game_model import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'url', 'title', 'platform', 'score', 'genre', 'editors_choice')
        # fields = '__all__'

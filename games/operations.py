import requests
from constants.app_constants import AppConstants
from games.game_model import GameModel


def get():
    r = requests.get(AppConstants.URL.value)
    print(r.json())


def post(game_model: GameModel):
    data = {
        'title': game_model.title,
        'platform': game_model.platform,
        'score': game_model.score,
        'genre': game_model.genre,
        'editors_choice': game_model.editors_choice
    }
    requests.post(url=AppConstants.URL.value, data=data)


# if __name__ == '__main__':
#     game = GameModel('NHL 13', 'Xbox 360', 8.5, 'Sports', 'N')
#     post(game)
#     get()

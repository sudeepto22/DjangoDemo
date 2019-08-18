from django.urls import path, include
from gamesapi.viewmodel import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games', views.GameView)

urlpatterns = [
    path('', include(router.urls))
]

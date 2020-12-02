from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('games/', include("games.urls", namespace='games')),
    path('players/', include("players.urls", namespace='players')),
]

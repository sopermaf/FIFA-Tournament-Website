from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fifa/', include("fifa.urls")),
]

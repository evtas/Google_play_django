from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search, name='search'),
    path("<int:game_id>", views.details, name='details'),
    path("download/<int:game_id>", views.download, name='download'),
    path("test", views.test, name='test'),
]
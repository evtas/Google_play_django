from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search, name='search'),
    path("detail/<int:game_id>", views.details, name='details'),
    path("download/<int:game_id>", views.download, name='download'),
    path('test_load_banlance/', views.nginx_view, name="nginx_view"),
    path("test", views.test, name='test'),
]
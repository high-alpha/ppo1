from django.urls import path, re_path
from . import views
urlpatterns = [
re_path(r'^$', views.enemy_list, name='enemy_list'),
re_path(r'^weapons$', views.weapon_list, name='weapon_list'),
]
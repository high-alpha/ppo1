from django.urls import path, re_path
from . import views
urlpatterns = [
re_path(r'^$', views.enemy_list, name='enemy_list'),
re_path(r'^weapons$', views.weapon_list, name='weapon_list'),
re_path(r'^weapons/new/$', views.weapon_new, name='weapon_new'),
re_path(r'^enemies/new/$', views.enemy_new, name='enemy_new'),
]
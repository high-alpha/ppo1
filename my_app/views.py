from django.shortcuts import render
from django.http import HttpResponse
from .models import Enemy

# Create your views here.
'''
def enemy_list(request):
	html=  "<html><body><H1>Вот они, вражины!!!</H1></body></html>"
	return HttpResponse(html)
'''
def enemy_list(request):
	enemies = Enemy.objects.order_by('name')
	return render(request, 'my_app/enemy_list.html', {'enemies': enemies})

def weapon_list(request):
	weapons = Weapon.objects.order_by('title')
	return render(request, 'my_app/weapon_list.html', {'weapons': weapons})
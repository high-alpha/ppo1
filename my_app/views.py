from django.shortcuts import render
from django.http import HttpResponse
from .models import Enemy
from .models import Weapon
from .forms import EnemyForm
from .forms import WeaponForm
from django.shortcuts import redirect
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
'''
def enemy_new(request):
	form = EnemyForm()
	return render(request, 'my_app/enemy_edit.html', {'form': form})
	'''
def enemy_new(request):
	if request.method == "POST":
		form = EnemyForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('enemy_list')
	else:
		form = EnemyForm()
	return render(request, 'my_app/enemy_edit.html', {'form': form})

def weapon_new(request):
	if request.method == "POST":
		form = WeaponForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('weapon_list')
	else:
		form = WeaponForm()
	return render(request, 'my_app/weapon_edit.html', {'form': form})
from django.contrib import admin


from .models import EnemyType
from .models import Enemy
from .models import Weapon
# Register your models here.
admin.site.register(EnemyType)
admin.site.register(Enemy)
admin.site.register(Weapon)

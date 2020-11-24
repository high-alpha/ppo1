from django import forms

from .models import EnemyType
from .models import Enemy
from .models import Weapon
'''
class EnemyTypeForm (forms.ModelForm):
    class Meta:
        model = EnemyTypefields = ('type',)
'''
class EnemyForm (forms.ModelForm):
    class Meta:
        model = Enemy
        fields = ('name','power','shield','etype',)

class WeaponForm (forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ('title','damage',)
from django.db import models

# Create your models here.
class EnemyType (models.Model):
	type = models.CharField(max_length=50)

	def publish(self):
		self.save()

	def __str__(self):
		return self.type

class Enemy (models.Model):
	name = models.CharField(max_length=50)
	power = models.IntegerField()
	shield = models.IntegerField()
	etype = models.ForeignKey(EnemyType, on_delete=models.CASCADE, default = 0)

	def publish(self):
		self.save()

	def __str__(self):
		return self.name

class Weapon (models.Model):
	title = models.CharField(max_length=50)
	damage = models.IntegerField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.title

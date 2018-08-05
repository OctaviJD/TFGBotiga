from django.db import models
from django.utils import timezone

class Recipe(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to='recipe/%Y/%m/%d', blank=True)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
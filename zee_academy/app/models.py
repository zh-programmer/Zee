from django.db import models
from django.urls import reverse

class Free_Tutorials(models.Model):
	title = models.CharField(max_length = 100)
	thumb = models.CharField(max_length = 30)
	body = models.CharField(null = True , max_length = 100)

	def get_absolute_url(self):
		return reverse("home")


class Paid_Courses(models.Model):
	title = models.CharField(max_length = 100)
	thumb = models.CharField(max_length = 30)
	body = models.CharField(null = True , max_length = 100)

	def get_absolute_url(self):
		return reverse("paid_courses")
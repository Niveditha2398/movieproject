from django.db import models

# Create your models here.
class Moviedetails(models.Model):
	releasedate = models.DateField()
	moviename = models.CharField(max_length=20)
	hero = models.CharField(max_length=20)
	heroine = models.CharField(max_length=20)
	rating = models.IntegerField()
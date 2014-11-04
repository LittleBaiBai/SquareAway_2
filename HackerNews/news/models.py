from django.db import models

class News(models.Model):
	title = models.CharField(max_length=200)
	score = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published') 
# Create your models here.

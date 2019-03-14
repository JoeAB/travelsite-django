from django.conf import settings
from django.db import models


# Create your models here.
class BlogPost(models.Model):
	country_code = models.TextField(max_length=3)
	title = models.TextField(max_length=150)
	text = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

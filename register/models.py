from django.db import models

# Create your models here.
class Record(models.Model):
	ts = models.DateTimeField('timestamp', auto_now_add=True)
	ip = models.CharField('ip address', max_length=20)
	email = models.CharField('e-mail', max_length=120)


class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

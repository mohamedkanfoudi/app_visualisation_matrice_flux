from django.db import models

# Create your models here.

class network(models.Model):
    ip = models.CharField(max_length=80)
    port = models.IntegerField()
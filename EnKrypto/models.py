
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class KeyStorage(models.Model):
    name = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    key = models.CharField(max_length=50)

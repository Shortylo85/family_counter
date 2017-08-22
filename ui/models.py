from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=64, null=True, blank=True)
    user = ForeignKey(User)

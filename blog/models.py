# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
User =settings.AUTH_USER_MODEL
# Create your models here.
class blogpost(models.Model):
    user=models.ForeignKey(User, default=1,null=True ,on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    slug= models.SlugField(unique=True, blank=False)
    content= models.TextField(null=True, blank=True)


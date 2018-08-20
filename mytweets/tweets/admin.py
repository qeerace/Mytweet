# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tweets.models import Tweet
admin.site.register(Tweet)

# Register your models here.
def __str__(self):
    return self.text

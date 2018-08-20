# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    if request.method == 'GET':
        return HttpResponse('I am called from a get Request')
    elif request.method == 'POST':
        return HttpResponse('I am called from a post Request')

from django.views.generic import View
from django.shortcuts import render
from user_profile.models import User
from tweets.models import Tweet
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)

from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.db.models import Q

from accounts.models import Account

from accounts.models.accounts import UserCategoryChoices


class IndexView(TemplateView):
    template_name = 'index.html'

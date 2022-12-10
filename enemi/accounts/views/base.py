from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.db.models import Q

from accounts.models import Account

from accounts.models.accounts import UserCategoryChoices


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['types'] = UserCategoryChoices.choices
        print(context['types'])
        return context

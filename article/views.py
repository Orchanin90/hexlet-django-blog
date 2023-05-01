from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        print(args, kwargs, request)

        return HttpResponse(
            f'Статья номер {kwargs["article_id"]}. Тег {kwargs["tags"]}')

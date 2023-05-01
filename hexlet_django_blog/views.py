from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView


def index(request):
    return redirect(
        reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['who'] = 'Vadim'
#         return context


def about(request):
    return render(request, 'about.html')

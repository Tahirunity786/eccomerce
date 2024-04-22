from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from core_control.models import Product


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Fetch all products from the database
        return context
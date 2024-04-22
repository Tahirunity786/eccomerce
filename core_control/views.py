from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from core_control.models import Product

# REST API LIBRARY
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status





class Login(TemplateView):

    template_name = 'core_control/login.html'

    def get(self, request):

        return render(request, self.template_name)
    



class Register(TemplateView):
    template_name = 'core_control/form.html'

    def get(self, request):
        # Render the registration form
        return render(request, self.template_name)


class Plate_Detail(TemplateView):

    template_name = 'core_control/product-detail.html'

    def get(self, request, slug):

        product_detailer = Product.objects.get(product_slug = slug)

        return render(request, self.template_name, {"content":product_detailer})
    
class Cart(TemplateView):

    template_name = 'core_control/cart.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Private_Plate(TemplateView):

    template_name = 'core_control/private-plates.html'
    model = Product.objects.all()

    def get(self, request):
        data={
            "product":self.model
        }
        return render(request, self.template_name, data)


class Faqs(TemplateView):
    template_name = 'core_control/freq-q-ans.html'

    def get(self,request):

        return render(request, self.template_name)
    

class Contact(TemplateView):
    template_name = 'core_control/contact.html'

    def get(self,request):

        return render(request, self.template_name)
    

class Checkout(TemplateView):
    template_name = "core_control/checkout.html"

    def get(self, request):

        return render(request, self.template_name)
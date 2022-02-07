
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from productapp.models import Product






# Create your views here.
#def welcome(request):

    #return render(request,'productapp/product_index.html')

class ProductList(ListView):
    model=Product
    context_object_name='Products'
    template_name='productapp/product_index.html'




def displayproduct(request):
    values={"name":"Abc","Address":"Texas","phone":"4465454"}
    return render(request,'productapp/displayproducts.html',values)


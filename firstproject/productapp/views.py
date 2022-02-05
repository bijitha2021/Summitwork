from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.
def welcome(request):

    return render(request,'productapp/product_index.html')


def displayproduct(request):
    values={"name":"Abc","Address":"Texas","phone":"4465454"}
    return render(request,'productapp/displayproducts.html',values)


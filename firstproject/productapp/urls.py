from productapp.views import displayproduct
#from productapp.views import welcome
from django.urls import path
from productapp import views


app_name='productapp'
urlpatterns = [
    path('', views.ProductList.as_view(),name='Product'),
    path('products/', displayproduct),

]

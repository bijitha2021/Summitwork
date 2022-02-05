from productapp.views import displayproduct
from productapp.views import welcome
from django.urls import path


urlpatterns = [
    path('', welcome),
    path('products/', displayproduct),

]

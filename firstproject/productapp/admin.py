from django.contrib import admin


# Register your models here.
from productapp.models import Product

admin.site.register(Product)

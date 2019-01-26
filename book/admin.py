from django.contrib import admin

# Register your models here.
from .models import Book, BuyingHistory

admin.site.register(Book)
admin.site.register(BuyingHistory)

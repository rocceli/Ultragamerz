from django.contrib import admin
from .models import message,product,category,order


admin.site.register(message)
admin.site.register(product)
admin.site.register(category)
admin.site.register(order)

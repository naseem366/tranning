from django.contrib import admin
from .models import Customer,Category,EmpModel
# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(EmpModel)


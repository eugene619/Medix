from django.contrib import admin
from medixapp.models import Product, Branch, Contact, Appointment, Member, Admin


# Register your models here.
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Member)
admin.site.register(Admin)


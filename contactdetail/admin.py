from django.contrib import admin
from contactdetail.models import Contactform

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_desplay=('username','useremail')
admin.site.register(Contactform,ContactAdmin)    
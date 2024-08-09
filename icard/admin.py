from django.contrib import admin
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=('user','first_name', 'last_name', 'email', 'mobile_no', 'photo','current_company')
admin.site.register(Person,PersonAdmin)
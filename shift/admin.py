from django.contrib import admin
from .models import JobShift
# Register your models here.
class JobShiftAdmin(admin.ModelAdmin):
    list_display=('username', 'current_company', 'desired_company', 'mobile_no', 'email')
admin.site.register(JobShift,JobShiftAdmin)
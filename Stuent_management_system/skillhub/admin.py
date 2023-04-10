from django.contrib import admin
from .models import Department,Role,Person,Year
from .forms import Personform
# Register your models here.

class Personadmin(admin.ModelAdmin):
   list_display = ['first_name', 'last_name', 'dept','year','role','phone']
   form = Personform
   list_filter = ['role']
   search_fields = ['first_name', 'last_name', 'phone']


admin.site.register(Person,Personadmin)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Year)
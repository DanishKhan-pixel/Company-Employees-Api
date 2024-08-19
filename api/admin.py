from django.contrib import admin
from api.models import company, Employee
# Register your models here.


class companyAdmin(admin.ModelAdmin):
    list_display=('name',"location",'type','about')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    search_fields=('name',)
    list_filter=('company',)


admin.site.register(company, companyAdmin)
admin.site.register(Employee, EmployeeAdmin)



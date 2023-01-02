from django.contrib import admin
from .models import Customer
from import_export.admin import ImportExportModelAdmin  
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['first_name','permanent_address','temporary_address','mobile_number','active']

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display=  ('id','first_name','middle_name','last_name','temporary_address','permanent_address','email_id','mobile_no','active')

# Register your models here.

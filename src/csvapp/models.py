from django.db import models

class Customer(models.Model):

    first_name = models.CharField(max_length=40, help_text="First name should be max. of 40 characters")
    middle_name = models.CharField(max_length=40, blank=True,  help_text="Middle name should be max. of 40 characters")
    last_name = models.CharField(max_length=40, help_text="Last name should be max. of 40 characters")
    permanent_address= models.CharField(max_length=50, help_text=" Permanent Address should be max. of 50 characters")
    temporary_address = models.CharField(max_length=50, help_text=" Temporary Address should be max. of 50 characters")
    mobile_no = models.CharField(max_length=15, blank=True, help_text="Mobile no. should be max. of 15 characters")
    email_id = models.CharField(max_length=50, blank=True, help_text="Email Id should be max. of 50 characters")
    active = models.BooleanField(default=True)


class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to="excel")





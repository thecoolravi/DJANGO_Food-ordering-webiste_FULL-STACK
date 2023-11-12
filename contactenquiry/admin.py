from django.contrib import admin
from contactenquiry.models import contactenquiry

# Register your models here.

class contact_enquiry(admin.ModelAdmin):
    list_display = ('name','email','phone','message')

admin.site.register(contactenquiry,contact_enquiry) 
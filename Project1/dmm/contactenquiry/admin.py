from django.contrib import admin
from contactenquiry.models import enquiry
# Register your models here.
class enquiryadmin(admin.ModelAdmin):
    list_display = ("e_name","e_email","e_message")

admin.site.register(enquiry,enquiryadmin)


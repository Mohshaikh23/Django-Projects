from django.db import models

# Create your models here.
class enquiry(models.Model):
    e_name = models.CharField(max_length=50)
    e_email = models.CharField(max_length=50)
    e_message = models.TextField()
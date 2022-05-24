from django.db import models

# Create your models here.
# STATUS_CHOICES = (
#     ("pending", "Pending"),
#     ("approved", "Approved"),
#     ("rejected", "Rejected"),
# )

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    education = models.CharField(max_length=100, default="")
    experience = models.CharField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=1000, null=True, blank=True)
    description = models.TextField(default=None, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume/', null='False', blank='False', verbose_name='File')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default='Applied')

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    hours = models.TimeField()
    notes = models.TextField(max_length=250, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    location = models.IntegerField()
    phone = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True)

    def get_photo(self):
        return f"Photo for shoe_id: {self.resource_id} @{self.url}"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shoes_detail', kwargs={'shoe_id': self.id})

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Resource(models.Model):
    # constants for the enum field, category.
    UNKNOWN = "UNKNOWN"
    FOOD = "FOOD"
    CLOTHING = "CLOTHING"
    ADDICTION_RECOVERY = "ADDICTION_RECOVERY"
    HYGIENE = "HYGIENE"
    FINANCIAL_EMPOWERMENT = "FINANCIAL_EMPOWERMENT"
    SHELTER = "SHELTER"
    WOMEN_AND_CHILDREN = "WOMEN_AND_CHILDREN"
    MENTAL_HEALTH_SERVICES = "MENTAL_HEALTH_SERVICES"
    FINANCIAL_EMPOWERMENT = "FINANCIAL_EMPOWERMENT"
    MEDICAL_ASSISTANCE = "MEDICAL_ASSISTANCE"

    CATEGORIES = (
        (UNKNOWN, "Unknown"),
        (FOOD, "Food"),
        (CLOTHING, "Clothing"),
        (ADDICTION_RECOVERY, "Addiction Recovery"),
        (HYGIENE, "Hygiene"),
        (FINANCIAL_EMPOWERMENT, "Financial Empowerment"),
        (SHELTER, "Shelter"),
        (WOMEN_AND_CHILDREN, "Women and Children"),
        (MENTAL_HEALTH_SERVICES, "Mental Health Services"),
        (FINANCIAL_EMPOWERMENT, "Financial Empowerment"),
        (MEDICAL_ASSISTANCE, "Medical Assistance")
    )

    resource_name = models.CharField(max_length=100)
    # TODO: org_name can be a ForeignKey.
    org_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, 
                                choices=CATEGORIES,
                                default=UNKNOWN)
    hours = models.TimeField()
    address = models.CharField(max_length=100, blank=True)
    street_number = models.CharField(max_length=100, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    long = models.DecimalField(max_digits=12, decimal_places=6)
    lat = models.DecimalField(max_digits=12, decimal_places=6)
    phone = PhoneNumberField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True)
    notes = models.TextField(max_length=250, blank=True)

    ordering = ['org_name', 'category', 'resource_name']

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return f'{self.org_name}: {self.resource_name}'

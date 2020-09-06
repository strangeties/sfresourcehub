from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    org_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, 
                                choices=CATEGORIES,
                                default=UNKNOWN)
    hours = models.TimeField()
    notes = models.TextField(max_length=250, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(blank=True, default=123456789)
    long = models.DecimalField(max_digits=12, decimal_places=6, default=0.000)
    lat = models.DecimalField(max_digits=12, decimal_places=6, default=0.000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('index')

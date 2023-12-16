from django.db import models
from django.core.validators import RegexValidator
class Register(models.Model):
    email=models.EmailField()
    company_name=models.CharField(max_length=30)
    contact=models.IntegerField()
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    password=models.CharField(max_length=50, unique=True, validators=[alphanumeric])





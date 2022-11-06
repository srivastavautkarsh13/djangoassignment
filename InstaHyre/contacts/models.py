from django.db import models
from users.models import User


class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    spam_flag = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
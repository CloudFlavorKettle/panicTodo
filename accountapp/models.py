from django.db import models
from django.contrib.auth.models import User as DjangoUser


# Create your models here.
class User(DjangoUser):

    def get_full_name(self):
        return self

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self

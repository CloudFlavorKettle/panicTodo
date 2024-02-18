from django.db import models


class Noti(models.Model):
    message = models.CharField(max_length=100)

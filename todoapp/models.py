from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    done = models.BooleanField(default=False)
    panic_time = models.DateTimeField(null=True)
    panic_description = models.TextField(null=True)

    def panic(self):
        if self.panic_time and timezone.now() >= self.panic_time:
            return self.panic_description
        return None

    def __str__(self):
        return self.title

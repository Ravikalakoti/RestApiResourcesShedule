from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class MyResource(models.Model):
    resource_name = models.CharField(max_length=100)
    shedule = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    details = models.TextField(max_length=100)
    def __str__(self):
        return self.resource_name



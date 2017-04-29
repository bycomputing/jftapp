# Create your models here.
from django.db import models
import datetime

class Page(models.Model):
    heading = models.CharField(max_length=80, unique_for_date='date')
    date = models.DateField()
    contents = models.TextField()

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['date']

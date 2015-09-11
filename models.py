# Create your models here.
from django.db import models

class JFTReading(models.Model):
    date = models.DateField(auto_now_add=True)
    tagname = models.CharField(max_length=30)
    contents = models.TextField()

    def __unicode__(self):
        return str(self.tagname)

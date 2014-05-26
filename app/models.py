from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()

    def __unicode__(self):
        return self.title


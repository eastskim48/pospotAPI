from django.db import models

# Create your models here.


class Taglist(models.Model):
    tag_name = models.CharField(max_length=200)
    num_tag = models.IntegerField(default=0)

from django.db import models

# Create your models here.


class Taglist(models.Model):
    tag_name = models.CharField(max_length=20,null=False)
    num_tag = models.IntegerField(default=0)
    imgurls = models.TextField(max_length=10000,null=True)

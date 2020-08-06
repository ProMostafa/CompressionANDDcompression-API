from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=255,blank=True,default="")
    size = models.IntegerField(blank=True,default=0.0)


    def __str__(self):
        return "Name: {} ,Size: {}".format(self.name,self.size)

from django.db import models

class City(models.Model):
    name = models.TextField(null=True)
    def __unicode__(self):
        return self.name

class Bin(models.Model):
    x_coordinate = models.FloatField(null=True)
    y_coordinate = models.FloatField(null=True)
    address = models.TextField(null=True)
    volume = models.IntegerField(null=True)
    cur_filling = models.IntegerField(null=True)
    city = models.ForeignKey(City, null=True)
    def __unicode__(self):
        return "Container"

class Sample(models.Model):
    bin = models.ForeignKey(Bin, null=True)
    date = models.DateField(null=True)
    volume_old = models.IntegerField(null=True)
    volume_new = models.IntegerField(null=True)
    def __unicode__(self):
        return "Sample"
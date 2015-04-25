from django.db import models

class City(models.Model):
    name = models.TextField(null=True)
    def __str__(self):
        return self.name

class Bin(models.Model):
    x_coordiante = models.FloatField(null=True)
    y_coordinate = models.FloatField(null=True)
    address = models.TextField(null=True)
    volume = models.IntegerField(null=True)
    city = models.ForeignKey(City, null=True)
    def __str__(self):
        return "Container with address " + self.address

class Sample(models.Model):
    bin = models.ForeignKey(Bin, null=True)
    date = models.DateField(null=True)
    volume_old = models.IntegerField(null=True)
    volume_new = models.IntegerField(null=True)
    def __str__(self):
        return "Sample of the container " + self.bin.address + ' ' + self.bin.date
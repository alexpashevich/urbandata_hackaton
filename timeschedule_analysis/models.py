from django.db import models

class City(models.Model):
    name = models.TextField()
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    def __str__():
        return self.name

class Bin(models.Model):
    x_coordiante = models.FloatField()
    y_coordinate = models.FloatField()
    address = models.TextField()
    volume = models.IntegerField()
    city = models.ForeignKey(City)
    def __str__():
        return "Container with address " + self.address

class Sample(models.Model):
    bin = models.ForeignKey(Bin)
    date = models.DateField()
    volume_old = models.IntegerField()
    volume_new = models.IntegerField()
    def __str__():
        return "Sample of the container " + self.bin.address + ' ' + self.bin.date

# class Choice(models.Model):
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
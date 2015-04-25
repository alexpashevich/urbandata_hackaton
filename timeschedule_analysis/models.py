from django.db import models

class City(models.Model):
    name = models.TextField()
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

class Bin(models.Model):
    x_coordiante = models.FloatField()
    y_coordinate = models.FloatField()
    address = models.TextField()
    volume = models.IntegerField()
    # city = models.ForeignKey(City)

class Sample(models.Model):
    bin = models.ForeignKey(Bin)
    date = models.DateField()
    volume_old = models.IntegerField()
    volume_new = models.IntegerField()

# class Choice(models.Model):
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
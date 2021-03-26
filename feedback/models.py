from django.db import models
# from django import forms


# Create your models here.
class Feedback(models.Model):

    name = models.CharField(max_length=200)
    competency = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=True)
    teachings_Skills = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=True)
    punctuality = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=True)
    practical_Knowlegde = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=True)
    approachability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=True)
    class_Control = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=True)

    def __str__(self):
        return self.name

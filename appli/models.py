from django.contrib.auth.models import User
from django.db import models

class Sondage(models.Model):
    titre = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    termine = models.BooleanField(null=True)

    def __str__(self):
        return self.titre


class Question(models.Model):
    intitule = models.CharField(max_length=255)
    sondage = models.ForeignKey(Sondage, on_delete=models.CASCADE)
    proposition1 = models.CharField(max_length=255)
    proposition2 = models.CharField(max_length=255)
    proposition3 = models.CharField(max_length=255, blank=True)
    proposition4 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.sondage.titre + ' : ' + self.intitule

class Reponse(models.Model):
    num_proposition = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.user.username + " -> " + self.question.sondage.titre + " : " + self.question.intitule + " : " + str(self.num_proposition)
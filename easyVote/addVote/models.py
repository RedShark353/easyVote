from django.db import models
from django.db.models.fields import IntegerField

#SuperUser: Creator/ poponelson@outlook.com / Super...1.
#Register every table at admin.py

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=64)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.votes} votes"

class Code(models.Model):
    code = models.CharField(max_length=6)
    used = models.BooleanField()

    def __str__(self):
        return f"{self.code}: {self.used} "
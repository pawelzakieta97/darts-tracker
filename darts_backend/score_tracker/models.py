from django.db import models


# Create your models here.
class Score(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    user_id = models.IntegerField()

    def __str__(self):
        return f'({self.x}, {self.y})'
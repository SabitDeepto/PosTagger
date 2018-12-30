from django.db import models


# admin can register merchant
class Word(models.Model):
    word = models.TextField()

    def __str__(self):
        return self.word


from django.db import models

# admin can register merchant
CHOICES = [
    ('Noun', 'Noun'),
    ('Pronoun', 'Pronoun'),
    ('Verb', 'Verb'),
    ('Others', 'Others'),

]


class Word(models.Model):
    word = models.TextField()
    pos = models.CharField(max_length=100, choices=CHOICES, blank=True)

    def __str__(self):
        return self.word

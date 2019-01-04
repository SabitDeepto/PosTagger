from django.db import models


class Sentence(models.Model):
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text


class Tag(models.Model):
    word = models.CharField(max_length=50)
    pos = models.CharField(max_length=50)
    sentence_id = models.ForeignKey(Sentence, on_delete=models.CASCADE)

    def __str__(self):
        return self.word



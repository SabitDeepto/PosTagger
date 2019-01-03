from django.db import models


# Create your models here.
class Pos(models.Model):
    id = models.IntegerField(primary_key=True)


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

from rest_framework import serializers

from PosRest.models import Sentence, Tag


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ('id', 'text')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'word', 'pos', 'sentence_id')

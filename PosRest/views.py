# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.request import Request
from rest_framework.response import Response

from PosRest.models import Sentence, Tag
from PosRest.serializers import SentenceSerializer, TagSerializer


# basic api test
@api_view(http_method_names=['GET', 'POST'])
def say_hello(request: Request):
    a = Sentence.objects.create(text=request.data['sentence'])
    a.save()
    for i in request.data['list_of_word']:
        for e in i['words']:
            b = Tag.objects.create(word=e['word'], pos=e['pos']['value'], sentence_id=a)
            b.save()

    return Response({
        'message': a.text
    })


@api_view(http_method_names=['POST'])
def save_words(request: Request):
    pass

#
# # serializer for Sentence Table
# class SentenceViewSet(viewsets.ModelViewSet):
#     queryset = Sentence.objects.all()
#     serializer_class = SentenceSerializer
#
#
# # serializer for Tag Table
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

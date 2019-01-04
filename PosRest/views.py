# Create your views here.
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from PosRest.models import Sentence, Tag
from PosRest.serializers import SentenceSerializer, TagSerializer


# basic api test
@api_view(http_method_names=['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def say_hello(request: Request):
    # a = Sentence.objects.create(text=request.data['sentence'])
    # a.save()
    # print(request.data)
    # for i in request.data['list_of_word']:
    #     for e in i['words']:
    #         b = Tag.objects.create(word=e['word'], pos=e['pos']['value'], sentence_id=a)
    #         b.save()

    return Response({
        'message': 'soft'
    })


@api_view(http_method_names=['GET', 'POST'])
def hello(request: Request):
    a = Sentence.objects.create(text=request.data['sentence'])
    a.save()
    for i in request.data['list_of_word']:
        b = Tag.objects.create(word=i['word'], pos=i['pos']['label'], sentence_id=a)
        b.save()
    response = JsonResponse(
        # your stuff here
        {'foo': request.data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS,POST"
    assert isinstance(response, object)
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response



# serializer for Sentence Table
class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


# serializer for Tag Table
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

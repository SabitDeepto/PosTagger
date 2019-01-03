
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from PosRest.views import say_hello, TagViewSet, SentenceViewSet

router = SimpleRouter()
router.register('sentence', SentenceViewSet, base_name='sentence')
router.register('tag', TagViewSet, base_name='tag')

urlpatterns = [
    path('save/', say_hello),
    path('', say_hello),
    path('', include(router.urls)),


]

from django.contrib import admin

# Register your models here.
from PosRest.models import Sentence, Tag

admin.site.register(Sentence)
admin.site.register(Tag)

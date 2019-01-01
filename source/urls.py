
from django.contrib import admin
from django.urls import path

from pos import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('test/', views.test, name='test'),

]

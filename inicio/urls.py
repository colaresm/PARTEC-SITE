
from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   url(r'$^',views.paginiainicial),
   url(r'^inicio/3.html', views.home, name='home'),
]

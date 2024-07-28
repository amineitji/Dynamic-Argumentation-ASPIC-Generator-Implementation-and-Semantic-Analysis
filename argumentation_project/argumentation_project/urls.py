# argumentation_project/urls.py

from django.contrib import admin
from django.urls import path
from aspic_generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

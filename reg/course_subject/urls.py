from django.urls import path

from . import views

app_name = "course_subject"
urlpatterns = [
    path('', views.index, name='index'),
    
]
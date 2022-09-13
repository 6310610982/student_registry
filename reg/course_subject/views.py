from django.shortcuts import render

from django.http import HttpResponse

from course_subject.models import Course
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    course = Course.objects.all()
    user_data = User.objects.filter(is_superuser=False)

    return render(request, 'course_subject/index.html',{
        'course_subject' : course,
        'user' : user_data
    })
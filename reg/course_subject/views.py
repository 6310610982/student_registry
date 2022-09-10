from django.shortcuts import render

from django.http import HttpResponse

from course_subject.models import Course

# Create your views here.

def index(request):
    course = Course.objects.all()
    return render(request, 'course_subject/index.html',{
        'course_subject' : course
    })
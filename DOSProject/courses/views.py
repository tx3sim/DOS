import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from courses.models import SemesterSubject


def maker(request):
    return render(request, 'pages/courses/../members/templates/pages/maker.html')


@csrf_exempt
def altCourse(request):
    if request.POST:
        course = request.POST
        courseName = course.get("course", "0")
        return JsonResponse(json.dumps(
            list(SemesterSubject.objects.filter(subject__module__course__name=courseName).values('subject__name')),
            cls=DjangoJSONEncoder), safe=False)


@csrf_exempt
def altClass(request):
    if request.POST:
        subject = request.POST
        subjectName = subject.get('subjectName', '0')
        return JsonResponse(json.dumps(
            list(SemesterSubject.objects.filter(subject__name=subjectName).values('time')),
            cls=DjangoJSONEncoder), safe=False)


@csrf_exempt
def getTimetable(request):
    module = request.POST
    moduleName = module.get("moduleName", "0")
    return JsonResponse(json.dumps(
        list(SemesterSubject.objects.filter(subject__module__name=moduleName).values('subject__name', 'time')),
        cls=DjangoJSONEncoder), safe=False)

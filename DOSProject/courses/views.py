from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from courses.models import SemesterSubject


def maker(request):
    return render(request, 'pages/maker.html')


@csrf_exempt
def altCourse(request):
    if request.POST:
        tmp = request.POST
        courseName = tmp.get("course", "0")
        return JsonResponse(
            serializers.serialize('json', SemesterSubject.objects.filter(subject__module__course=courseName)),
            safe=False)


@csrf_exempt
def altClass(request):
    if request.POST:
        tmp = request.POST
        subjectName = tmp.get('subjectName', '0')
        return JsonResponse(serializers.serialize('json', SemesterSubject.objects.filter(subject=subjectName)),
                            safe=False)


@csrf_exempt
def getTimetable(request):
    module = request.POST
    moduleName = module.get("moduleName", "0")
    return JsonResponse(
        serializers.serialize('json', SemesterSubject.objects.filter(subject__module__name=moduleName)),
        safe=False)

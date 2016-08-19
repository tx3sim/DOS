from django.core import serializers
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from timetable.models import *


def index(request):
    return render(request, 'pages/index.html')


@csrf_exempt
def payment_1(request):
    courseName = 'Starter'
    if request.POST:
        course = request.POST
        courseName = course.get("levelName", "0")
        return JsonResponse(serializers.serialize('json', Class.objects.filter(moduleName__level__name=courseName)),
                            safe=False)
    else:
        return render(request, 'pages/payment_1.html', {"courseName": courseName})


@csrf_exempt
def payment_2(request):
    if request.POST:
        targetClass = request.POST
        className = targetClass.get('className', '0')
        return JsonResponse(serializers.serialize('json', Class.objects.filter(className=className)), safe=False)

    else:
        return render(request, 'pages/payment_2.html')


@csrf_exempt
def getTimetable(request):
    module = request.POST
    moduleName = module.get("moduleName", "0")
    return JsonResponse(serializers.serialize('json', Class.objects.filter(moduleName=moduleName)), safe=False)


# @csrf_exempt
# def selected(request):
#     data = request.GET
#     courseName = data.get("targetCourseName", "0")
#     className = data.get("targetClassName", "0")
#     return render(request, 'pages/payment_1.html', {"courseName": courseName, "className": className})

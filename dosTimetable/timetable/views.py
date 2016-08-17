from django.core import serializers
import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from timetable.models import *


def index(request):
    return render(request, 'pages/index.html')


@csrf_exempt
def getTimetable(request):
    module = request.POST
    moduleName = module.get("moduleName", "0")
    return JsonResponse(
        serializers.serialize('json', Class.objects.filter(moduleName=moduleName)), safe=False)


@csrf_exempt
def getClass(request):
    level = request.POST
    levelName = level.get("levelName", "0")
    return JsonResponse(serializers.serialize('json', Class.objects.filter(moduleName__level__name=levelName)), safe=False)


@csrf_exempt
def getTime(request):
    targetClass = request.POST
    className = targetClass.get('className', '0')
    return JsonResponse(serializers.serialize('json', Class.objects.filter(className=className)), safe=False)

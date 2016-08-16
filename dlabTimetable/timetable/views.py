from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from timetable.models import Timetable, LevelModule


def index(request):
    return render(request, 'index.html')


def getTimetable(request):
    return JsonResponse(serializers.serialize('json', LevelModule.objects.all()), safe=False)
# 포스트로 어느 모듈인지 넘겨서 해당 모듈안에 있는 class 다 넘겨주고 시간표에 띄우면 끝
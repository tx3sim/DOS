from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from courses.models import SemesterSubject, Subject, Course, Module


@csrf_exempt
def payment_2(request):
    if request.POST:
        targetClass = request.POST
        className = targetClass.get('className', '0')
        return JsonResponse(serializers.serialize('json', SemesterSubject.objects.filter(subject=className)),
                            safe=False)

    else:
        return render(request, 'pages/register.html')


def apply_1(request):
    course = Course.objects.all().values('name')
    subject = Subject.objects.filter(module__course__name=request.GET.get('course')).values("name")
    if request.GET.get('time'):
        time = SemesterSubject.objects.filter(subject=request.GET.get('subject')).values("time")
    else:
        time = None
    return render(request, 'pages/apply_1.html',
                  {'course': course, 'courseName': request.GET.get('course'),
                   'subject': subject, 'subjectName': request.GET.get('subject'),
                   'time': time, 'timeValue': request.GET.get('time')
                   })

# class CreateApplyForm(FormView):
#     template_name = 'pages/apply_1.html'
#     # success_url = '/pages/payment_2.html'
#     form_class = ApplyForm
#
#     def get_form_kwargs(self):
#         kwargs = super(CreateApplyForm, self).get_form_kwargs()
#         tmp = self.request.GET
#         kwargs['subject_choices'] = Subject.objects.filter(module__course__name=tmp.get('course')).values_list("name",
#                                                                                                                flat=True)
#         kwargs['time_choices'] = SemesterSubject.objects.filter(subject=tmp.get('subject')).values_list("time",
#                                                                                                         flat=True)
#         return kwargs
#
#     def get_initial(self):
#         tmp = self.request.GET
#         initial = super(CreateApplyForm, self).get_initial()
#         initial['Course'] = tmp.get('course')
#         if tmp.get('subject'):
#             initial['Subject'] = tmp.get('subject')
#             initial['Time'] = tmp.get('time')
#         else:
#             initial['Subject'] = 0
#             initial['Time'] = 0
#
#         return initial

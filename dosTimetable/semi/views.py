from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from semi.forms import PaymentForm
from semi.models import *

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


@csrf_exempt
def altCourse(request):
    if request.POST:
        tmp = request.POST
        courseName = tmp.get("course", "0")
        return JsonResponse(serializers.serialize('json', SemesterClass.objects.filter(className__moduleName__course=courseName)),
                            safe=False)


@csrf_exempt
def altClass(request):
    if request.POST:
        tmp = request.POST
        className = tmp.get('className', '0')
        return JsonResponse(serializers.serialize('json', SemesterClass.objects.filter(className=className)), safe=False)


@csrf_exempt
def payment_2(request):
    if request.POST:
        targetClass = request.POST
        className = targetClass.get('className', '0')
        return JsonResponse(serializers.serialize('json', SemesterClass.objects.filter(className=className)), safe=False)

    else:
        return render(request, 'pages/payment_2.html')


@csrf_exempt
def getTimetable(request):
    module = request.POST
    moduleName = module.get("moduleName", "0")
    return JsonResponse(
        serializers.serialize('json', SemesterClass.objects.filter(className__moduleName=moduleName)),
        safe=False)


class CreatePaymentForm(FormView):
    template_name = 'pages/payment_1.html'
    #success_url = '/pages/payment_2.html'
    form_class = PaymentForm

    def get_form_kwargs(self):
        kwargs = super(CreatePaymentForm, self).get_form_kwargs()
        tmp = self.request.GET
        kwargs['class_choices'] = Classes.objects.filter(moduleName__course__name=tmp.get('course')).values_list("name", flat=True)
        kwargs['time_choices'] = SemesterClass.objects.filter(className=tmp.get('class')).values_list("time", flat=True)
        return kwargs

    def get_initial(self):
        tmp = self.request.GET
        initial = super(CreatePaymentForm, self).get_initial()
        initial['Course'] = tmp.get('course')
        if tmp.get('class'):
            initial['Class'] = tmp.get('class')
            initial['Time'] = tmp.get('time')
        else:
            initial['Class'] = 0
            initial['Time'] = 0

        return initial


# def signup(request):
#     signupform = SignupForm()
#     if request.method == "POST":
#         signupform = SignupForm(request.POST)
#         if signupform.is_valid():
#             user = signupform.save(commit=False)
#             user.email = signupform.cleaned_data['email']
#             user.save()
#
#             return HttpResponseRedirect(
#                 reverse("signup_ok")
#             )
#
#     return render(request, "pages/payment_2.html", {
#         "signupform": signupform,
#     })
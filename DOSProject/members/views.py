from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from courses.models import SemesterSubject, Subject, Course
from members.models import Member, ChildMember


@csrf_exempt
def apply_2(request):
    if request.POST:
        member = Member.objects.create_user(request.POST['email'],
                                            request.POST['memberName'],
                                            request.POST['phoneNumber'],
                                            request.POST['address'],
                                            request.POST['path'])
        member.set_password(request.POST['password1'])
        member.save()
        new_member = authenticate(email=request.POST['email'],
                                  password=request.POST['password1'], )
        login(request, new_member)
        child = ChildMember.objects.create(memberName=member, childName=request.POST['childName'],
                                           gender=request.POST['gender'], school=request.POST['school'],
                                           experience=request.POST['experience'], birthday=request.POST['birthday'])
        child.save()
        return JsonResponse({'course': request.POST['course'], 'subject': request.POST['subject'],
                             'time': request.POST['time'], 'childName': request.POST['childName']}, )

    else:
        tmp = request.GET
        return render(request, 'pages/register.html',
                      {'course': tmp.get('course'), 'subject': tmp.get('subject'), 'time': tmp.get('time')})


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
                   'time': time, 'timeValue': request.GET.get('time')})


def applyCheck(request):
    tmp = request.GET
    return render(request, 'pages/applyCheck.html',
                  {'member': request.user, 'course': tmp.get('course'), 'subject': tmp.get('subject'),
                   'time': tmp.get('time'), 'childName': tmp.get('childName')})


@csrf_exempt
def MemberLogin(request):
    print(request.POST)
    email = request.POST['email']
    password = request.POST['password']
    member = authenticate(email=email, password=password,)
    if member is not None:
        login(request, member)
        child = ChildMember.objects.filter(memberName__memberName=request.user.memberName).values_list('childName', flat=True)
        return JsonResponse({'course': request.POST['course'], 'subject': request.POST['subject'], 'time': request.POST['time'],
                             'childName': child[0]})
    else:
        return JsonResponse({'result': 'error'})


@csrf_exempt
def payment_result(request):
    tmp = request.GET
    return render(request, 'pages/payment_result.html', {'name': tmp.get('name')})

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

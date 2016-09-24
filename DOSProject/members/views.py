from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from courses.models import SemesterSubject, Subject, Course
from members.models import Member, ChildMember, ChildMemberSubject, Payment


def apply_1(request):
    course = Course.objects.all().values('name')
    subject = Subject.objects.filter(module__course__name=request.GET.get('course')).values("name")
    if request.GET.get('time'):
        time = SemesterSubject.objects.filter(subject__name=request.GET.get('subject')).values("time")
    else:
        time = None
    return render(request, 'pages/Apply//makerApply_1.html',
                  {'course': course, 'courseName': request.GET.get('course'),
                   'subject': subject, 'subjectName': request.GET.get('subject'),
                   'time': time, 'timeValue': request.GET.get('time')})


@csrf_exempt
def apply_2(request):
    if request.POST:
        if request.POST['path'] == '검색':
            path = request.POST['path'] + ' - ' + request.POST['keyword']
        else:
            path = request.POST['path']
        member = Member.objects.create_user(request.POST['email'],
                                            request.POST['memberName'],
                                            request.POST['phoneNumber'],
                                            request.POST['address'],
                                            path)
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
        return render(request, 'pages/Apply/makerApply_2.html',
                      {'course': tmp.get('course'), 'subject': tmp.get('subject'), 'time': tmp.get('time')})


@csrf_exempt
def apply_3_1(request):
    tmp = request.GET
    child = ChildMember.objects.filter(memberName__memberName=request.user.memberName).values('childName')
    return render(request, 'pages/Apply/makerApply_3_1.html',
                  {'member': request.user, 'course': tmp.get('course'), 'subject': tmp.get('subject'),
                   'time': tmp.get('time'), 'child': child, 'childName': child[0].get('childName')})


@csrf_exempt
def apply_3_1_1(request):
    tmp = request.GET
    if request.POST:
        child = ChildMember.objects.create(memberName=request.user, childName=request.POST['childName'],
                                           gender=request.POST['gender'], school=request.POST['school'],
                                           experience=request.POST['experience'], birthday=request.POST['birthday'])
        child.save()
        return JsonResponse({'subject': request.POST['subject'], 'time': request.POST['time']})
    else:
        return render(request, 'pages/Apply/makerApply_3_1_1.html', {'subject': tmp.get('subject'), 'time': tmp.get('time')})


@csrf_exempt
def apply_3_2(request):
    tmp = request.GET
    if request.POST:
        subject = SemesterSubject.objects.filter(subject__name=request.POST['subject'],
                                                 time=request.POST['time']).values_list(
            'subject__module__course__name', 'subject__name', 'time', 'semester__name')

        info = {'memberName': request.user.memberName, 'email': request.user.email,
                'phoneNumber': request.user.phoneNumber, 'address': request.user.address,
                'course': subject[0][0], 'subject': subject[0][1], 'time': subject[0][2], 'semester': subject[0][3]}
        return JsonResponse(info)
    else:
        child = ChildMember.objects.filter(memberName__memberName=request.user.memberName).values('childName')
        return render(request, 'pages/Apply/makerApply_3_2.html',
                      {'member': request.user, 'course': tmp.get('course'), 'subject': tmp.get('subject'),
                       'time': tmp.get('time'), 'child': child, 'childName': tmp.get('childName')})


@csrf_exempt
def MemberLogin(request):
    email = request.POST['email']
    password = request.POST['password']
    member = authenticate(email=email, password=password, )
    if member is not None:
        login(request, member)
        return JsonResponse(
            {'course': request.POST['course'], 'subject': request.POST['subject'], 'time': request.POST['time']})
    else:
        return JsonResponse({'result': 'error'})


@csrf_exempt
def payment_result(request):
    if request.POST:
        child = ChildMember.objects.get(memberName__memberName=request.user.memberName, childName=request.POST['childName'])
        subject = SemesterSubject.objects.get(subject__name=request.POST['subject'], time=request.POST['time'])
        childMemberSubject = ChildMemberSubject.objects.create(childName=child, subject=subject)
        payment = Payment.objects.create(memberName=request.user)
        childMemberSubject.save()
        payment.save()
        return JsonResponse({'result': 'success'})
    else:
        tmp = request.GET
        return render(request, 'pages/Apply/payment_result.html',
                      {'name': tmp.get('name'), 'applyNum': tmp.get('applyNum'), 'amount': tmp.get('amount'),
                       'childName': tmp.get('childName')})

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

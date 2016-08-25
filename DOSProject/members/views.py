from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from courses.models import SemesterSubject, Subject, Course, Module

# def register(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST, prefix='user')
#         upf = UserProfileForm(request.POST, prefix='userprofile')
#         if uf.is_valid() * upf.is_valid():
#             user = uf.save()
#             userprofile = upf.save(commit=False)
#             userprofile.user = user
#             userprofile.save()
#             return django.http.HttpResponseRedirect(…something…)
from members.admin import UserCreationForm

# ser = User.objects.create_user(form.cleaned_data['username'],
#                                form.cleaned_data['email'],
#                                form.cleaned_data['password1'])
# profile = Profile(user=user, gender=form.cleaned_data['gender'])
# profile.save()
# if form.cleaned_data['gender'] == "MAN":
#     user.groups.add(name='강남')
# else:
#     user.groups.add(name="판교")
# user.save()
from members.models import Member, ChildMember


def apply_2_1(request):
    if request.POST:
        member = Member.objects.create_user(request.POST['email'],
                                            request.POST['memberName'],
                                            request.POST['phoneNumber'],
                                            request.POST['password1'])
        member.save()
        child = ChildMember.objects.create(memberName=member, childName=request.POST['childName'],
                                           gender=request.POST['gender'], school=request.POST['school'],
                                           experience=request.POST['experience'], birthday=request.POST['birthday'])
        child.save()
        print(request.GET)
        return HttpResponseRedirect('/apply_2_2')

    else:
        tmp = request.GET
        return render(request, 'pages/register.html', {'course': tmp.get('course'), 'subject': tmp.get('subject'), 'time': tmp.get('time')})


def apply_2_2(request):
    print(request.POST)
    return render(request, 'pages/appplyCheck.html', {'course': request.GET.get('course'), 'subject': request.GET.get('subject')})


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


def payment_result(request):
    return render(request, 'pages/payment_result.html')
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

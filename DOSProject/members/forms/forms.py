from django import forms
from django.forms import ModelForm

from courses.models import Course, SemesterSubject
from members.models import Member, ChildMember


# class MemberForm(ModelForm):
#     class Meta:
#         model = Member
#
#
# class ChildMemberForm(ModelForm):
#     class Meta:
#         model = ChildMember
#         exclude = ['memberName']

# class ApplyForm(forms.ModelForm):
#     class Meta:
#         model = SemesterSubject
#         fields = ('Course', 'Subject', 'Time')
#
#     Course = forms.ModelChoiceField(
#         queryset=Course.objects.all()
#     )
#     Subject = forms.ModelChoiceField(
#         queryset=None
#     )
#     Time = forms.ModelChoiceField(
#         queryset=None
#     )
#
#     def __init__(self, subject_choices, time_choices, *args, **kwargs):
#         super(ApplyForm, self).__init__(*args, **kwargs)
#         if subject_choices is not None:
#             self.fields['Subject'].queryset = subject_choices
#         if time_choices is not None:
#             self.fields['Time'].queryset = time_choices


# class MemberCreationForm(forms.ModelForm):
#
#     email = forms.EmailField(label="E-mail")
#     username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, label='Username')
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
#     password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password")
#     # GENDER_CHOICES = (('M', 'Man'), ('W', 'Women'))
#     # gender = forms.TypedChoiceField(
#     #     choices=GENDER_CHOICES, widget=forms.RadioSelect,
#     # )
#
#     class Meta:
#         model = Member
#         fields = ('email', 'username', 'password1', 'password2')
#
#     def clean_username(self):
#         try:
#             user = User.objects.get(username__iexact=self.cleaned_data['username'])
#         except User.DoesNotExist:
#             return self.cleaned_data['username']
#         raise forms.ValidationError("Username already exists")
#
#     def clean(self):
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError("Password not match")
#             return self.cleaned_data


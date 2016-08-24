from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.images import get_image_dimensions

from semi.models import *


class PaymentForm(forms.ModelForm):
    class Meta:
        model = UserClass
        fields = ('Course', 'Class', 'Time')

    Course = forms.ModelChoiceField(
        queryset=Course.objects.all()
    )
    Class = forms.ModelChoiceField(
        queryset=None
    )
    Time = forms.ModelChoiceField(
        queryset=None
    )

    def __init__(self, class_choices, time_choices, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        if class_choices is not None:
            self.fields['Class'].queryset = class_choices
        if time_choices is not None:
            self.fields['Time'].queryset = time_choices


# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Email',
#             'required': 'True',
#         }
#     ))
#     username = forms.RegexField(label="username", max_length=30,
#                                 regex=r'^[\w.@+-]+$',
#                                 help_text="Required. 30 characters or fewer. Letters, digits and "
#                                           "@/./+/-/_ only.",
#                                 error_messages={
#                                     'invalid': "This value may contain only letters, numbers and "
#                                                "@/./+/-/_ characters."},
#                                 widget=forms.TextInput(attrs={
#                                     'class': 'form-control',
#                                     'placeholder': 'Username',
#                                     'required': 'true',
#                                 }))
#     password1 = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password',
#                 'required': 'True',
#             }
#         )
#     )
#     password2 = forms.CharField(
#         label="Password confirmation",
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password confirmation',
#                 'required': 'True',
#             }
#         ),
#         help_text="Enter the same password as above, for verification."
#     )
#
#     class Meta:  # SignupForm에 대한 기술서
#         model = MyUser
#         fields = ("email", "username", "password1", "password2",)  # 작성한 필드만큼 화면에 보여짐
#
#
# class LoginForm(AuthenticationForm):
#     email = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'username',
#                 'required': 'True',
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password',
#                 'required': 'True',
#             }
#         )
#     )

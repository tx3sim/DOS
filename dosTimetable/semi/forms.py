from django.contrib.auth.models import User
from django import forms

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


    # GENDER_CHOICES = (('M', 'Man'), ('W', 'Women'))
    # gender = forms.TypedChoiceField(
    #     choices=GENDER_CHOICES, widget=forms.RadioSelect,
    # )

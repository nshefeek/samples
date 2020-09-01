from django import forms
from django.contrib.auth.models import ReadOnlyPasswordHashField

from .models import Employee

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Employee
        fields = (
                'name',
                'email',
                'mobile',
                'password',
                'date_of_birth',
                'department',
                'designation',
                'organization',
                'reporting_to',
                'photograph'
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



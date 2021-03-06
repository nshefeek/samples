from django import forms
#from django.contrib.auth.models import ReadOnlyPasswordHashField

from .models import Employee

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = Employee
        fields = (
                'name',
                'email',
                'mobile',
                'date_of_birth',
                'department',
                'designation',
                'organization',
                'reporting_to',
                'photograph',
            )

    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.clean_password())
        if commit:
            user.save()
        return user



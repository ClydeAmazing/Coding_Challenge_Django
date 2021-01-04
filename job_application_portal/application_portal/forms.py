from django import forms
from django.core.validators import EMPTY_VALUES
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import applicant_details, application_attachment, applicant_education

# Account registration form
# Subclassed from UserCreationForm to make use of built-in user creation form validations
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name'
        }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
        }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
        }))

    # Adds form-control(bootstrap class) and custom my-input attributes to each field.
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-input'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# Account login form
# Subclassed from AuthenticationForm to make use of built-in user creation form validations
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control my-input',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control my-input',
        'placeholder': 'Password'
    }))

# Applicant Details form
class ApplicantDetailsForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    nationality = forms.CharField(widget=forms.widgets.TextInput(attrs={'list': 'data_nationalities'}))
    country = forms.CharField(widget=forms.widgets.TextInput(attrs={'list': 'data_countries'}))
    city = forms.CharField(widget=forms.widgets.TextInput(attrs={'list': 'data_cities'}))

    # Adds form-control(bootstrap class) and custom my-input attributes to each field.
    def __init__(self, *args, **kwargs):
        super(ApplicantDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-input'

    class Meta:
        model = applicant_details  
        exclude = ['user']

    def clean(self):
        status = self.cleaned_data.get('marital_status')
        dependents = self.cleaned_data.get('dependents')
        if status == 'Married' and dependents in EMPTY_VALUES:
            self._errors['dependents'] = self.error_class(['This field is required.'])

        return self.cleaned_data

class AttachmentsForm(forms.ModelForm):
    attachment_file = forms.FileField(widget=forms.ClearableFileInput())
        
    class Meta:
        model = application_attachment
        fields = ['attachment_file']

class EducationForm(forms.ModelForm):

    degree = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-sm',
    }))
    university = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-sm',
    }))
    gpa = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-sm',
    }))
        
    class Meta:
        model = applicant_education
        fields = ['degree', 'university', 'gpa']
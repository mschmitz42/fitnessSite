from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           label="Name",
                           error_messages={"required": "Please enter your name"})
    contactInfo = forms.CharField(required=True,
                                  label="Contact Info (Phone or Email)",
                                  error_messages={"required": "Please enter your Contact Information"})
    message = forms.CharField(widget=forms.Textarea,
                              label="Message",
                              error_messages={"required": "Please enter a message"})


class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, label="Input File")


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=75, required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname']
        required = ['nickname']



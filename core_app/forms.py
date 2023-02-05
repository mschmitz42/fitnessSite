from django import forms


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
    file = forms.FileField(required=True, label="Measurements File")



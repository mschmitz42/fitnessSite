import requests
from django.shortcuts import render, redirect
from .forms import ContactForm, UploadFileForm
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
from sms import send_sms
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from .models import Profile
from .serializers import ProfileSerializer
from .file_upload import handle_measurement_file_import, handle_macro_file_import
from django.contrib.auth.decorators import login_required, user_passes_test
import logging


logger = logging.getLogger(__name__)


def user_is_staff(user):
    return user.is_staff


def core_app_index(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                "name": form.cleaned_data["name"],
                "contact_info": form.cleaned_data["contactInfo"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            send_sms(message, None, [+14154701060,+15309791020])
            # try:
            #     send_mail("Message From DHF Website",
            #               message,
            #               "webmaster@derek-haff-fitness.com",
            #               ["derek.haff@yahoo.com"])
            # except BadHeaderError:
            #     return HttpResponse("Invalid Header Found")
            return redirect("core_app:home")

    return render(request, 'core_app/index.html', {"form": form})


@login_required
def core_app_menu(request):
    return render(request, 'core_app/menu.html')


def core_app_under_construction(request):
    return render(request, 'core_app/under_construction.html')


@login_required
def core_app_profile(request):
    return render(request, 'core_app/profile.html')


@login_required
@user_passes_test(user_is_staff)
def core_app_client(request):
    return render(request, 'core_app/client.html')


@login_required
def core_app_measurement_file_upload(request):
    if request.method == 'GET':
        form = UploadFileForm()
        title = "Upload Measurement File"
        return render(request, 'core_app/file_upload.html', {'form': form, 'title': title})

    try:
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_measurement_file_import(request.user, 'weight', request.FILES['file'])
        else:
            logger.debug(form.errors.as_data())

    except Exception as e:
        logger.error("Unable to upload file:" + repr(e))

    return render(request, 'core_app/profile.html')


@login_required
def core_app_macro_file_upload(request):
    if request.method == 'GET':
        form = UploadFileForm()
        title = "Upload Macro File"
        return render(request, 'core_app/file_upload.html', {'form': form, 'title': title})

    try:
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_macro_file_import(request.user, request.FILES['file'])
        else:
            logger.debug(form.errors.as_data())

    except Exception as e:
        logger.error("Unable to upload file:" + repr(e))

    return render(request, 'core_app/profile.html')


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            qs = Profile.objects.all()
        else:
            qs = Profile.objects.filter(user=self.request.user)

        return qs




from django.shortcuts import render, redirect
from .forms import ContactForm
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
from sms import send_sms


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


def core_app_dashboard(request):
    return render(request, 'core_app/dashboard.html')


def core_app_under_construction(request):
    return render(request, 'core_app/under_construction.html')

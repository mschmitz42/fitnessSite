from django.shortcuts import render


def coreApp_index(request):
    return render(request, 'coreApp/index.html')



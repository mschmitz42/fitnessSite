from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)


def analyzer_index(request):
    return render(request, 'analyzer/index.html')

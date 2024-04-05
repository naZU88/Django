from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)


# Create your views here.
from django.http import HttpResponse

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("This is the main page.")

def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")
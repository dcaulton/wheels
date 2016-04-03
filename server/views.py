from django.core.urlresolvers import reverse
from django.http import HttpResponse

import json

def index(request):
    return HttpResponse('server index')

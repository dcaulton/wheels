from django.core.urlresolvers import reverse
from django.http import HttpResponse

import json

def index(request):
    return HttpResponse(json.dumps('lidar index'), content_type='application/json')

# Create your views here.
def get_reading(request):
    return HttpResponse('getting a reading')

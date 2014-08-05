from django.shortcuts import render_to_response

from django.template import RequestContext
from home.forms import ConfigForm
from home.models import BaseWebConfig
# Create your views here.


def index(request):
    """
    """
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ConfigForm()

    return render_to_response('index.html', {'form':form}, RequestContext(request))

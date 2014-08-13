#coding:utf-8
from django.shortcuts import render_to_response
from .models import MpttMeetInfo,Owner

# Create your views here.
def show_info(request):
	owner = Owner.objects.all()[0]
	return render_to_response("test.html",{'meetInfo':owner.meetInfo,"test":"test"})

############################################
from .models import Meet
##test ajax
#写restful风格的接口
#ajax不需要考虑csrf的问题，session request里会携带
#url来定位,id
from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#can use #require login?
@csrf_exempt
def edit_meet_info(request,id):
    yourid =int(id)
    username = request.POST.get('username', '')
    #meet = Meet.objests.get(id=int(yourid))
    #print username
    data = {"yourdata": username,"id":yourid}
    response = simplejson.dumps(data)
    return HttpResponse(response)

def test_ajax(request):
	return render_to_response("test_ajax.html",{})

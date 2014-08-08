from django.shortcuts import render_to_response
from .models import MpttMeetInfo,Owner
# Create your views here.
def show_info(request):
	owner = Owner.objects.all()[0]
	return render_to_response("test.html",{'meetInfo':owner.meetInfo,"test":"test"})
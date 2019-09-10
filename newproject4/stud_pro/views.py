from django.shortcuts import render,redirect

from stud_pro.forms import teacherform 
from stud_pro.models import *

def show(request):
	teachers = Teacher.objects.raw('SELECT * FROM stud_pro_teacher')
	return render(request,"show.html",{'teachers':teachers})
# Create your views here.
def dashboard(request):
	print(request.session['login_id'])
	if ("loginid" in request.session):
		if ("student" in request.session):
			return render(request,"student.html")
	else:
		return render(request,"login.html")

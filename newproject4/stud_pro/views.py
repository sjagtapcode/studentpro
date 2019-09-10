from django.shortcuts import render,redirect

from stud_pro.forms import teacherform 
from stud_pro.models import *

def show(request):
	teachers = Teacher.objects.raw('SELECT * FROM stud_pro_teacher')
	return render(request,"show.html",{'teachers':teachers})
# Create your views here.
def dashboard(request):
	if ("session_on" in request.session):
		if ("student" in request.session):
			return render(request,"student.html")
	#else if (request.method == "GET"):
	#	return render(request,"login.html")
	elif (request.method == "POST"):
		login_id=request.POST['login_id']
		password=request.POST['password']
		print(login_id)
		if (request.POST['type'] == "student"):
			return render(request,"student.html")
		elif (request.POST['type'] == "parent"):
			return render(request,"parent.html")
		else:
			return render(request,"login.html")

	else:
		return render(request,"login.html")

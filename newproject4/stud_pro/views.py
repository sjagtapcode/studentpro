from django.shortcuts import render,redirect

from stud_pro.forms import teacherform,studentform,parentform 
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

def  admin_teacher(request):
	if request.method == "POST" :
		form = teacherform(request.POST)
		if form.is_valid():
			try :
				print(form.cleaned_data["teacher_name"])
				form.save()
				#return redirect("/show")
				messages.success(request, 'Form submission successful')
			except :
				pass
	else :
		form = teacherform()
	return render(request,"admin_add_teacher.html",{'form':form})	

def  admin_student(request):
	if request.method == "POST" :
		form = studentform(request.POST)
#		if form.is_valid():
		try :
			print("sdjo")
			print(form.cleaned_data["cats"])
			form.save()
			#return redirect("/show")
			messages.success(request, 'Form submission successful')
		except :
			pass
	else :
		form = studentform()
	return render(request,"admin_add_student.html",{'form':form})		

def  admin_parent(request):
	if request.method == "POST" :
		form = parentform(request.POST)
		if form.is_valid():
			try :
				form.save()
				#return redirect("/show")
				messages.success(request, 'Form submission successful')
			except :
				pass
	else :
		form = parentform()
	return render(request,"admin_add_parent.html",{'form':form})


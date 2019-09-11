from django.shortcuts import render,redirect

from stud_pro.forms import teacherform,studentform,parentform 
from stud_pro.models import *

def show(request):
	teachers = Teacher.objects.all()
	return render(request,"show.html",{'teachers':teachers})
# Create your views here.
def login(request):
	if ("session_on" in request.session):
		if (request.session["session_on"]=="student"):
			#print(request.session["login_id"])
			return redirect("/student/")
		elif (request.session["session_on"]=="parent"):
			return redirect("/parent/")


	elif (request.method == "GET"):
		return render(request,"login/login.html")

	elif (request.method == "POST"):
		current_login_id=request.POST['login_id']
		print(current_login_id)
		password=request.POST['password']
		if (request.POST['type'] == "student"):
			request.session['session_on']="student"
			if (current_login_id=="admin"):		#check in database
				request.session['login_id']=current_login_id
				print("first login")
				return redirect("/student/")
		elif (request.POST['type'] == "parent"):
			request.session['session_on']="parent"
			if(current_login_id=="papa"):
				request.session['login_id']=current_login_id
				return redirect("/parent/")
	#request.session["invalid"]=login_id
	return render(request,"login/login.html")


def parent(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="parent"):
			login_id=request.session['login_id']
			
			# (to-do) parent dashboard
			return render(request,"parent/parent.html")
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")



def student(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="student"):
			login_id=request.session['login_id']

			### (to-do) student dashboard here
			return render(request,"student/student.html")
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")


def admin(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="admin"):
			login_id=request.session['login_id']

			# (to-do) admin dashboard
			return render(request,"admin/admin.html")
		else:
			request.session.clear()
			return redirect("/invalid/")
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
#	return redirect("/login/")


def logout(request):
	if("session_on" in request.session):	#deleate everything in the session
		request.session.clear()
	return redirect("/login/")
#>>>>>>> fc8de6a5be9c837a2ec3e90f2f1dc70e16f945ef


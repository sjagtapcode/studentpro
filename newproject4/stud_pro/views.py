from django.shortcuts import render,redirect

from stud_pro.forms import teacherform,studentform,parentform,subjectform,subject_teacherform
from stud_pro.models import *
from django.db.models import CharField, Value


def show_teacher(request):
	teachers=Teacher.objects.all()
	return render(request,"admin/show_teacher.html",{'teachers':teachers})

def admin_dept(request):
	dept=Department.objects.all()
	return render(request,"admin/admin_dept.html",{"dept":dept})

def admin_class(request,id):
	#print(id)
	Cl=Class.objects.filter(dept_id__exact=id)
	#print(Cl)
	return render(request,"admin/admin_class.html",{"Cl":Cl})

def admin_class_teacher(request,id):
	Cl=Class_Teacher.objects.filter(class_id_id__exact=id)
	hol=[]
	for i in range(len(Cl)):
		print(str(Cl[i].sr_no))
		sr=Teacher_Subject.objects.filter(sr_no__exact=str(Cl[i].sr_no))
		hol.append(sr)
	#print("sda")
	#print(hol)
	return render(request,"admin/admin_teacher_subject.html",{"sr":hol})

def teacher_subject(request):
	subject=Teacher_Subject.objects.all()
	return render(request,"admin/teacher_subject.html",{'subject':subject})

def  admin_teacher_subject(request):
	if request.method == "POST" :
		form = subject_teacherform(request.POST)
		if form.is_valid():
			try :
				#print(form.cleaned_data["teacher_name"])
				form.save()
				return redirect("/teacher_subject")
			except :
				pass
	else :
		form = subject_teacherform()
	return render(request,"admin/admin_add_teacher_subject.html",{'form':form})		

#select t.teacher_id_id,t.sub_id_id from stud_pro_teacher_subject t join stud_pro_subject s on (t.sub_id_id=s.sub_id)where s.dept_id_id=101;
#Above query select teacher and subjects according department

#def desplay_dept_wise_teacher_sub(request)
	

def  admin_teacher(request):
	if request.method == "POST" :
		form = teacherform(request.POST)
		if form.is_valid():
			try :
				#print(form.cleaned_data["teacher_name"])
				form.save()
				return redirect("/show_teacher")
			except :
				pass
	else :
		form = teacherform()
	return render(request,"admin/admin_add_teacher.html",{'form':form})		



def edit_teacher(request,id):
	teacher=Teacher.objects.get(teacher_id=id)
	return render(request,"admin/edit_teacher.html",{'teacher':teacher})

def update_teacher(request,id):
	teacher = Teacher.objects.get(teacher_id=id)
	form=teacherform(request.POST,instance=teacher)
	
	#[to-do update does not work update]

	if form.is_valid():

		form.save()
		return redirect('/show_teacher')
	return render(request,"admin/edit_teacher.html",{'teacher':teacher})

def delete_teacher(request,id):
	teacher=Teacher.objects.get(teacher_id=id)
	teacher.delete()
	return redirect('/show_teacher')



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

			# (to-do) student dashboard here
			return render(request,"student/student.html")
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")

def teacher(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="teacher"):
			login_id=request.session['login_id']

			# (to-do) teacher dashboard here
			return render(request,"teacher/teacher.html")
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
		return redirect("/login/")




def  admin_student(request):
	if request.method == "POST" :
		form = studentform(request.POST)
#		if form.is_valid():
		try :
			print("sdjo")
			print(form.cleaned_data["cats"])
			form.save()
			#return redirect("/show")
		except :
			pass
	else :
		form = studentform()
	return render(request,"admin/admin_add_student.html",{'form':form})		

def  admin_parent(request):
	if request.method == "POST" :
		form = parentform(request.POST)
		if form.is_valid():
			try :
				form.save()
				#return redirect("/show")
			except :
				pass
	else :
		form = parentform()
	return render(request,"admin/admin_add_parent.html",{'form':form})
#	return redirect("/login/")


def logout(request):
	if("session_on" in request.session):	#deleate everything in the session
		request.session.clear()
	return redirect("/login/")






"""

def teacher(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="teacher"):
			current_login_id=request.session['login_id']			
			teacher_det=Teacher.objects.filter(teacher_id__exact=current_login_id)
			teachers = Teacher_Subject.objects.filter(teacher_id__exact=current_login_id)
			classt = Class_Teacher.objects.filter(sr_no__in= teachers)
			classlist=[]
			classnamelist=[]
			clist=[]
			xx=0

			for i in range(0,len(classt)):
				xx=classt[i].class_id
				yy=Class.objects.filter(class_name__exact = xx)
				classnamelist.append(yy[0].class_id)
				classlist.append(yy)

		#	class_nm = Class.objects.filter(class_name__in = classt) 

			del teacher_det[0].password
			return render(request,"teacher/teacher.html", { "teacher_det" : teacher_det , "classlist" : classlist , "teacher_subject" : teachers , "classnamelist" : classnamelist})
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")











<!DOCTYPE html>
{% extends "home.html" %}
{% block head_title %}
	Teacher dashboard
{% endblock%}
{% block body_block %}
	<h2>THIS is teacher dashboard</h2>
	<h4>

	{% for t in teacher_det %}
		<br>id = {{t.teacher_id}}
		<br>name = {{t.teacher_name}}
		<br>email = {{t.email}}
	{% endfor %}
	<br>
	<h4>
	{% for c in classnamelist %}
		<br>
		<a href="/teacher/{{c}}" class="btn btn-info">{{ c }}</a>>
	{% endfor %}
	</h4>

{% endblock %}

{% block nav6%}
	<a href="#">teacher</a>
{% endblock %}
"""
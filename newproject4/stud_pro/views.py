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


def show_teacher(request):
	teachers=Teacher.objects.all()
	return render(request,"admin/show_teacher.html",{'teachers':teachers})

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


def class_combo(request):
	class_com = Class.objects.all()
	return render(request,"admin_add_student.html",{'class_com':class_com})

def student_profile(request):
	details = Student.objects.all()
	print(details)
	return render(request,"student/student_profile.html",{'details':details})

def teacher_classes(request):
	current_login_id=request.session['login_id']
	teachers = Teacher_Subject.objects.filter(teacher_id__exact=current_login_id)
	classt = Class_Teacher.objects.filter(sr_no__in= teachers)
	class_nm = Class.objects.filter(class_id__in = classt)
	#stud_nm = Student.objects.filter(class_id_id__in = class_nm)
	return render(request,"teacher/teacher_classes.html",{'class_nm':class_nm})

def teacher_students(request,class_id):
	#current_login_id=request.session['login_id']
	stud_from_cls = Student.objects.filter(class_id__exact=class_id)
	#classt = Class_Teacher.objects.filter(sr_no__in= teachers)
	#class_nm = Class.objects.filter(class_id__in = classt)
	#stud_nm = Student.objects.filter(class_id_id__in = class_nm)
	parent_ids = Student.objects.filter(class_id__exact=class_id).values("parent_id")
	print(parent_ids)
	return render(request,"teacher/teacher_students.html",{'stud_from_cls':stud_from_cls})	
# Create your views here.
def login(request):
	if ("session_on" in request.session):
		if (request.session["session_on"]=="student"):
			#print(request.session["login_id"])
			return redirect("/student/")
		elif (request.session["session_on"]=="parent"):
			return redirect("/parent/")
		elif (request.session["session_on"]=="teacher"):
			return redirect("/teacher/")
		elif (request.session["session_on"]=="admin"):
			return redirect("/admin/")


	elif (request.method == "GET"):
		return render(request,"login/login.html")

	elif (request.method == "POST"):
		current_login_id=request.POST['login_id']
		password=request.POST['pass_word']
		if (request.POST['type'] == "student"):
			request.session['session_on']="student"
			if (Student.objects.filter(student_id = current_login_id).exists() ):		#check in database
				request.session['login_id']=current_login_id
				student_det=Student.objects.filter(student_id__exact=current_login_id)
				if(password==student_det[0].password):
					del student_det[0].password 										#check password
					return render(request,"student/student.html",{'student_det':student_det})
				else :
					request.session.clear()
					context = { 'invalid' : "invalid password " }
					return render(request,"login/login.html",context)
			else :
				request.session.clear()
				context1 = { 'invalid_id' : "invalid id " }
				return render(request,"login/login.html",context1)		
     
		elif (request.POST['type'] == "parent"):
			request.session['session_on']="parent"
			if (Parent.objects.filter(parent_id = current_login_id).exists() ):
				request.session['login_id']=current_login_id
				parent_det=Parent.objects.filter(parent_id__exact=current_login_id)
				if(password==parent_det[0].password):
					del parent_det[0].password
					return render(request,"parent/parent.html",{'parent_det':parent_det})
				else :
					request.session.clear()
					context = { 'invalid' : "invalid password " }
					return render(request,"login/login.html",context)
			else :
				request.session.clear()
				context1 = { 'invalid_id' : "invalid id " }
				return render(request,"login/login.html",context1)	

		elif(request.POST['type'] == "teacher"):
			request.session['session_on']="teacher"
			if (Teacher.objects.filter(teacher_id = current_login_id).exists() ):
				request.session['login_id']=current_login_id
				teacher_det=Teacher.objects.filter(teacher_id__exact=current_login_id)
				if(password==teacher_det[0].password):
					del teacher_det[0].password
					#return render(request,"teacher/teacher.html",{'teacher_det':teacher_det})
					return redirect("/teacher/")
				else :
					request.session.clear()
					context = { 'invalid' : "invalid password " }
					return render(request,"login/login.html",context)
			else :
				request.session.clear()
				context1 = { 'invalid_id' : "invalid id " }
				return render(request,"login/login.html",context1)	

		elif(request.POST['type'] == "admin"):
			request.session['session_on']="admin"
			if (request.session['login_id']=="rootx"):
				if(password=="pict123"):
					return redirect("/admin/")
				else :
					request.session.clear()
					context = { 'invalid' : "invalid password " }
					return render(request,"login/login.html",context)
			else :
				request.session.clear()
				context1 = { 'invalid_id' : "invalid id " }
				return render(request,"login/login.html",context1)	
	request.session.clear()
	return render(request,"login/login.html")


def parent(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="parent"):
			current_login_id=request.session['login_id']
			
			# (to-do) parent dashboard
			return render(request,"parent/parent.html",{"login_id":current_login_id})
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")



def student(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="student"):
			current_login_id=request.session['login_id']

			# (to-do) student dashboard here
			return render(request,"student/student.html",{"login_id":current_login_id})
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")



def teacher(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="teacher"):
			current_login_id=request.session['login_id']
			teacher_det=Teacher.objects.filter(teacher_id__exact=current_login_id)
			teachers = Teacher_Subject.objects.filter(teacher_id__exact=current_login_id)
			classt = Class_Teacher.objects.filter(sr_no__in= teachers)
			classlist=[]
			classnamelist=[]
			subjectnamelist=[]
			clist=[]
			var1=0
			#can be optimized
			for i in range(0,len(classt)):
				var1=classt[i].class_id
				var2=Class.objects.filter(class_name__exact = var1)
				varr=str(var2[0].class_id)#+"-"+str(teachers[i].sub_id)
				classnamelist.append(varr)
				classlist.append(var2[0].class_id)
				var3=classt[i].sr_no
				subjectnamelist.append(str(teacher[i].sub_id))
			#	var4=Teacher_Subject.objects.filter(sr_no__exact = var3)
			#	var5=var4[0].sub_id
			#	subjectnamelist.append(var5)

			#class_nm = Class.objects.filter(class_name__in = classt) 

			del teacher_det[0].password
			return render(request,"teacher/teacher.html", { "teacher_det" : teacher_det , "classlist" : classlist , "teacher_subject" : teachers , "classnamelist" : classnamelist,"login_id":current_login_id})
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")


def admin(request):
	if("session_on" in request.session):
		if(request.session["session_on"]=="admin"):
			current_login_id=request.session['login_id']

			# (to-do) admin dashboard
			return render(request,"admin/admin.html",{"login_id":current_login_id})
		else:
			request.session.clear()
			return redirect("/invalid/")
	else:
		return redirect("/login/")


"""def  admin_teacher(request):
	if request.method == "POST" :
		form = teacherform(request.POST)
		if form.is_valid():
			try :
				print(form.cleaned_data["teacher_name"])
				form.save()
				#return redirect("/show")
			except :
				pass
	else :
		form = teacherform()
	return render(request,"admin/admin_add_teacher.html",{'form':form})"""	

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
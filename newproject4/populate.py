import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newproject4.settings')

import django
django.setup()

##fake pop

import random
from stud_pro.models import Department,Subject,Teacher,Teacher_Subject,Class,Parent,Student
from faker import Faker

fakegen = Faker()

"""
pids=[]
def popolu(n):
	for entry in range(n):
		fk_name=fakegen.name()
		fk_email=fakegen.email()
		fk_id=random.randint(1,10000)
		
		papa = Parent.objects.get_or_create(name=fk_name,email=fk_email,pid=fk_id)[0]
		pids.append(papa)
		
	for i in pids:
		for j in range(random.randint(1,2)):
			fk_id=i
			fk_sname=fakegen.name()
			fk_sid=random.randint(10000,90000)
			fk_marks=random.randint(0,100)
			bachcha = student.objects.get_or_create(name=fk_sname,marks=fk_marks,sid=fk_sid,pid=fk_id)[0]
"""
sdepartment=[]
ssubject=[]
steacher=[]
ssubjectteacher=[]
ssno=[]
sclass=[]
sParent=[]
sStudent=[]

def pdepartment(n):
	did = 1
	name = "Information Technology"
	HOD = fakegen.name()
	strength = 160
	dpt=Department.objects.get_or_create(dept_id=did,dept_name=name,dept_HOD=HOD,dept_strength=strength)
	sdepartment.append(dpt)
	did = 2
	name = "Computer Science"
	HOD = fakegen.name()
	strength = 320
	dpt = Department.objects.get_or_create(dept_id=did,dept_name=name,dept_HOD=HOD,dept_strength=strength)
	sdepartment.append(dpt)
	did = 3
	name = "Electronics"
	HOD = fakegen.name()
	strength = 360
	dpt = Department.objects.get_or_create(dept_id=did,dept_name=name,dept_HOD=HOD,dept_strength=strength)
	sdepartment.append(dpt)

def afterdepartment():
	dpt=Department.objects.all()
	for i in range(3):
		sdepartment.append(dpt[i])	

def pSubject(dept,semest,num):
	cont=0
	for did in sdepartment:
		for sem in range(semest):
			for sid in range(num):
				cont=cont+1
				name = fakegen.word()
				sub=Subject.objects.get_or_create(sub_id=cont,semester=sem,dept_id=did,sub_name=name)
				ssubject.append(sub)

def afterSubject():
	sub=Subject.objects.all()
	for i in sub:
		ssubject.append(i)	

def pTeacher(n):
	for j in range(n):
		tid = 1000000 + random.randint(0,99999)
		name = fakegen.name()
		word = fakegen.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
		mail = fakegen.email()
		teach=Teacher.objects.get_or_create(teacher_id=tid,teacher_name=name,password=word,email=mail)
		steacher.append(teach)

def afterTeacher():
	teach=Teacher.objects.all()
	for i in teach:
		steacher.append(i)	


def pTeacher_Subject(n):
	num = 1
	for i in ssubject:
		x=random.randint(1,3)
		ssno.append(x)
		for j in range(x):
			tid=random.choice(steacher)
			teach=Teacher_Subject.objects.get_or_create(sr_no=num,teacher_id=tid,sub_id=i)
			ssubjectteacher.append(teach)
			num = num + 1

def pClass(n):
	name=["FE","SE","TE","BE"]
	deptname=["IT","CS","EN"]
	x=0
	for dept in sdepartment:
		x=x+1
		for sem in range(1,4):
			for c in range(0,n):
				num=(1000*x)+(100*sem)+c
				tid=random.choice(steacher)
				cc=tid.teacher_name
				cla=Class.objects.get_or_create(class_id=num,class_name=(deptname[x-1]+name[sem-1]+str(c)),class_coordinator_name = cc, strength = 0, semester=sem,dept_id=dept)
				sclass.append(cla)

def afterclass():
	clss=Class.objects.all()
	for c in clss:
		sclass.append(c)


# table Parent
def pParent(n):
	for i in range(n):
		profile=fakegen.profile()
		parent_id = 990001+i
		parent_name = profile["name"]
		occupation = profile["job"]
		address = profile["residence"]
		password = fakegen.password()
		contact_no = ""
		for x in range(1,10):
			contact_no = contact_no + str(random.randint(0,9))
		email = profile["mail"]
		cla=Parent.objects.get_or_create(parent_id=parent_id,parent_name=parent_name,occupation=occupation,address=address,password=password,contact_no=contact_no,email=email)
		sParent.append(cla)

def afterparent():
	parents=Parent.objects.all()
	for prent in parents:
		sParent.append(prent)


# table Student
def pStudent(n):
	i=0
	cur=0
	classcount=len(sclass)
	parentcount=len(sParent)
	for pid in range(parentcount):
		profile=fakegen.profile()
		student_id = 190001+i
		i=i+1
		student_name = profile["name"]
		password = fakegen.password()
		email = profile["mail"]
		contact_no = ""
		for x in range(1,10):
			contact_no = contact_no + str(random.randint(0,9))
		parent_id = sParent[pid]
		if (cur>=classcount):
			cur=0
		class_id = sclass[cur]
		cur=cur+1
		stu=Student.objects.get_or_create(student_id=student_id,student_name=student_name,password=password,email=email,contact_no=contact_no,parent_id=parent_id,class_id=class_id)
		ssubject.append(stu)
		n=n-1
		if (n==0):
			break
		if (pid==(parentcount-1)):
			pid=0


def afterStudent():
	studs=Student.objects.all()
	for i in studs:
		sStudent.append(i)

'''
print("populating Department")
pdepartment(3)
print("done populating Department")
'''
'''
afterdepartment()
print("populating subjects")
pSubject(3,4,5)
print("done populating subjects")
'''
'''
print("populating teachers")
pTeacher(30)
print("done populating teachers")
'''
'''
print("populating sno")
afterTeacher()
afterSubject()
pTeacher_Subject(30)
print("done populating sno")
'''
'''
afterdepartment()
afterTeacher()
print("populating classes")
pClass(4)
print("done populating classes")
'''
'''
print("populating parents")
pParent(200)
print("done populating parents")
'''
'''
afterclass()
afterparent()
print("populating classes")
pStudent(230)
print("done populating classes")
'''

afterclass()
afterTeacher()
afterClass_Teacher()
afterSubject()
afterTeacher_Subject()
print("populating class_teacher")
pClass_Teacher()
print("done populating class_teacher")

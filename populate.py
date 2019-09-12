import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstpro.settings')

import django
django.setup()

##fake pop

import random
from stud_pro.models import Department,Subject,Teacher,Teacher_Subject
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

def pSubject(dept,semest,num):
	for did in sdepartment:
		for sem in range(semest):
			for sid in range(num):
				name = fakegen.word()
				sub=Subject.objects.get_or_create(sub_id=sid,semester=sem,dept_id=did,sub_name=name)
				ssubject.append(sub)

def pTeacher(n):
	for j in range(n):
		tid = 1000000 + random.randint(100000)
		name = fakegen.name()
		word = fakegen.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
		mail = fakegen.email()
		teach=Teacher.objects.get_or_create(teacher_id=tid,teacher_name=name,password=word,email=mail)
		steacher.append(teach)


def pTeacher_Subject(n):
	num = 1
	for i in ssubject:
		x=1+random.randint(3)
		ssno.append(x)
		for j in range(x):
			tid=random.choice(steacher)
			teach=Teacher.objects.get_or_create(sr_no=num,teacher_id=tid,sid=i)
			ssubjectteacher.append(teach)
			num = num + 1

def pClass(dept,semest,clss):
	for did in sdepartment:
		for sem in semest:
			for num in clss:

	class_id = models.IntegerField(primary_key=True)
	class_name = models.CharField(max_length=30)
	class_coordinator_name = models.CharField(max_length=30)
	strength = models.IntegerField()
	semester = models.IntegerField()
	dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)



print("populating Department")
pdepartment(3)
print("done populating Department")

'''
print("populating subjects")
pSubject(dept=3,semest=4,num=5)
print("done populating subjects")
'''
'''
print("populating teachers")
pTeacher(30)
print("done populating teachers")
'''
'''
print("populating sno")
pTeacher_Subject(30)
print("done populating sno")
'''



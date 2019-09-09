import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstpro.settings')

import django
django.setup()

##fake pop

import random
from firstapp.models import Parent,student
from faker import Faker

fakegen = Faker()
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


print("populating scripts")
popolu(10)
print("done populating")

from django.shortcuts import render,redirect

from stud_pro.forms import teacherform 
from stud_pro.models import *

def show(request):
	teachers = Teacher.objects.all()
	return render(request,"show.html",{'teachers':teachers})
# Create your views here.

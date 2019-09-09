from django import forms
from stud_pro.models import *

class teacherform(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = "__all__"


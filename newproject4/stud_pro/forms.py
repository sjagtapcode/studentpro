from django import forms
from stud_pro.models import *

class teacherform(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = "__all__"

class studentform(forms.ModelForm):
	cats = forms.ModelChoiceField(queryset=Class.objects.order_by('class_name').values_list('class_id', flat=True).distinct())
	class Meta:
		model = Student
		fields = "__all__"
		#fields = ("student_id","student_name","password","email","class_id")
		#widgets = {
		#'class_id' : [Class.objects.order_by('class_name').values_list('class_id', flat=True)]
		#}
#	def save(self , commit=True):

class parentform(forms.ModelForm):
	class Meta:
		model = Parent
		fields = "__all__"
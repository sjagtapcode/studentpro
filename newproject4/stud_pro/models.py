from django.db import models
# Create your models here.

# table department
class Department(models.Model):
	dept_id = models.IntegerField(primary_key=True)
	dept_name = models.CharField(max_length=30)
	dept_HOD = models.CharField(max_length=30)
	dept_strength = models.IntegerField()

	def __str__(self):
		return self.dept_name

# table subject
class Subject(models.Model):
	sub_id = models.IntegerField(primary_key=True)
	sub_name = models.CharField(max_length=30)
	semester = models.IntegerField()
	dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)
	def __str__(self):
		return self.sub_name

# table teacher
class Teacher(models.Model):
	teacher_id = models.IntegerField(primary_key=True)
	teacher_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.EmailField()

	def __str__(self):
		return self.teacher_name

#class desplay_dept_wise_teacher_sub(models.Model):

class Teacher_Subject(models.Model):
	sr_no = models.AutoField(primary_key=True)
	#sr_no = models.IntegerField(primary_key=True,auto_now_add=True)
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	sub_id = models.ForeignKey(Subject,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.sr_no)


# table class
class Class(models.Model):
	class_id = models.IntegerField(primary_key=True)
	class_name = models.CharField(max_length=30)
	class_coordinator_name = models.CharField(max_length=30)
	strength = models.IntegerField()
	semester = models.IntegerField()
	dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)
	def __str__(self):
		return self.class_name

# table class_teacher - this is the static table viewed only by teacher assigned by admin

class Class_Teacher(models.Model):
	class_id = models.ForeignKey(Class,on_delete=models.CASCADE)
	sr_no = models.ForeignKey(Teacher_Subject,on_delete=models.CASCADE)

# table Parent
class Parent(models.Model):
	parent_id = models.IntegerField(primary_key=True)
	parent_name = models.CharField(max_length=30)
	occupation = models.CharField(max_length=80)
	address = models.CharField(max_length=200)
	password = models.CharField(max_length=30)
	contact_no = models.CharField(max_length=15)
	email = models.CharField(max_length=50)
	def __str__(self):
		return self.parent_name

# table Student
class Student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	student_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	attendance = models.IntegerField(default=0)
	marks = models.IntegerField(default=0)
	email = models.CharField(max_length=50)
	contact_no = models.CharField(max_length=15,default="-")
	parent_id = models.ForeignKey(Parent,on_delete=models.PROTECT,null=True)
	class_id = models.ForeignKey(Class,on_delete=models.PROTECT,null=True)
# fd43b9ce3011007c17632851ce67e7a20d9e0c06
	def __str__(self):
		return self.student_name

# table Attendance_Marks
class Attendance_Marks(models.Model):
	student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
	sub_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
	attendance = models.IntegerField()
	marks = models.IntegerField()







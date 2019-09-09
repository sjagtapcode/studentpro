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
	dept_id = models.ForeignKey(Department,on_delete=models.PROTECT)

	def __str__(self):
		return self.sub_name

# table teacher
class Teacher(models.Model):
	teacher_id = models.IntegerField(primary_key=True)
	teacher_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

	def __str__(self):
		return self.teacher_name


# table teacher_subject
class Teacher_Subject(models.Model):
	sr_no = models.IntegerField(primary_key=True)
	teacher_id = models.ForeignKey(Teacher,on_delete=models.PROTECT)
	sub_id = models.ForeignKey(Subject,on_delete=models.PROTECT)

# table class
class Class(models.Model):
	class_id = models.IntegerField(primary_key=True)
	class_name = models.CharField(max_length=30)
	class_coordinator_name = models.CharField(max_length=30)
	strength = models.IntegerField()
	semester = models.IntegerField()
	dept_id = models.ForeignKey(Department,on_delete=models.PROTECT)

	def __str__(self):
		return self.class_name

# table class_teacher - this is the static table viewed only by teacher assigned by admin

class Class_Teacher(models.Model):
	class_id = models.ForeignKey(Class,on_delete=models.PROTECT)
	sr_no = models.ForeignKey(Teacher_Subject,on_delete=models.PROTECT)

# table Parent
class Parent(models.Model):
	parent_id = models.IntegerField(primary_key=True)
	parent_name = models.CharField(max_length=30)
	occupation = models.CharField(max_length=30)
	address = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	contact_no = models.IntegerField()
	email = models.CharField(max_length=30)

	def __str__(self):
		return self.parent_name

# table Student
class Student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	student_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	attendance = models.IntegerField()
	marks = models.IntegerField()
	email = models.CharField(max_length=30)
	parent_id = models.ForeignKey(Parent,on_delete=models.PROTECT)
	class_id = models.ForeignKey(Class,on_delete=models.PROTECT)
	def __str__(self):
		return self.student_name

# table Attendance_Marks
class Attendance_Marks(models.Model):
	student_id = models.ForeignKey(Student,on_delete=models.PROTECT)
	sub_id = models.ForeignKey(Subject,on_delete=models.PROTECT)
	attendance = models.IntegerField()
	marks = models.IntegerField()







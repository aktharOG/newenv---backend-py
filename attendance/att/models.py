from django.db import models

# Create your models here.
class Login(models.Model):
    user_id=models.CharField(max_length=4,primary_key=True)
    password=models.CharField(max_length=4)
    user_type=models.CharField(max_length=4)

class Classroom(models.Model):
    class_id=models.CharField(max_length=20,primary_key=True)
    # classname=models.CharField(max_length=20,unique=True)
    year=models.CharField(max_length=20,null=True)
    program=models.CharField(max_length=20,null=True)
                          
class Student(models.Model):
    student_id=models.CharField(max_length=10,primary_key=True)
    user_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=25)
    student_address=models.CharField(max_length=40)
    phone=models.CharField(max_length=12,unique=True)
    gender=models.CharField(max_length=6)
    email=models.CharField( max_length=50,unique=True)
    clas=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    image=models.ImageField(null=True)

class Teacher(models.Model):
    teacher_id=models.CharField(max_length=10,primary_key=True)
    user_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    teacher_name=models.CharField(max_length=25)
    teacher_address=models.CharField(max_length=40,null=True)
    phone=models.CharField(max_length=12,unique=True)
    gender=models.CharField(max_length=6)
    email=models.CharField( max_length=50,unique=True)
    class_incharge=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    image=models.ImageField(null=True)



class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    class_id=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    h1=models.BooleanField(default=1)
    h2=models.BooleanField(default=1)
    h3=models.BooleanField(default=1)
    h4=models.BooleanField(default=1)
    h5=models.BooleanField(default=1)
    h6=models.BooleanField(default=1)

class Timetable(models.Model):
    id=models.AutoField(primary_key=True)
    class_id=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    day=models.CharField(max_length=15)
    h1=models.CharField(max_length=30)
    h2=models.CharField(max_length=30)
    h3=models.CharField(max_length=30)
    h4=models.CharField(max_length=30)
    h5=models.CharField(max_length=30)
    h6=models.CharField(max_length=30)

class Notification(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=40)
    destination=models.CharField(max_length=10,default="1")
    


    

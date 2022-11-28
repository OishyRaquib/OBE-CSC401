from django.db import models

# Create your models here.

class Question(models.Model):
    SEMS=(
        ('Summer','Summer'),
        ('Spring','Spring'),
        ('Autumn', 'Autumn')
    )
    QID=models.AutoField(primary_key=True,auto_created=True)
    semester=models.CharField(max_length=6, choices=SEMS)
    year=models.IntegerField(default=2022)
    duration=models.IntegerField()
    question=models.TextField(max_length=500, null=True)
    # totalQuestions=
    # totalMarks=
    # CorrectAns=

# class Department(models.Model):
#     deptID=models.CharField(max_length=5, primary_key=True)
#     deptName=models.CharField(max_length=50)

# class Program(models.Model):
#     programID=models.CharField(max_length=1, primary_key=True)
#     programName=models.CharField(max_length=50,null=False)
#     DeptID=models.ForeignKey(Department)

# class User(models.Model):
#     TYPES=(('Faculty','Faculty'),
#     ('Student','Student')    
#     )
#     userID=models.CharField(max_field=7, primary_key=True)
#     name=models.CharField(max_length=100)
#     dateofbirth=models.DateField()
#     email=models.CharField(max_field=50)
#     phone=models.IntegerField(max_field=11)
#     address=models.CharField(max_field=100)
#     usertype=models.Model(choices=TYPES)

# class Faculty(User):
#     FUserID=models.OneToOneField(User,max_length=4,on_delete=models.SET_NULL)
#     position=models.CharField(max_length=30)
#     room=models.CharField(max_length=5, null=True)
#     managerID=models.ForeignKey(FUserID)
#     coordinatorID=models.ForeignKey(FUserID)
#     deptID=models.ForeignKey(Department,on_delete=models.SET_NULL)

# class Student(User):
#     SUserID=models.OneToOneField(User,max_length=7, on_delete=models.SET_NULL)
#     enroll_date=models.DateField()
#     programID=models.ForeignKey(Program)
#     deptID=models.ForeignKey(Department)


# class Section(models.Model):
#     secID=
#     secNo=
#     semester=
#     year=
#     FUserID=
#     CourseID=

# class Course(models.Model):
#     TYPES=(
#         ('Major','Major'),
#         ('Minor','Minor')
#     )
#     courseID=models.CharField(max_length=6, null=False)
#     courseName=models.CharField(max_length=50)
#     credits=models.IntegerField(max_length=1)
#     type=models.CharField(choices=TYPES)
#     programID=models.ForeignKey(Program)

# class Answer(models.Model):
#     marks=
#     FUserID=
#     SUserID=
#     QID=
#     COID=


# class PLO(models.Model):
#     PLONo=models.CharField()
#     PLOTitle=
#     PLODescription=
#     ProgramID=

# class CO(models.Model):
#     CONo=models.CharField(max_length=3)
#     Domain="Cognitive"
#     Level=models.IntegerField(max_length=1)
#     Statement=models.CharField(max_length=200)
#     SecID=models.ForeignKey(Section)

#models

class Department(models.Model):
    deptID=models.CharField(max_length=15)
    deptName=models.CharField(max_length=50)


class Program(models.Model):
    programID=models.CharField(max_length=5)
    programName=models.CharField(max_length=50,null=False)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)


class User(models.Model):
    # TYPES=(('Faculty','Faculty'),
    # ('Student','Student')    
    # )
    userID=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    email=models.CharField(max_length=50,blank=True)
    phone=models.IntegerField(blank=True)
    address=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    # usertype=models.Model(choices=TYPES)
    # def Meta(self):
    #     return self.userID

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    SUserID=models.CharField(max_length=7)
    enroll_year=models.IntegerField()
    programID=models.ForeignKey(Program,on_delete=models.CASCADE)
    deptID=models.ForeignKey(Department,on_delete=models.CASCADE)
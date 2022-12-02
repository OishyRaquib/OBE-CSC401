from django.db import models

# class Faculty(User):
#     FUserID=models.OneToOneField(User,max_length=4,on_delete=models.SET_NULL)
#     position=models.CharField(max_length=30)
#     room=models.CharField(max_length=5, null=True)
#     deptID=models.ForeignKey(Department,on_delete=models.SET_NULL)



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
#     course_deptID=models.ForeignKey(Department)

# class Answer(models.Model):
#     answer=models.CharField(max_length=1000)
#     fac_pk=models.ForeignKey(Faculty)
#     s_pk=models.ForeignKey(Student)
#     q_pk=models.ForeignKey(Question)
#     co_pk=models.ForeignKey(CO)


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

class Question(models.Model):
    SEMS=(
        ('Summer','Summer'),
        ('Spring','Spring'),
        ('Autumn', 'Autumn')
    )
    # QID=models.AutoField(primary_key=True,auto_created=True)
    semester=models.CharField(max_length=6, choices=SEMS)
    year=models.IntegerField(default=2022)
    duration=models.IntegerField()
    question=models.TextField(max_length=500)
    mark=models.FloatField()

    # totalQuestions=
    # totalMarks=
    correctAns=models.TextField(max_length=1000)

class Department(models.Model):
    deptID=models.CharField(max_length=15)
    deptName=models.CharField(max_length=50)
    def __str__(self):
        return self.deptName


class Program(models.Model):
    programID=models.CharField(max_length=5)
    programName=models.CharField(max_length=50,null=False)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.programName


class User(models.Model):
    userID=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    email=models.CharField(max_length=50,blank=True)
    phone=models.IntegerField(blank=True)
    address=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    SUserID=models.CharField(max_length=7)
    enroll_year=models.IntegerField()
    programID=models.ForeignKey(Program,on_delete=models.CASCADE,related_name="prg")
    deptID=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="dep")
    
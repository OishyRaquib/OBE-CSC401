from django.db import models


#models



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

class Course(models.Model):
    # TYPES=(
    #     ('Major','Major'),
    #     ('Minor','Minor')
    # )
    courseID=models.CharField(max_length=6, null=False,unique=True)
    courseName=models.CharField(max_length=50)
    credits=models.IntegerField()
    # type=models.CharField(max_length=5,choices=TYPES)
    programID=models.ForeignKey(Program,on_delete=models.CASCADE,related_name="course_prog")
    course_deptID=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="course_dep")
    def __str__(self):
        return self.courseID

class User(models.Model):
    userID=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    email=models.CharField(max_length=50,blank=True)
    phone=models.IntegerField(blank=True)
    address=models.CharField(max_length=100,blank=True)
    password=models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    SUserID=models.CharField(max_length=7)
    enroll_year=models.IntegerField()
    programID=models.ForeignKey(Program,on_delete=models.CASCADE,related_name="prg")
    deptID=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="dep")
    

class Faculty(models.Model):
    FUserID=models.CharField(max_length=4,unique=True)
    position=models.CharField(max_length=30)
    room=models.CharField(max_length=5, null=True)
    fac_deptID=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="fac_dep")

class Section(models.Model):
    SEMS=(
        ('Summer','Summer'),
        ('Spring','Spring'),
        ('Autumn', 'Autumn')
    )
    semester=models.CharField(max_length=6, choices=SEMS)
    # secID=models.Integer(max_length=2)
    secNo=models.IntegerField()
    year=models.IntegerField(default=2022)
    fac_id=models.ForeignKey(Faculty, on_delete=models.CASCADE,related_name="faculty_id")
    CourseID=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="sec_courseid")

class CO(models.Model):
    CONo=models.CharField(max_length=3,unique=True)
    Domain="Cognitive"
    Level=models.IntegerField()
    Statement=models.TextField(max_length=200)
    SecID=models.ForeignKey(Section,on_delete=models.CASCADE, related_name="co_sec")

class PLO(models.Model):
    PLONo=models.CharField(max_length=4,unique=True)
    PLOTitle=models.TextField(max_length=50)
    PLODescription=models.TextField(max_length=500)
    ProgramID=models.ForeignKey(Program, on_delete=models.CASCADE, related_name="plo_prog")

class CourseOutline(models.Model):

    CourseTitle=models.CharField(max_length=100, blank=True)
    courseCode=models.CharField(max_length=20, unique=True)
    courseResource=models.TextField(max_length=100)
    duration=models.CharField(max_length=10, blank=True)
    PreRequisite=models.CharField(max_length=100, blank=True)
    credit=models.IntegerField()
    contactHour=models.CharField(max_length=30, blank=True)
    grading=models.TextField(max_length=100)
    assesment=models.TextField(max_length=100)
    SEMS=(
        ('Summer','Summer'),
        ('Spring','Spring'),
        ('Autumn', 'Autumn')
    )
    semester=models.CharField(max_length=6, choices=SEMS)
    year=models.IntegerField(default=2022)

class Question(models.Model):
    SEMS=(
        ('Summer','Summer'),
        ('Spring','Spring'),
        ('Autumn', 'Autumn')
    )
    semester=models.CharField(max_length=6, choices=SEMS)
    year=models.IntegerField(default=2022)
    duration=models.IntegerField()
    question=models.TextField(max_length=500)
    mark=models.FloatField()
    course_q=models.OneToOneField(Course,on_delete=models.CASCADE,related_name="q_course")
    correctAns=models.TextField(max_length=1000)
    def __str__(self):
        return self.question

class Answer(models.Model):
    ans=models.CharField(max_length=1000)
    # fac_pk=models.ForeignKey(Faculty)
    # s_pk=models.ForeignKey(Student)
    q_pk=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="ans_qpk")
    # co_pk=models.ForeignKey(CO)


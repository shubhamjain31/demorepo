from django.db import models

# Create your models here.


class Student(models.Model):
    SECTION = (
        ('A', 'Alpha'),
        ('B', 'Beta'),
        ('C', 'Cappa'),
    )
    
    first_name 			= models.CharField(max_length=30)
    last_name 			= models.CharField(max_length=30)
    age 				= models.IntegerField()
    email 				= models.EmailField()
    mobile 				= models.CharField(max_length=15)
    website 			= models.URLField()
    section 			= models.CharField(max_length=1, choices=SECTION, default=SECTION[1][0])
    date_joined 		= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'student'


class Teacher(models.Model):
	name 			= models.CharField(max_length=100)
	user 			= models.ForeignKey('auth.User', on_delete=models.CASCADE)
	members 		= models.ManyToManyField(Student, through='Classroom')

	def __str__(self):
	    return self.name

	class Meta:
	    db_table = 'teacher'

class Classroom(models.Model):
    student 		= models.ForeignKey(Student, on_delete=models.CASCADE, related_name ='classroom_student')
    teacher 		= models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name ='classroom_teacher')
    date_joined 	= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.student)

    class Meta:
        db_table = 'classroom'


class Courses(models.Model):
	Credits = (
	    ('1', 'One'),
	    ('2', 'Two'),
	    ('3', 'three'),
	    ('4', 'four'),
	    ('6', 'Six'),
	)

	course_code 	= models.CharField(max_length=20, primary_key=True, default='CS-202')
	course_name 	= models.CharField(max_length=50)
	duration 		= models.CharField(max_length=1, choices=Credits)
	students 		= models.ManyToManyField(Student, related_name ='student_courses')

	def __str__(self):
	    return self.name

	class Meta:
	    db_table = 'courses'


class Grade(models.Model):
    student 		= models.ForeignKey(Student, on_delete=models.CASCADE)
    course 			= models.CharField(max_length=100)
    grade 			= models.IntegerField(default=0)

    def __str__(self):
        return str(self.student)

    class Meta:
        db_table = 'grade'
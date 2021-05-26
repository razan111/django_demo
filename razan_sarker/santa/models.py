from django.db import models

# Create your models here.

class Teacher(models.Model):
    Teacher_Name = models.CharField(max_length=100)
    Teacher_Age = models.IntegerField(default=0)
    Teacher_Dept = models.CharField(max_length=100)
    Teacher_Salary = models.FloatField(default=0.00)
    Teacher_Descation = models.TextField()

    def __str__(self):
        return self.Teacher_Name+"  "+self.Teacher_Age

class Students(models.Model):
    Student_Name = models.CharField(max_length=100)
    Student_Id = models.CharField(max_length=50)
    Student_Age = models.IntegerField(default=0)
    Student_Dept = models.CharField(max_length=100)
    Student_Cgpa = models.FloatField(default=0.00)

    def __str__(self):
        return self.Student_Dept


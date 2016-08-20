from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    course = models.ForeignKey(Course, default="Starter")

    def __str__(self):
        return self.name


class Classes(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    moduleName = models.ForeignKey(Module, default="DS1")

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    className = models.ManyToManyField(Classes)

    def __str__(self):
        return self.name


class SemesterClass(models.Model):
    id = models.AutoField(primary_key=True)
    semester = models.ForeignKey(Semester, default="2016-9")
    className = models.ForeignKey(Classes, default="DS-101")
    time = models.CharField(max_length=128, null=False)


class UserClass(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.ForeignKey(User)
    className = models.ForeignKey(SemesterClass)
    # moduleClass = models.CharField(max_length=128)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.ForeignKey(User, default="Sangyoon")



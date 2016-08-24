from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    module = models.ForeignKey(Module)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


class SemesterSubject(models.Model):
    id = models.AutoField(primary_key=True)
    semester = models.ForeignKey(Semester)
    subject = models.ForeignKey(Subject)
    time = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.subject.name

from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)

    def __str__(self):
        return self.name


class ClassModule(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    level = models.ForeignKey(Course)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    moduleName = models.ForeignKey(ClassModule)
    className = models.CharField(max_length=128)
    classCode = models.CharField(max_length=128)
    stdMax = models.IntegerField

    def __str__(self):
        return self.className

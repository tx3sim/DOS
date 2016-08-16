from django.db import models


# Create your models here.
class ClassLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class LevelModule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    level = models.ForeignKey(ClassLevel)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    moduleName = models.ForeignKey(LevelModule)
    className = models.CharField(max_length=128)
    classCode = models.CharField(max_length=128)
    stdMax = models.IntegerField

    def __str__(self):
        return self.className


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    types = models.ManyToManyField(ClassLevel, related_name='Timetables')

    def __str__(self):
        return self.name

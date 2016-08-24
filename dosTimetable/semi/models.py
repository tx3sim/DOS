from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User)


# Create your models here.
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=MyUserManager.normalize_email(email),
#             username=username,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password):
#         u = self.create_user(email=email,
#                              username=username,
#                              password=password,
#                              )
#         u.is_admin = True
#         u.save(using=self._db)
#         return u
#
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email',
#         max_length=255,
#         unique=True,
#     )
#     username = models.CharField(
#         u'이름',
#         max_length=10,
#         blank=False,
#         unique=False,
#         default='',
#     )
#
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __str__(self):
#        return self.email


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
    username = models.ForeignKey(User)
    className = models.ForeignKey(SemesterClass)
    # moduleClass = models.CharField(max_length=128)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User)

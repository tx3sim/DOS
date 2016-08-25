from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import datetime

from courses.models import SemesterSubject

GENDER = (
    ('M', '남자'),
    ('W', '여자'),
)


class MemberManager(BaseUserManager):
    def create_user(self, email, memberName, phoneNumber, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            memberName=memberName,
            phoneNumber=phoneNumber,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, memberName, phoneNumber, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                memberName=memberName,
                                phoneNumber=phoneNumber
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    memberName = models.CharField(max_length=10, default="")
    phoneNumber = models.CharField(blank=True, max_length=13)  # validators should be a list
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['memberName', 'phoneNumber']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class ChildMember(models.Model):
    id = models.AutoField(primary_key=True)
    memberName = models.ForeignKey(Member, default=0)
    childName = models.CharField(max_length=10)
    birthday = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=1, choices=GENDER, default="남자")
    school = models.CharField(max_length=255, default="")
    experience = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.childName

    def create_child(self, childName, birthday, school, gender, experience):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not childName:
            raise ValueError('Users must have an email address')

        user = self.model(
            childName=childName,
            birthday=birthday,
            school=school,
            gender=gender,
            experience=experience
        )

        user.save(using=self._db)
        return user


class ChildMemberSubject(models.Model):
    childName = models.ForeignKey(ChildMember)
    subject = models.ForeignKey(SemesterSubject)

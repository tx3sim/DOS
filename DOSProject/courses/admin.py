from django.contrib import admin

# Register your models here.
from courses.models import Course, Module, Subject, SemesterSubject, Semester


class SemesterSubjectAdmin(admin.ModelAdmin):
    model = SemesterSubject
    list_display = ['id', 'semester', 'subject', 'time']

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(SemesterSubject, SemesterSubjectAdmin)

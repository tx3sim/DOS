from django.contrib import admin
from semi.models import *

# Register your models here.


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Classes)
admin.site.register(Semester)
admin.site.register(UserClass)


class SemesterClassAdmin(admin.ModelAdmin):
    model = SemesterClass
    list_display = ['id', 'semester', 'className', 'time']


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['userName']

admin.site.register(Payment, PaymentAdmin)
admin.site.register(SemesterClass, SemesterClassAdmin)

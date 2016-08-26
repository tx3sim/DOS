"""DOSProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from courses.views import maker, getTimetable, altCourse, altClass
from members.views import apply_2, apply_1, payment_result, applyCheck, MemberLogin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', maker),
    url(r'^tt$', getTimetable),
    url(r'^altCourse$', altCourse),
    url(r'^altClass$', altClass),
    url(r'^apply_2$', apply_2),
    url(r'^apply_1$', apply_1),
    url(r'^login$', MemberLogin),
    url(r'^applyCheck$', applyCheck),
    url(r'^payment_result$', payment_result)
]

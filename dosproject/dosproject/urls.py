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
from django.views.generic import TemplateView

from courses.views import maker, getTimetable, altCourse, altClass
from members.views import apply_2, apply_1, payment_result, apply_3_2, apply_3_1, apply_3_1_1, MemberLogin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="pages/index.html")),
    url(r'^JuniorStartup/js_info.html$', TemplateView.as_view(template_name="pages/JuniorStartup/js_info.html")),
    url(r'^aboutus.html$', TemplateView.as_view(template_name="pages/aboutus.html")),
    url(r'^camp1.html$', TemplateView.as_view(template_name="pages/camp1.html")),
    url(r'^camp.html$', TemplateView.as_view(template_name="pages/camp.html")),
    url(r'^camp2.html$', TemplateView.as_view(template_name="pages/camp2.html")),
    url(r'^contacts.html$', TemplateView.as_view(template_name="pages/contacts.html")),
    url(r'^contactusDoc.html$', TemplateView.as_view(template_name="pages/contactusDoc.html")),
    url(r'^courses_home.html$', TemplateView.as_view(template_name="pages/courses_home.html")),
    url(r'^edu_supports.html$', TemplateView.as_view(template_name="pages/edu_supports.html")),
    url(r'^news.html$', TemplateView.as_view(template_name="pages/news.html")),
    url(r'^camp0/camp_1601/camp_1601_apply_01.html$', TemplateView.as_view(template_name="pages/camp0/camp_1601/camp_1601_apply_01.html")),
    url(r'^camp0/camp_1601/camp_1601_apply_02.html$', TemplateView.as_view(template_name="pages/camp0/camp_1601/camp_1601_apply_02.html")),
    url(r'^camp0/camp_1601/camp_1601_apply_03.html$', TemplateView.as_view(template_name="pages/camp0/camp_1601/camp_1601_apply_03.html")),
    url(r'^camp0/camp_1601/camp_1601_apply_04.html$', TemplateView.as_view(template_name="pages/camp0/camp_1601/camp_1601_apply_04.html")),
    url(r'^camp0/camp_1601/camp_1601_apply_05.html$', TemplateView.as_view(template_name="pages/camp0/camp_1601/camp_1601_apply_05.html")),
    url(r'^event/event_151021_1.html$', TemplateView.as_view(template_name="pages/event/event_151021_1.html")),
    url(r'^event/event_151021_2.html$', TemplateView.as_view(template_name="pages/event/event_151021_2.html")),
    url(r'^event/event_151125.html$', TemplateView.as_view(template_name="pages/event/event_151125.html")),
    url(r'^event/event_151210.html$', TemplateView.as_view(template_name="pages/event/event_151210.html")),
    url(r'^event/event_160211.html$', TemplateView.as_view(template_name="pages/event/event_160211.html")),
    url(r'^event/event_160309.html$', TemplateView.as_view(template_name="pages/event/event_160309.html")),
    url(r'^event/event_160621.html$', TemplateView.as_view(template_name="pages/event/event_160621.html")),
    url(r'^event/event_160705.html$', TemplateView.as_view(template_name="pages/event/event_160705.html")),
    url(r'^event/event_160730.html$', TemplateView.as_view(template_name="pages/event/event_160730.html")),
    url(r'^courses/creator$', TemplateView.as_view(template_name="pages/courses/creator.html")),
    url(r'^courses/starter$', TemplateView.as_view(template_name="pages/courses/starter.html")),
    #
    url(r'^courses/maker.html$', TemplateView.as_view(template_name="pages/courses/maker.html")),
    url(r'^Apply/apply_2$', apply_2),
    url(r'^Apply/apply_1$', apply_1),
    url(r'^login$', MemberLogin),
    url(r'^Apply/apply_3_2$', apply_3_2),
    url(r'^Apply/apply_3_1$', apply_3_1),
    url(r'^Apply/apply_3_1_1$', apply_3_1_1),
    url(r'^Apply/payment_result$', payment_result),
    #
    url(r'^tt$', getTimetable),
    url(r'^altCourse$', altCourse),
    url(r'^altClass$', altClass),
]

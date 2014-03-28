from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from resume.views import get_resume_list


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'resume_list.html')),
    url(r'^getResumeDate/$', 'resume.views.get_resume_list', name="get_resume_list"),
)

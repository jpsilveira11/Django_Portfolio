from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('experience', views.experience, name='experience'),
    path('projects', views.projects, name='projects'),
    path('certifications', views.certifications, name='certifications'),
    path('contact', views.contact, name='contact'),
    path('test',views.test,name='test'),
]
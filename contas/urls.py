from django.urls import path
from contas import views
urlpatterns = [

    path('', views.inicioBlog, name='blog'),
    path('about/', views.aboutBlog, name='about'),
    path('post/<int:id>', views.postBlog, name='post'),
    path('contact/', views.contactBlog, name='contact'),
    path('filter/<int:id>',  views.filterView, name='filter'),
    path('teste/<int:id>',  views.testeView, name='teste'),

]

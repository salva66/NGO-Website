from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('about_us/', views.about_us, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
    path('outlook/', views.outlook, name='outlook'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('articles/', views.articles, name='articles'),
    path('volunteerform/', views.volunteerform, name='volunteerform'),
    path('member/', views.member, name='member'),
    path('executive_director/', views.executive_director, name='executive_director'),

]
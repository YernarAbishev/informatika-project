from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('courses/', views.courses, name='courses'),
    path('courses/<slug:slug>/', views.courses, name='coursesFilter'),
    path('course/detail/<slug:slug>/', views.courseDetail, name='courseDetail'),
    path('course/detail/<slug:slug>/lessons/', views.lessonsList, name='lessonsList'),
    path('course/detail/<slug:slug>/lessons/<int:pk>/', views.lessonDetail, name='lessonDetail'),
    path('user/sign-up/', views.signUp, name='signUp'),
    path('user/login/', views.loginPage, name='loginPage'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
]
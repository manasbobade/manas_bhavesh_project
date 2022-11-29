from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('mainpage',views.mainpage,name="mainpage"),
    path('register',views.register,name="register"),
    path('weather',views.weather,name='weather'),
    path('disease',views.disease,name='disease'),
    path('homePage',views.homePage,name='homePage'),
    path('question/<int:id>',views.questionPage,name='question'),
    path('new-question',views.newQuestionPage,name='new-question'),
    path('reply', views.replyPage, name='reply') 
]

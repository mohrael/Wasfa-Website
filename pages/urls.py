from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('HomePage.html',views.homepage,name='homepage2'),
    path('register.html',views.register,name='register'),
    path('allrecipes_logged.html',views.allrecipes_logged,name='allrecipes_logged'),
    path('Meal_of_the_day.html',views.mealoftheday,name='meal of the day'),
    path('about.html',views.about,name='about'),
    path('login.html',views.login ,name='login'),
    path('userhomepage.html',views.userhomepage,name='user homepage'),
    path('adminhomepage.html',views.adminhomepage,name='admin homepage'),
    path('aboutadmin.html',views.aboutadmin,name='admin about'),
    path('aboutuser.html',views.aboutuser,name='user about'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('allrecepies-notlogged.html',views.allrecipes_notlogged,name='allrecipes_notlogged'),

]



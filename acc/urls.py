from turtle import update
from django.urls import path
from acc import views

app_name = "acc"

urlpatterns =[
    path('index/', views.index, name='index'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('signup/', views.signup,name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/', views.profile, name='profile'),
    path('chpass/', views.chpass, name='chpass')
]
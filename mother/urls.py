from django.urls import path
from mother import views
urlpatterns = [
    path('mother',views.mothers,name='mother'),
    path('createChild/<str:pk>/', views.createChild, name='createchild'),
    path('register',views.registerUser,name='register'),
    path('login',views.loginUser,name='login'),
    path('logoutUser/',views.logoutUser,name='logout'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('updateChild/<str:pk>/',views.updateChild,name='updatechild'),
    path('deleteChild/<str:pk>/',views.deleteChild,name='deletechild'),
    path('choose_meals/<str:pk>/',views.choose_meals,name='meals'),
    path('',views.home,name='home'),
    path('main',views.main,name='main'),
    path('addNotes/<str:pk>/',views.addNotes,name='addnotes'),
    path('updateProfil/',views.updateProfile,name='updateProfile'),
    path('notifications_m/',views.notifications_m,name='notifications_m'),
]
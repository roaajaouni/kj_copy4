from django.urls import path
from teacher import views

urlpatterns = [
    path('teachers',views.teachers,name='teachers'),
    path('teacherRegisteration',views.teacherRegisteration,name='teacherregister'),
    path('loginTeacher',views.loginTeacher,name='loginteacher'),
    path('chileprofile/<str:pk>/',views.childprofile,name='childprofile'),
    path('logoutUser',views.logoutUser,name='logoutuser'),
    path('createReport/<str:pk>/',views.createReport,name='createreport'),
    path('readreport/<str:pk>/',views.readReport,name='readreport'),
    path('readNotes/<str:pk>/',views.readNotes,name='readnotes'),
    path('updateProfilet/',views.updateProfilet,name='updateProfilet'),
    path('notifications_t/',views.notifications_t,name='notifications_t'),
    path('bus/<str:pk>/',views.bus,name='bus'),
    path('location_t/<str:pk>/',views.readlocation,name='location_t'),
]
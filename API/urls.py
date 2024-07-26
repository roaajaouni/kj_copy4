from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from mother.models import *

urlpatterns =[
    #paths
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getMoms),
    path('getMom/',views.getMom),
    path('updatemom/',views.updatemom),
    #path('addmom/',views.addMom),
    path('getchilds/',views.childProfile),
    path('addchild/',views.addChild),
    path('getchild/<str:pk>/',views.getchild),
    path('getchildmom/',views.getchildmom),
    path('updatechilds/<str:pk>/',views.updateChild),
    path('getTeachers/',views.getTeachers),
    path('getTeacher/',views.getTeacher),
    path('updateteacher/',views.updateteacher),
    path('deletechild/<str:pk>/',views.deleteChild),
    path('readreport/<str:pk>/',views.readReport),
    path('createreport/<str:pk>/',views.createReport),
    path('notes/<str:pk>/',views.notes),
    path('createnotes/<str:pk>/',views.createnotes),
    path('meal/<str:pk>/',views.meal),
    path('chosemeal/<str:pk>/',views.chosemeal),
    path('location/<str:pk>/',views.location),
    path('sendlocation/<str:pk>/',views.sendlocation),
    path('register/',views.register),
    path('getchildteacher/',views.getchildteacher),
    path('notifications/',views.notifications),
    path('notificationsmom/',views.notificationsmom),
    path('notificationsteacher/',views.notificationsteacher),
    path('getmeal/',views.getmeal),
    path('logout_view/',views.logout_view),
    path('childteacher/',views.childteacher),
]

    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from teacher.models import  Teacher
from mother.models import Child,Report
from django.contrib.auth.models import User

class TeacherCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1', 'password2']

class Childprofile(forms.ModelForm):
    class Meta:
        model = Child
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model= Report
        fields = '__all__'

class ProfileFormt(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['user']         
class busForm(forms.ModelForm):
    class Meta:
        model= Child
        fields = ['name','location','Important_notes','created']
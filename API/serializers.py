from rest_framework import serializers
from mother.models import Mother,Child,Report
from teacher.models import Teacher
from mother.models import *
class SignUpSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['email','username','password']
     extra_kwargs = {
         'email':{'required':True, 'allow_blank':False},
         'username':{'required':True, 'allow_blank':False},
         'password': {'required':True, 'allow_blank':False},
         
         
     }
class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        #fields = '__all__'
        
        fields=['username','email','phone','address']

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        #fields = '__all__'
        fields = ['id','mom','name','age','child_gender','featured_image','state_health']
       # exclude = ['teach','mom','featured_image']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
       # fields = '__all__'
        fields=['username','email','phone','address']
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        #fields = '__all__'
        fields = ['id','learn','activities','attiude','mood','created','child']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        #fields = '__all__'
        fields = ['name','notes']
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name','meal']
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name','location','Important_notes',]

class childteacherSerializer(serializers.ModelSerializer):
    teach = serializers.CharField()

    class Meta:
        model = Child
        fields = ['name', 'teach']

    def update(self, instance, validated_data):
        teach_username = validated_data.pop('teach', None)
        instance.name = validated_data.get('name', instance.name)
        if teach_username:
                teacher = Teacher.objects.get(username=teach_username)
                instance.teach = teacher
        instance.save()
        return instance
    

class childteacherSerializer(serializers.ModelSerializer):
    teach = serializers.SlugRelatedField(slug_field='username', queryset=Teacher.objects.all())
    class Meta:
        model = Child
        fields = ['name', 'teach']

    def update(self, instance, validated_data):
        teach_username = validated_data.pop('teach', None)
        instance.name = validated_data.get('name', instance.name)
        if teach_username:
                teacher = Teacher.objects.get(username=teach_username)
                instance.teach = teacher
        instance.save()
        return instance
       
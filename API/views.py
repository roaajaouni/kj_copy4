from rest_framework.response import Response
from rest_framework.decorators import api_view
from mother.models import Mother , Child
from teacher.models import Teacher
from API.serializers import *
from rest_framework import status
from django.contrib.auth.hashers import make_password
from notifications.signals import notify
from notifications.models import Notification
from django.contrib.auth import get_user
from django.contrib.auth.models import User,Group
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
##APIs

# @api_view(['POST'])
# def register(request):
#     data = request.data
#     user = SignUpSerializer(data=data)  
#     if user.is_valid():
#         if not User.objects.filter(username=data['username']).exists():
#             user = User.objects.create(
#                 email=data['email'],
#                 username=data['username'],
#                 password= data['password'],
                
#             )
        
#             return Response({'details': 'Your Account Registered Successfully!'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'This email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)  
    if user.is_valid():
        if not User.objects.filter(username=data['username']).exists():
            user = User.objects.create(
                email=data['email'],
                username=data['username'],
                password= make_password(data['password']),
                
            )
        
            return Response({'details': 'Your Account Registered Successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'This email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def getMoms(request):
    mothers = Mother.objects.filter(group=2)
    serializer = TeacherSerializer(mothers, many=True)
    return Response(serializer.data)
# تم اضافة هذا التابع ليجلب ام واحدة
@api_view(['GET'])
def getMom(request):
        user = User.objects.get(id=request.user.id)
        mothers = Mother.objects.filter(user=user)
        serializer = MotherSerializer(mothers, many=True)
        return Response(serializer.data)
###### تم الاضافة
@api_view(['POST'])
def updatemom(request):
    user = User.objects.get(id=request.user.id)
    mother = Mother.objects.get(user=user)
    serializer = MotherSerializer(instance=mother, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
@api_view(['POST'])
def addMom(request):
    serializer = MotherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def childProfile(request):
    child = Child.objects.all()
    print(child)
    serialzer = ChildSerializer(child,many=True)
    return Response(serialzer.data)


@api_view(['GET'])
def getchild(request,pk):
    child = Child.objects.get(id=pk)
    print(child)
    serialzer = ChildSerializer(child,many=False)
    return Response(serialzer.data)
#تم التعديل لكي يتم اضافة الطفل لام معينة
@api_view(['POST'])
def addChild(request):
    user = User.objects.get(id=request.user.id)
    mother = Mother.objects.get(user=user)
   
    serializer = ChildSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(mom=mother)
        return Response(serializer.data)

#####تمت اضافة هذا التابع ليجلب كل الاطفال لام معينة 
@api_view(['GET'])
def getchildmom(request):
    user = User.objects.get(id=request.user.id)
    mother = Mother.objects.get(user=user)
    child = mother.child_set.all()
    serialzer = ChildSerializer(child,many=True)
    return Response(serialzer.data)



@api_view(['POST'])
def updateChild(request,pk):
    child = Child.objects.get(id=pk)
    serializer = ChildSerializer(instance=child,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['GET'])
def getTeachers(request):
    teachers = Teacher.objects.filter(group=3)
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)
# تم اضافة هذا التابع ليجلب انسة واحدة
@api_view(['GET'])
def getTeacher(request):
    user = User.objects.get(id=request.user.id)
    teachers = Teacher.objects.get(user=user)
    serializer = TeacherSerializer(teachers,many=False)
    return Response(serializer.data)
##### تم الاضافة
@api_view(['POST'])
def updateteacher(request):
    user = User.objects.get(id=request.user.id)
    teacher = Teacher.objects.get(user=user)
    serializer = TeacherSerializer(instance=teacher,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteChild(request,pk):
    child = Child.objects.get(id=pk)
    child.delete()
    return Response('This Child has been deleted')

@api_view(['GET'])
def readReport(request,pk):
    child = Child.objects.get(id=pk)
    report = child.report_set.all()
    print(child)
    serializer = ReportSerializer(report,many=True)
    return Response(serializer.data)
#تم التعديل ليتم ربط الطفل بالتقرير
@api_view(['POST'])
def createReport(request, pk):
    child = Child.objects.get(id=pk)
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        # إنشاء نسخة جديدة من التقرير
        new_report = serializer.save()
        teacher = request.user.teacher
        mother = child.mom
        new_report.teacher = teacher
        new_report.child = child
        new_report.save()

        notify.send(
            sender=teacher,
            recipient=mother.user,
            verb='New report',
            description=f'Child {child.name} New Report '
        )
        
        return Response(serializer.data)

#تم الاضافة 
@api_view(['GET'])
def notes(request,pk):
    note = Child.objects.get(id=pk)
    print(note)
    serialzer = NoteSerializer(note,many=False)
    return Response(serialzer.data)

#تم الاضافة 
@api_view(['POST'])
def createnotes(request,pk):
    child = Child.objects.get(id=pk)
    serializer = NoteSerializer(instance=child,data=request.data)
    if serializer.is_valid():
          mother = request.user.mother
          teacher = child.teach
          serializer.save(mother=mother)
          notify.send(
            sender=mother,
            recipient=teacher.user,
            verb='New nots',
            description=f'Child {child.name} New Notes '
        )
        
    return Response(serializer.data)
#تم الاضافة 
@api_view(['GET'])
def meal(request,pk):
    meal = Child.objects.get(id=pk)
    print(meal)
    serialzer = MealSerializer(meal,many=False)
    return Response(serialzer.data)

#تم الاضافة 
@api_view(['POST'])
def chosemeal(request, pk):
        child = Child.objects.get(id=pk)
        serializer = MealSerializer(instance=child, data=request.data)

        if serializer.is_valid():
          mother = request.user.mother
          teacher = child.teach
          serializer.save(mother=mother)
          notify.send(
            sender=mother,
            recipient=teacher.user,
            verb='New meal',
            description=f'Child {child.name} New Meal'
        )
        
        return Response(serializer.data)
#تم الاضافة 
@api_view(['GET'])
def location(request, pk):
    location = Child.objects.get(id=pk)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)

#تم الاضافة 
@api_view(['POST'])
def sendlocation(request, pk):
    child = Child.objects.get(id=pk)
    serializer = LocationSerializer(instance=child, data=request.data) 
    if serializer.is_valid():
        teacher = request.user.teacher
        mother = child.mom
        serializer.save(teacher=teacher)
        notify.send(
            sender=teacher,
            recipient=mother.user,
            verb='New Location',
            description=f'Child {child.name} New Location'
        )
        
        return Response(serializer.data)
    return Response(serializer.data)
@api_view(['GET'])
def notifications(request):
    notifications = request.user.notifications.all()
    serialized_notifications = [{"verb": n.verb, "description": n.description} for n in notifications]
    return Response(serialized_notifications)

@api_view(['GET'])
def notificationsmom(request):
    user = User.objects.get(id=request.user.id)
    mother = Mother.objects.get(user=user)
    notifications = Notification.objects.filter(recipient=mother.user)
    serialized_notifications = [{"verb": n.verb, "description": n.description} for n in notifications]
    
    return Response(serialized_notifications)

@api_view(['GET'])
def notificationsteacher(request):
    user = User.objects.get(id=request.user.id)
    teachers = Teacher.objects.get(user=user)
    notifications = Notification.objects.filter(recipient=teachers.user)
    serialized_notifications = [{"verb": n.verb, "description": n.description} for n in notifications]
    return Response(serialized_notifications)
@api_view(['GET'])
def getmeal(request):
    meal_types = Child.meal_types
    meal_images = {
    'meat': 'images/food/meat.jpg',
    'milk': 'images/food/Milk.jpg',
    'sandwich': 'images/food/sandwich.jpg',
    'nuggets': 'images/food/Nuggets.jpg',
    'burger': 'images/food/Burger.jpg',
    'pasta': 'images/food/Pasta.jpg',
    'pie': 'images/food/Pie.jpg',
    'pizza': 'images/food/Pizza.jpg',
    'pancake': 'images/food/Pancake.jpg',
    'waffle': 'images/food/Waffle.jpg'
    }

    meals = [{'name': meal[1], 'image': meal_images.get(meal[0], 'default_image.jpg')} for meal in meal_types]
    return Response(meals)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'details': 'Successfully logged out.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getchildteacher(request):
    user = User.objects.get(id=request.user.id)
    teacher = Teacher.objects.get(user=user)
    child = teacher.child_set.all()
    serialzer = ChildSerializer(child,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def childteacher(request, pk):
    child = Child.objects.get(id=pk)
    serializer = childteacherSerializer(instance=child, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def childteacher(request):
    data = request.data
    for child_data in data:
        child_name = child_data.get('name')  # تحديد اسم الطفل
        child = Child.objects.get(name=child_name)
        teach_username = child_data.get('teach')  # اسم المعلم الجديد
        teacher = Teacher.objects.get(username=teach_username)
        child.teach = teacher
        child.save()

    serializer = childteacherSerializer(instance=Child.objects.all(), many=True)
    return Response(serializer.data)


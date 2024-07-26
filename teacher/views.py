from django.shortcuts import render
from teacher.models import Teacher
from mother.models import Child, Mother
from mother.decorators import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from teacher.teacherForms import *
from notifications.signals import notify


# @allowed_users(allowed_roles=['admin','teachers'])
def loginTeacher(request):
    if request.user.is_authenticated:
        return redirect('teachers')
    else:
        messages.error(request, 'can not do this')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('teachers')
        else:
            messages.error(request, 'username or password is incorrect')

    return render(request, 'log-reg.html')

@allowed_users(allowed_roles=['admin','teachers'])
def teacherRegisteration(request):
    page = 'register'
    form = TeacherCreation()
    if request.method == 'POST':
        form = TeacherCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('teachers')
        else:
            messages.error(request, 'Can\'t register')
    context = {'page': page, 'form': form}
    return render(request, 'log-reg.html', context)

@allowed_users(allowed_roles=['admin','teachers'])
def logoutUser(request):
    logout(request)
    return redirect('loginteacher')

@allowed_users(allowed_roles=['admin','teachers'])
def teachers(request):
    teachers = Teacher.objects.all()
    print(teachers)
    teacher = request.user.teacher
    if 'search_query'in request.GET:
        search_query=request.GET['search_query']
        children = Child.objects.filter(name=search_query)
    else:    
      children = Child.objects.all()
    context = {'children': children, 'teacher': teacher}
    return render(request, 'teachers.html', context)

@allowed_users(allowed_roles=['admin','teachers'])
def childprofile(request, pk):
    child = Child.objects.get(id=pk)
    context = {
        'child': child,
    }
    return render(request, 'childprofile.html', context)


# اضافة الاشعار 
def createReport(request,pk):
    teacher = request.user.teacher
    child = Child.objects.get(id=pk)
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
           report = form.save(commit=False)
           report.user = request.user.teacher
           report.teacher = teacher
           report.child = child
           mother = child.mom
           report.save()
           notify.send(sender=teacher, recipient=mother.user, verb='new report ',action_objects=report)
           return redirect('teachers')
        else:
            ReportForm()
    context = {'teacher':teacher,'child':child,'form':form}
    return render(request,'reportform.html',context)

def readReport(request,pk):
    child = Child.objects.get(id=pk)
    report = child.report_set.all()
    context = {'child':child,'report':report}
    return render(request,'readreport.html',context)

def readNotes(request,pk):
    child = Child.objects.get(id=pk)
    context = {'child':child}
    return render(request,'readnotes.html',context)





def updateProfilet(request):
    teacher = request.user.teacher
    forms = ProfileFormt(instance=teacher)
    if request.method =='POST':
        forms = ProfileFormt(request.POST,instance=teacher)
        if forms.is_valid():
           teacher.save()
           return redirect('teachers')
        else :
          forms = ProfileFormt()  
    context = {'teacher':teacher,
               'forms':forms}
    return render(request,'account_teacher.html',context)
#def teachers(request):
    #search_query = ''
    #if request.GET.get('search_query'):
       # search_query = request.GET.get('search_query')
    #teachers = Teacher.objects.all()
    #print(teachers)
   # teacher = request.user.teacher
    #children = Child.objects.filter( name=search_query)
    #children = Child.objects.filter( name=search_query)
    #context = {'children': children, 'teacher': teacher, 'search_query': search_query}
    #return render(request, 'teachers.html', context)

def notifications_t (request):
     notifications= request.user.notifications.all()
     notification_count = notifications.count()
     context = {
         'notifications': notifications,
         'notification_count': notification_count ,
     }


     return render(request,'notifications_t.html', context)    


def bus(request,pk):
    teacher = request.user.teacher
    child = Child.objects.get(id=pk)
    form = busForm()
    if request.method == 'POST':
        form = busForm(request.POST)
        if form.is_valid():
           report = form.save(commit=False)
           report.user = request.user.teacher
           report.teacher = teacher
           report.child = child
           mother = child.mom
           report.save()
           notify.send(sender=teacher, recipient=mother.user, verb='child_location ',action_objects=report)
           return redirect('teachers')
        else:
            busForm()
    context = {'teacher':teacher,'child':child,'form':form}
    return render(request,'location.html',context)

def readlocation(request,pk):
   child = Child.objects.get(id=pk)
   context = {'child':child}
   return render(request,'readlocation.html',context)
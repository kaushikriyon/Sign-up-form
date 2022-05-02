from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import User
# Create your views here.
def Login(request):
    return render(request, 'login.html')


def Signup(request):
    return render(request, 'signup.html')


def get_login_data(request):
    res = {'status' : "False",'msg' : "Data not fetched..."}
    if request.method == 'POST':
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        password=request.POST.get('Password')
        print("\n\n\n")
        print('Name ',name, 'Email', email, 'Password', password)
        print("\n\n\n")
        # User.objects.create(
        # name = name,
        # email =  email,
        # password = password,)
        # User_data=User.objects.all()
        # res = {'status' : 'Save','data' : User_data}
        # res={'status':"LoggedIn"}
        return JsonResponse({'status':"LoggedIn"})
        # return HttpResponse(json.dumps(res), content_type='application/json')
    # return HttpResponse(json.dumps(res), content_type='application/json')
    return JsonResponse({'status':"NotLoggedIn"})


def get_signup_data(request):
    res = {'status' : "False",'msg' : "Data not fetched..."}
    if request.method == 'POST':
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        password=request.POST.get('Password')
        print("\n\n\n")
        print('Name ',name, 'Email', email, 'Password', password)
        print("\n\n\n")
        # User.objects.create(
        # name = name,
        # email =  email,
        # password = password,)
        # User_data=User.objects.all()
        # res = {'status' : 'Save','data' : User_data}
        # res={'status':"Submitted"}
        return JsonResponse({'status':'Submitted'})
        # return HttpResponse(json.dumps(res), content_type='application/json')
    # return HttpResponse(json.dumps(res), content_type='application/json')
    return JsonResponse({'status':'NotSubmitted'})



    


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)



        if password != password2:
            return redirect('/sign-up')
        else:
            exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return HttpResponse("아이디가 존재합니다!!")
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio
                new_user.save()
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        me = UserModel.objects.get(username=username)

        if password == me.password:
            return render(request,'mainpage.html',{'username':username})
        else:
            return redirect('/sign-in')
        
    elif request.method == 'GET':
        return render(request,'user/signin.html')
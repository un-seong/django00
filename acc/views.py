from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'acc/index.html')

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u: # 로그인 성공 시
            login(request, u) # 로그인을 u에 실어야함
            messages.success(request, f"{un}님 환영합니다.")
            return redirect("acc:index")
        else:
            messages.error(request, "계정정보가 일치하지 않습니다.")
    return render(request, 'acc/login.html')


def userlogout(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
            return redirect("acc:login")
        except:
            un = request.POST.get("uname")
            up = request.POST.get("upass")
            uc = request.POST.get("ucomm")
            pi = request.FILES.get("upic")
            messages.error(request, "계정이름이 이미 존재합니다.")
    return render(request, 'acc/signup.html')

def profile(request):
    return render(request, "acc/profile.html")

def delete(request):
    u=request.user
    cp= request.POST.get('cpass')
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.error(request, "비밀번호 정보가 일치하지 않습니다.")
    return redirect("acc:profile")

def update(request):
    if request.method == "POST":
        u = request.user
        ue = request.POST.get('umail')
        uc = request.POST.get('ucomm')
        up = request.FILES.get('upic')
        if up:
            u.pic.delete()
            u.pic = up
        u.email, u.comment = ue, uc
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")

def chpass(request):
    u = request.user
    cp = request.POST.get('cpass')
    if check_password(cp, u.password):
        np = request.POST.get('npass')
        u.set_password(np)
        u.save()
        return redirect('acc:login')
    else:
        messages.error(request, "비밀번호가 맞지않습니다..")
    return redirect("acc:update")


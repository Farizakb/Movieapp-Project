from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ChangePasswordForm, RegisterForm, UserForm, UserModelForm,ProfileForm
# Create your views here.



def login_req(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password  = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            if User.objects.filter(email__iexact = email).exists():
                
                username = User.objects.get(email__iexact = email).username
                user = authenticate(username=username,password=password)
                
                if user is not None:
                    login(request, user)
                    
                    if not remember_me:
                        request.session.set_expiry(0)
                        request.session.modified  = True
                    return redirect("home")
                else:
                    form.add_error(None,"Email ve ya Parol duzgun daxil edilmiyib")
                    return render(request, 'users/login.html',{"form":form})
           
        else:
            return render(request, 'users/login.html',{"form":form})
            
    form = UserForm()
    return render(request, 'users/login.html',{"form":form})



def register_req(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            print(user.username)
            return redirect("login")
        

        else:
            form.add_error(None,"Formu duzgun doldurun zehmet deilse")
            return render(request, 'users/register.html', {"form":form})
            
    form = RegisterForm()
    
    return render(request, 'users/register.html', {"form":form})

def logout_req(request):
    logout(request)
    return redirect("home")



def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"parol deyisdirildi")
            return redirect("change_password")
        else:
             return render(request, 'users/change_password.html',{
                "form":form
            })
                    
    
    form = ChangePasswordForm(request.user)
    return render(request, 'users/change_password.html',{
        "form":form
    })

def watch_list(request):
    return render(request, 'users/watch_list.html')



@login_required(login_url="/users/login")
def profile(request):
    if request.method =="POST":
        user_form = UserModelForm(request.POST,instance = request.user)
        profile_form = ProfileForm(request.POST,instance = request.user.profile, files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Deyisiklikler ugurla edilmisdir")
            return redirect("profile")
            
        else:
            messages.error(request,"Melumatlari duzgun daxil edin")
            return render(request, 'users/profile.html',{
                "user_form":user_form,
                "profile_form":profile_form
            })
                    
    else:
        
        user_form = UserModelForm(instance = request.user)
        profile_form = ProfileForm(instance = request.user.profile)
        
        
        
        return render(request, 'users/profile.html',{
            "user_form":user_form,
            "profile_form":profile_form
        })
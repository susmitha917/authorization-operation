from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm

# Create your views here.

#For User Sign up
def sign_up(request):
  if request.method=='POST':
    fm=SignUpForm(request.POST)
    if fm.is_valid():
       messages.success(request,'Account Create Successfully !')
       fm.save()
     

  else:    
    fm=SignUpForm()
  return render(request,'api/signup.html',{'form':fm})

#For User Login

def login_user(request):
 if not request.user.is_authenticated: 
  if request.method=='POST':
    fm=AuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
      uname=fm.cleaned_data['username']
      upass=fm.cleaned_data['password']
      user=authenticate(username=uname,password=upass)
      if user is not None:
        login(request,user)
        messages.success(request,'Login Suessfully !!')
        return HttpResponseRedirect('/profile/')
  else:
   fm=AuthenticationForm()
  return render(request,'api/userlogin.html', {'form':fm}) 
 else:
   return HttpResponseRedirect('/profile/')
   

#For User Profile
def user_profile(request):
  if request.user.is_authenticated:
   return render(request,'api/profile.html',{'name' : request.user})
  else:
    return HttpResponseRedirect('/userlogin/')

# For Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/userlogin/')

# For Change Password with old password

def user_change_pass(request):
 if request.user.is_authenticated: 
   if request.method=="POST":
     fm = PasswordChangeForm(user=request.user , data=request.POST)
     if fm.is_valid():
       fm.save
       messages.success(request,'password Change Suessfully !!')
       update_session_auth_hash(request,fm.user)
       return HttpResponseRedirect('/profile/')
   else:
    fm = PasswordChangeForm(user=request.user)
   return render(request,'api/changepass.html', {'form':fm})
 else:
   return HttpResponseRedirect('/userlogin/')
 
 #For Change password without old password

def user_change_pass1(request):
 if request.user.is_authenticated: 
   if request.method=="POST":
     fm = SetPasswordForm(user=request.user , data=request.POST)
     if fm.is_valid():
       fm.save
       messages.success(request,'password Change Suessfully !!')
       update_session_auth_hash(request,fm.user)
       return HttpResponseRedirect('/profile/')
   else:
    fm = SetPasswordForm(user=request.user)
   return render(request,'api/changepass1.html', {'form':fm})
 else:
   return HttpResponseRedirect('/userlogin/')


from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from django.utils.decorators import method_decorator


# Create your views here.

def signin_required(fun):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            messages.error(request,"Unsuccessful...!Login Required")
            return redirect('signin')
    return inner

@method_decorator(signin_required,name='dispatch')
class Home(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            form = TodoForms()
            return render(request,'home.html',{'form':form})
        else:
            return render(request,'home.html')
        
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            user=request.user
            form_data = TodoForms(data=request.POST)
            if form_data.is_valid():
                todo=form_data.save(commit=False)
                todo.user=user
                todo.save()
                messages.success(request,'Activity Added...!')
                return redirect('details')
            else:
            # messages.error(request,'Unsuccessful...!')
                 return render(request,'signin.html')

class SigninReg(View):
    def get(self,request,*args,**kwargs):
        form = SigninForm()
        return render(request,'signin.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form_data = SigninForm(data=request.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get('username')
            pswd  = form_data.cleaned_data.get('password')
            user  = authenticate(username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,'Login Successfully...!')
                return redirect('home')
            else:
                messages.error(request,'Unsuccessful...!')
                return render(request,'signin.html',{'form':form_data})
        else:
            return render(request,'signin.html',{'form':form_data})
 
class SignupReg(View):
    def get(self,request,*args,**kwargs):
        form = SignupForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form_data = SignupForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('signin')
        else:
            messages.error(request,'Unsuccessful...!')
            return render(request,'signup.html',{'form':form_data})
 
       
class LgOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')
    
@method_decorator(signin_required,name='dispatch')   
class Details(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            user = request.user
            details = Todoo.objects.filter(user=user)
            return render(request,'details.html',{'details':details})
        else:
             return render(request,'details.html')
            
        
    
class Delete(View):
    def get(self,request,*args,**kwargs):
        tdel = kwargs.get('tdel')
        todo = Todoo.objects.get(id=tdel)
        todo.delete()
        messages.success(request,'Activity Deleted')
        return redirect('details')
    
@method_decorator(signin_required,name='dispatch')    
class Update(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            tupd = kwargs.get('tupd')
            todo = Todoo.objects.get(id=tupd)
            form = TodoForms(instance=todo)
            return render(request,'update.html',{'form':form})
        else:
            return render(request,'update.html')
        
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            user=request.user
            tupd = kwargs.get('tupd')
            todo    = Todoo.objects.get(id=tupd)
            form_data = TodoForms(data=request.POST,instance=todo)
            if form_data.is_valid():
                form_data.instance.user=user
                form_data.save()
                messages.success(request,'Activity Updated Successfully...!')
                return redirect('details')
            else:
                # messages.error(request,'Unsuccessful...!')
                return render(request,'update.html',{'form':form_data})
                      


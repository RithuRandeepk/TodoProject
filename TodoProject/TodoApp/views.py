from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,DeleteView,ListView,UpdateView
from django.http import HttpResponse
from TodoApp.forms import SignUpForm,SignInForm,TodoForm,TodoEditForm
from django.core.mail import send_mail,settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from TodoApp.models import Todos
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from TodoApp.decorators import login_required



class Home(TemplateView):
     template_name='home.html'


# class SignUp(View):

#      def get(self,request,*args,**kwargs):
#           form=SignUpForm()
#           return render(request,"signup.html",{"form":form})
     
#      def post(self,request,*args,**kwargs):

#           form=SignUpForm(request.POST)
#           print(form)

#           if form.is_valid():
#                # form.save()
#                User.objects.create_user(**form.cleaned_data)
#                return HttpResponse("Saved")
class SignIn(View):

     def get(self,request,*args,**kwargs):

          form=SignInForm()
          return render(request,'signin.html',{"form":form})
     
     def post(self,request,*args,**kwargs):

          form = SignInForm(request.POST)
          print(form)

          if form.is_valid():
               uname=form.cleaned_data.get('username')
               psw=form.cleaned_data.get('password')
               user=authenticate(request,username=uname,password=psw)
               print(user)

               if user:

                    login(request,user)

                    msg='LOGIN SUCCESFULL'
                    messages.success(request,msg)

                 
                    return redirect('todocreate')
                    # return render(request,'signin.html')
               
               else:
                    msg='invalid credentials'
                    messages.error(request,msg)
                    return render(request,'signin.html')

@method_decorator(login_required,name='dispatch')             
class SignOut(View):
     # def get(self,request,*args,**kwargs):
     #      if request.user.is_authenticated:
                    
     #           logout(request)
     #           return redirect('hm')
     #      else:
     #           messages.error(request,'you must login first')
     #           return redirect('signin')

     def get(self,request,*args,**kwargs):

          logout(request)
          return redirect('hm')



# class Home(View):

#      def get(self,request,*args,**kwargs):
         
#           return render(request,'home.html')
# class TodoCreate(View):

#      def get(self,request,*args,**kwargs):

#           form=TodoForm()

#           return render(request,'todocreate.html',{'form':form})
     
#      def post(self,request,*args,**kwargs):

#           form=TodoForm(request.POST)
#           if form.is_valid():
#                form.instance.user=request.user
#                form.save()
#                return redirect('hm')

class TodoCreate(CreateView):

     model=Todos
     template_name='todocreate.html'
     form_class=TodoForm
     success_url=reverse_lazy('todolist')

     def form_valid(self, form):
          form.instance.user=self.request.user
          messages.success(self.request,'The task was created succesfully')
          return super().form_valid(form)

class SignUp(CreateView):
     model=User
     template_name='signup.html'
     form_class=SignUpForm
     success_url=reverse_lazy('signin')

     def form_valid(self, form):
          return super().form_valid(form)







# class TodoList(View):


#      def get(self,request,*args,**kwargs):
          
#           # form=Todos.objects.all()
#           form=Todos.objects.filter(user=request.user)
#           return render(request,'todolist.html',{'form':form})

class TodoList(ListView):

     model=Todos
     template_name="todolist.html"

     context_object_name="form"

     def get_queryset(self):
          return Todos.objects.filter(user=self.request.user)





     
# class TodoEdit(View):
#      def get(self,request,*args,**kwargs):
#           # print(args)
#           # print(kwargs)
#           id=kwargs.get('id')
#           data=Todos.objects.get(id=id)
#           form=TodoEditForm(instance=data)

         
#           return render(request,'todoedit.html',{"form":form})
     
#      def post (self,request,*args,**kwargs):
#           id=kwargs.get('id')
#           data=Todos.objects.get(id=id)

#           form=TodoEditForm(request.POST,instance=data)

#           if form.is_valid():
#                form.save()
#                return redirect('todolist')
class TodoDelete(View):
     def get(self,request,*args,**kwargs):
          # print(args)
          # print(kwargs)
          id=kwargs.get('id')
          data=Todos.objects.get(id=id).delete()
          return redirect('todolist')

class TodoEdit(UpdateView):
     model=Todos
     template_name='todoedit.html'
     form_class=TodoEditForm
     success_url=reverse_lazy('todolist')
     pk_url_kwarg='id'

     def form_valid(self, form):
          messages.success(self.request,'edited succesfully')
          return super().form_valid(form)
     
class TodoDelete(DeleteView):
    model = Todos
    template_name = 'deletetodo.html'
    success_url = reverse_lazy('todolist')
    pk_url_kwarg='id'










               









          
   


          
          


          

          
                  
       

        
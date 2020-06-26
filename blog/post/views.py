from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout
from .forms import CreateUserForm, profileform, post_form
from django.contrib.auth.forms import UserCreationForm
from .models import profile as userProfile
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def index(request):
    return render(request , 'post/index.html')

def home(request):
    context={
        'pst' : reversed(blog.objects.all())
    }
    return render(request, 'post/home.html',context)

class blogListView(ListView):
    model = blog
    template_name = 'post/home.html'
    context_object_name = 'pst'
    ordering = ['-date']

class blogDetailView(DetailView):
    model = blog
    
class blogUpdateView(UserPassesTestMixin ,UpdateView):
    template_name='post/posts.html'
    model = blog
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pst = self.get_object()
        print("Ass")
        print(pst.user)
        if self.request.user == pst.user:
            return True
        return False

class blogDeleteView(UserPassesTestMixin ,DeleteView):
    template_name='post/delete.html'
    model = blog
    success_url = '/home/'
    def test_func(self):
        pst = self.get_object()
        if self.request.user == pst.user:
            return True
        return False

def register(request):
        if(request.method=="POST"):
            form = CreateUserForm(request.POST)
            pform = profileform(request.POST)
            if(form.is_valid() and pform.is_valid()):
                user=form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ username)
                return redirect('/login')
        else:
            form = CreateUserForm()
            pform = profileform()

        context= {'form':form , 'pform':pform}
        return render(request,'post/register.html',context)



def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username , password=password)
            if user is not None :
                auth_login(request,user)
                return redirect('/home/')
            else:
                messages.info(request , "Username or password incorrect")

    return render(request,'post/login.html')



def profile(request):
    prof = request.user.profile
    form = profileform(instance=prof)
    if request.method == "POST":
        form = profileform(request.POST , request.FILES , instance=prof)
        if form.is_valid():
            form.save()
    context={'form':form ,'i':issued_item}
    return render(request , 'post/profile.html',context)


def logouts(request):
    logout(request)
    return redirect('/login/')

def posts(request):
    if(request.method=="POST"):
        form = post_form(request.POST)
        title = request.POST["title"]
        pst = request.POST["posts"]
        c = blog(user=request.user ,title=title, content = pst)
        c.save()
        messages.success(request, "Your post has been posted")
    else:
        form = post_form()
    context = {'form':form}
    return render(request,'post/posts.html' , context)

def error(request):
    return render(request , 'post/error.html')


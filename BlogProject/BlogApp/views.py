from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from .forms import BlogForm

def base(request):
    context={}
    return render(request, "BlogApp/base.html", context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_list')
        else:
            return render(request, 'BlogApp/login.html', {'error': 'Invalid username or password'})
    return render(request, "BlogApp/login.html")


def logout_page(request):
    logout(request)
    return redirect('../')


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect('../')
    return render(request, "BlogApp/register.html")

@login_required(login_url='../')
def home(request):
    return render(request, 'BlogApp/user/home.html')

@login_required(login_url='../')
def userbase(request):
    return render(request, "BlogApp/user/userbase.html")


@login_required(login_url='../')  
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at') 
    return render(request, 'BlogApp/user/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'BlogApp/user/blog_detail.html', {'blog': blog})


@login_required(login_url='../')
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'BlogApp/user/blog_form.html', {'form': form})

@login_required(login_url='../')
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.author:
        messages.error(request, 'You do not have permission to edit this blog!')
        return redirect('blog_list')

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully!')
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'BlogApp/user/blog_form.html', {'form': form})


@login_required(login_url='../')
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.author:
        messages.error(request, 'You do not have permission to delete this blog!')
        return redirect('blog_list')
    
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted successfully!')
        return redirect('blog_list')

    return render(request, 'BlogApp/user/blog_confirm_delete.html', {'blog': blog})

def blog_cards(request):
    blogs = Blog.objects.all()
    return render(request, 'BlogApp/blog.html', {'blogs': blogs})

def blogdetail (request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'BlogApp/blogdetails.html', {'blog': blog})

def about(request):
    return render(request, 'BlogApp/about.html')
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect, get_object_or_404
# from.models import myBlogs
# from.forms import BlogForm
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import logout as auth_logout
#
#
# def home(request):
#     blogs = myBlogs.objects.all()
#     return render(request, 'notes/home.html', {'blogs': blogs})
#
# def blog_detail(request, blog_id):
#     blog = get_object_or_404(myBlogs, id=blog_id)
#     return render(request, 'notes/blog_detail.html', {'blog': blog})
# # def signup_view(request):
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#         else:  # <-- this runs on GET
#             form = UserCreationForm()
#     return render(request, 'notes/signup.html', {'form': form})
#
#     # if request.method == 'POST':
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         user = form.save()
#     #         login(request, user)
#     #         return redirect('home')
#     #     else:
#     #         form = UserCreationForm()
#     # return render(request, 'notes/signup.html', {'form': form})
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('home')
#         else :
#             return redirect('signup')
#
# def logout_view(request):
#     auth_logout(request)
#     return render(request, "notes/logout.html")
#
#
#
#
# @login_required
#
# def create_blog(request):
#     if request.method == "POST":
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             return redirect('home')
#         else:
#             form = BlogForm()
#         return render(request,'notes/create_blog.html', {'form': form})
#
#
# # Create your views here.
# # def blog_detail(request, blog_id):
# #     pass

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import myBlogs,myComments
from .forms import BlogForm,CommentForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def home(request):
    blogs = myBlogs.objects.all()
    return render(request, 'notes/home.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(myBlogs, id=blog_id)
    # return render(request, 'notes/blog_detail.html', {'blog': blog})
    comments = myComments.objects.filter(blog=blog).order_by('-created_date')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.author = request.user
                comment.save()
                return redirect('blog_detail', blog_id=blog.id)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'notes/blog_detail.html', {
        'blog': blog,
        'comments': comments,
        'form': form
    })


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    return render(request, 'notes/login.html')  # <-- Missing GET handler added


def logout_view(request):
    auth_logout(request)
    return render(request, "notes/logout.html")


@login_required(login_url='login')
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'notes/create_blog.html', {'form': form})

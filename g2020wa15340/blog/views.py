from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django import db
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url= '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# @login_required
# def home(request):
#     data = {
#         'posts' : Post.objects.all()
#     }
#     print("Printing data from the home function")
#     return render(request, 'blog/home.html', context=data)
    
def about(request):
    
    print("Loading About page!")
    return render(request, 'blog/about.html', {'title': 'About'})
    # HttpResponse("<h1>About Page!!!</h1>")
    
    



# Posts = [
#         {
#             'Title' : 'Post 1',
#             'Content' : 'Hi, This is the 1st post!',
#             'Author' : 'John Doe',
#             'Date_Posted': '5th Aug 2024'
#         },
#         {
#             'Title' : 'Post 2',
#             'Content' : 'Hi, This is the 1st post2!',
#             'Author' : 'Manipal Singh',
#             'Date_Posted': '4th Aug 2024'
#         }
#     ]
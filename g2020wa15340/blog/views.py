from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import db
from .models import Post

# Create your views here.

@login_required
def home(request):
    data = {
        'posts' : Post.objects.all()
    }
    print("Printing data from the home function")
    return render(request, 'blog/home.html', context=data)
    
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
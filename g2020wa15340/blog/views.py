from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

Posts = [
        {
            'Title' : 'Post 1',
            'Content' : 'Hi, This is the 1st post!',
            'Author' : 'John Doe',
            'Date_Posted': '5th Aug 2024'
        },
        {
            'Title' : 'Post 2',
            'Content' : 'Hi, This is the 1st post2!',
            'Author' : 'Manipal Singh',
            'Date_Posted': '4th Aug 2024'
        }
    ]

def home(request):
    data = {
        'posts' : Posts
    }
    print("Printing data from the home function")
    return render(request, 'blog/home.html', context=data)
    
def about(request):
    
    print("Loading About page!")
    return render(request, 'blog/about.html', {'title': 'About'})
    # HttpResponse("<h1>About Page!!!</h1>")
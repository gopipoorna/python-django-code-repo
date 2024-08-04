This is to record all the commands that we used in all days
DAY 1
Install Django framework using Python

Here, we have created a Repository in the CodeCommit Serverice in AWS and created 2 branches master(prod) and dev.

We will develop our code in the dev branch and commit the changes in it.

We will clone the repo and automatically, we will have our branches in it.

By default we will have the git installed in the instance.

We will use git commands get the repo

> git clone <repo_https_link>

In the git cloned directory, let's create a virtual environment

We have to create a virtual environment using Python3 commands

let's see these commands to create a virtual environment

> python3 -m venv <virtual_env_name> 

Here, we have created the virtual environment with the name django-venv

Now, let's activate the virtual environment

> source django-venv/bin/activate

This will activate the virtual environment

What is this virtual environment?

Virtual Environment is used to bundle up the modules required to our application in a folder, where our Virtual environment is there and our application will also be
using these modules in the application. Through this we can be able to deploy our application anywhere with the modules that is used by the application.

once activate the virtual environment, we will install the Django framework using pip.

> pip install django

Now, let's start the project using Django

> django-admin startproject <project-name>

now, let's use the dev branch,

> git checkout dev

If the branch doesn't exist, then run this, the below command will create a branch

> git branch <branch-name>

then run the git checkout command to go to dev branch

Now, create a app in the project.

> django-admin startapp <app-name>

Now, we have successfully created a django project and an app in it.

to check the django version

> python3 -m django --version

If you run the below, you can see all the subcommands of django.

> django-admin 

We can verify the project that we created just now, using the below command.

> python3 manage.py runserver (optional) <ip>:<port>

This will run the server, we also need to add the IP's in the allowed hosts in the settings.py file.

Then Cloud9 is compatible of creating the URL for the test purpose.

When we run the application using the above command, then automatically the application will start and runs on the localhost:8000 by default,

we can override this by using the ip address and the port in it. 

Django have a feature of creating multiple applciations without less dependency and we can also put these apps in other projects as well.

We can now create an app here.

There are 2 ways we can create an app, both will work

> django-admin startapp <app-name>

> python3 manage.py startapp <app-name>

Django Works in MVT -  Model Views Template 

Models - These are the tables or Blueprints of the data.

Views - These are the Controller, used to post or get the data from the Templates.

Templates - These are used to create HTML pages and used.

And by default Django app will create templates, views and models python files, while starting an app.

Now, let's jump into the actual code

Once, the app is created, let's create some templates

open, the views.py file in the blog directory.

Now, import the HttpResponse from the django.http

code-snippet:

<
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello World!!</h1>")
    
>

Now, let's create a urls.py file in the app directory and add the below lines there

and add the default import from the urls.py file in the Project directory

By using urls.py file, we can route the traffic and also create routes easily

code-snippet:
<
from django.urls import path, include
from . import views

urlpatterns = [
    path("app/", views.<fun_name>, name="app-home"),
    ......
]
>

Now, we can also add this under the urls.py file in the project file

code-snippet:

<
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<app>.urls')),
]
>

As we know, we can't type the whole HTML code in the HTTPResponse in the function to simplfy that we can use Render function

We can also pass the HTML pages in these views, for that we need to use the render function.

So, we are creating a templates directory under the app directory

By default, Django will look for the templates folder in every app directory.

So, we can create the html templates required for our application.

Now, we need to render the HTML Template from the views, open apps.py file in the app directory and copy the class name

and open settings.py in the Project directory and add required line in the installed apps.

Here, we are adding the app in the settings.py from the blog->apps.py->BlogConfig

code-snippet:
<
allowed_apps=[
    'blog.apps.BlogConfig',
    .....
]
>

We need to add this line, so that apps will get to know that templates folder has the html pages.

Now, to add the html pages from the views, we can use the

code-snippet:
<
def home(request):
    return render(request, 'blog/home.html') ->in 2nd parameter "Under templates -> app -> html page
>

Now, how to pass the data into the html page

For that, we have a parameter called context.

code-snippet:
<
def home(request):
    return render(request, 'blog/home.html', context=<dictionary>)
>


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

Day - 2:

Let's pass some demo data into the HTML Template using views.py

The data that we are passing to the context parameter to the HTML page must be a dictionary type. 

Through this, we can use that data by Jinja 

code-snippet:

<
<body>
    <h1>Blog Home!!</h1>
    {% for post in posts %} 
        <h1>{{post.Title}}</h1>
        <p> By {{post.Author}} posted on {{post.Date_Posted}}</p>
        <p>{{post.Content}}</p>
    {% endfor %}
</body>
>


Usually, all our webpages have the common UI, and so if we wanna make changes we can make changes easily from one place and it will reflect in all the web pages, 

to do this, we have to create a default webpage and inherit this default web page in all the web pages.

We can use this by having the below code in the default page

code-snippet:
<
{% block <any-name> %}
{% endblock %}
>

Now, we need to inherit this to all the pages in our application

To do this,

We can use the 

code-snippet:
<
{% extends 'path' %}
{% block <name-used-in-default-template> %}
{% endblock <name-used-in-default-template> %}
>

In Django, the static files are located under the static folder 

TO add thee static files, we need to add the

code-snippet:
<
{% load static %}
>

and we inherit the properties of these static files.

Day-3:

Django, by default comes with the Administration console, which is used to create and manage users.

You can find the admin page under 'admin/' route after the IP/URL.

To use this, we should have a superuser, this superuser can be access the admin console and create and manage users, groups and roles.

But, if you try to create a superuser from the CLI, it won't work because because, we haven't migrated the apps.

Migrations are nothing but used to create DB tables and modify the DB tables.

These all migrations are stored under the migrations folder with the versions.

Now, let's migrate and create the super user using the CLI Commands

code-snippet:
<
$python3 manage.py migrate
$python3 manage.py createsuperuser 
>

And when you are trying to access the application from the URL or any https site then it won't work because, CSRF (Cross-Site-Request-Forgery) Token will retrict by default
you can see more info in - https://docs.djangoproject.com/en/4.2/ref/csrf/

To access this site, then we need to add the below variable in the Settings.py file
and also make sure the list data should contain, either http/https

<
CSRF_TRUSTED_ORIGINS=['https://*.amazonaws.com']
>

Django uses models to create and manage the data tables.

By default Django uses sqlite3 to store the data, we can change it based on the environment.

Now, let's use the models to create the tables and store the data in the tables.

Here, we have created a model under models.py file.

Now, we have to migrate the changes to see the differences and to apply them into the application.

And likewise, we can also see this code under the App->Migrations->migration_number

Here, all the details can be seen.

Now, let's see, how we can see the raw SQL code for the same to create a table from the model.

For this, we have to go to CLI and the required parameters are the app-name, and migration number

<
$ python3 manage.py sqlmigrate blog <0001>
>

Now, after this, we can use Django-shell to work with the models interatively.

code-snippet:
CLI
<
$ python3 manage.py shell
>

Usually, the models can be found in the 'django.contrib.auth.models import User'

Now, let's access our models from here

let's import our models from the app

<
from app import models
from django.contrib.auth.models import User
# to filter the data
User.objects.all()
User.objects.filter(name="")
User.objects.get(id=1)
User.objects.first()

# we can add data to the table by using the classes in the models
m1 = model(data)
m1.save()

# by using save, we can insert or update the data
>

https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#date

From the admin GUI, we can't see the models here but to see the models here, we have to register them in the admin.py file in the app directory

to do that we have to add the below line

<
from .models import class_name

admin.site.register(class_name)
>

User Registration using Django:

For this, let's create a new app to use the UserRegistration and login and logout.

<
$ django-admin startapp users
>

after this add this app in the settings.py file in the project

<
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
]
>

Usually, whenever the user is registering to our Application, we may need to do some validations.

To do this we have to create an view and we can use some default forms that exists in Django.

Usually, the classes will acts as a HTML template in Django

Now, let's add these forms.

To do this, we have to import the UserCreationForm from the django.contrib.auth.forms

This will give us the flexibility to add users into the application.

Now, take this instance and add the form.

You may check the code in Users->views.py file

Now, we have to pass this forms into the html template, and you may check the templates in the users for this

But, as we are using the default forms provided by Django, we are not seeing the firstname, lastname and email fields in the Registration page

to get this, we have to do some modifications in the UserCreationForm form, for this, we are creating a forms.py file and inherit the UserCreationForm

and modify it as per your requirement

Go through the forms.py file in the Users directory.

Now, import that custom class into the views.py and update it, now we can be able to see these fields.

Now, how to add the created user to the DB.

Simply use .save() method and the user will be created and saved to the DB.

Now, the UI is not so good, we want to add the design to our UI.

For this we have Crispy forms, which is used to fetch CSS from Bootstrap, tailwind, or anything.

We have to install it first, let's install it.

<
$ pip install django-crispy-forms
>

after installing it, we need to add this crispy forms to the apps in settings.py file.

Now, we need to also tell the django-crispy-forms to use the bootstrap, for this, we can simply add the 

<
CRISPY_TEMPLATE_PACK = 'bootstrap5'/'tailwind'
>

add the tag at the top of the html page

<
{% load crispy_forms_tags %}

and also in the form data tag

{{ form | crispy }}
>

Now, we have to use the bootstrap5, for this we also need to install the crispy-bootstrap5

and add it to the apps 

<
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
>

Now, reload the page and the design will change automatically.

Now, let's add the login and logout functionality

for this, we are adding the 2 more routes in the urls.py file in the Users application

and the methods we are taking directly from the django.contrib.auth.views, we are importing 

<
from django.contrib.auth import views

    path("login/", views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path("logout/", views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
>

by default the route will look for the login and logout templates in the default folder, we need to change this by adding the template_name parameter in the pattern

and also we need to add a few paths in the settings.py file to route the traffic back to these urls.

<
LOGIN_REDIRECT_URL = 'blog-home'

LOGIN_URL = 'user-login'
>

So, when the authenticated user tries to look some data then it will automatically redirect to the LOGIN_REDIRECT_URL page

When the un-authenticated user tries to login then automatically login to user-login page

We can also restrict the un-authenticated users to access content by adding the decorators 

<
from django.contrib.auth.decorators import login_required

@login_required
def fun():
    pass
>

We just need to add this decorators, and then the user must be authenticated to access the content.


Adding the Profile and feature to modify the username and other fields.

Usually, django User table doesn't have the profile picture option,

so, we are adding here by creating a new model and making a one to one relationship between the tables

We need to add the ImageField to add the user.

We also need Pillow module, to use the image field.

We are using a separate model called Profile, to see and update the profile of the user, for this we have created a model, which will be in a onetoone relationship
with the User model, this will be having the extra field called image, which will store the image and also have the default image in it.

Now, we have create a Profile model and migrated it.

Now, we will be passing this to the profile template using the views.

=======================================================================

Usually, we will face the issue that the image is not showing in the Profile, even though the path is correct.

For this, if we are using different apps, we are creating a MEDIA_URL and MEDIA directory to store our images but here,

We have to extend it with the urlpatterns, and this need to be done in the project_directory, where setting.py file is there.

In this directory open the urls.py file and add the extra line,

Open the project>urls.py file more info on this.

========================================================================

Now, once the functionality is added, you will observe that the image is still not showing for the user who has created at that instance.

This is because the Profile is not creating for the users all the time, to create this,

We have to use signals.py file and add the methods to trigger automatically to create a profile with the default image.

for this, create signals.py file in the users app, import the below modules.

<
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
>

Now, add the functionality by using the decorator receiver and pass the instances.

Open the signals.py file to get more clarity on this.

and also we have to add a function in the apps.py in the application directory

Once this is done, whenever any new user is created then Django is capable of creating a profile by default.

Now, let's add the functionality of modifying the user profile and picture with the certain length and width.

For this, we are creating a new forms in the users->forms.py file, 

Let's create a new forms, called updateUserProfile and UpdateUserForm.

Here, using these both classes, we can update the user profile.

now, let's create a new view and pass the data through it.

and use the required methods to update the data through the form.

Load the User and Profile models and using the requests.

Open the views for more breifing.

We also have to update the template for the same.

Day 5:

Let's create the Forms to create, update, delete posts in our application.

To do this, we are using class based views which comes default with the Django, by using these class based views,

We can get all our details.

For this, we have to import the class based views from the django.views.generic import CreateView, DetailView, DeleteView, UpdateView

We are using all these views to achieve the functionalities that we want.

So, we are creating and inheriting these generic views in our classes, this will help us in reducing the code and display the UI easily.

Now, you can see the views.py file to know more about this.

By default, these ClassBased views have the default templates, to use them we have to create the <app>/<model_viewtype>.html under our templates directory

To override these, we have to tell the ClassBased views to use the particular files.

You can get these more from the Errors itself.

We also have to add some more functions in the models and also in the details.

Day 6:

https://docs.djangoproject.com/en/5.0/topics/pagination/
Pagination, is nothing but adjusting the content into multiple pages, so that the content will spread out and adding page numbers to the content
For this we can use the views and in previous topics, we have used our ClassBased Views, by default the ListView will be having the pagination inheritance.
Through this we can add the parameter "paginate_by = <number>" under this class.
and we have to add the links to go to other pages, please go through the documentation or the go through the home.html page, you can find the process of adding links

Password reset using email, using the Django
For this, we have a few default views to add these routers, for this we just have to create the routes and the templates.

In this we have to add the below routes

<
path("password-reset/", views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
path("password-reset-done/", views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
path("password-reset-confirm/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
path("password-reset-complete/", views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
>

and also we have to create the corresponding templates as well for this.

and check the documentation for the same

documentation:

DEV:
https://docs.djangoproject.com/en/2.1/topics/email/#configuring-email-for-development
https://docs.djangoproject.com/en/5.1/topics/email/#configuring-email-for-development

Prod:
https://docs.djangoproject.com/en/5.1/topics/email/#


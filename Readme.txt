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

Auto-Logout after inactivity: https://pypi.org/project/django-auto-logout/

#########################################################################

Day:7

Deploying application into the server

Let's create a server in AWS for this and recommended is ubuntu.

Now, let's change the hostname of the server by

$ hostnamectl set-hostname <hostname>
$ hostname

Now, we also need to make changes in the /etc/hosts file as well

Open this file and add the server private IP of the machine and name you want

<
19.24.98.23 <host_name>
>

Now, let's add the user, to provide less privileges,

$ adduser <username>

Give the password and other details, which you wanna give.

We have to provide access to the user to use Sudo, we can do this by simply running the below command

$ adduser <username> sudo

##############

SSH Authentication: 

For this create a folder called ".ssh"

usually, when we are creating this folder, we have to create in this ways

$ mkdir -p ~/.ssh

Now, on your local machine, create a ssh key, for this go to your local machine cmd and run

$ ssh-keygen -t rsa -b 4096

Now, we can find this file in the default .ssh folder of your machine.

After finding the file, copy the public key file to the server under .ssh directory as authorized_keys

and change the permissions to 600/700 to all the files in the .ssh folder

$ chmod 600 .ssh/*

<
poorna:~/$ ll /home/ec2-user/.ssh/
total 20
-rw-------. 1 ec2-user ec2-user  991 Jul 31 12:47 authorized_keys
-rw-------. 1 ec2-user ec2-user 3414 Aug 12 05:41 id_rsa
-rw-r--r--. 1 ec2-user ec2-user  764 Aug 12 05:41 id_rsa.pub
-rw-------. 1 ec2-user ec2-user  828 Aug 12 05:43 known_hosts
-rw-r--r--. 1 ec2-user ec2-user   92 Aug 12 05:18 known_hosts.old
>

To enable ssh authentication in ubuntu/rpm based machines, we need to edit the ssh_config file under /etc/ssh/ssh_config

<
$ sudo vi /etc/ssh/sshd_config
>

Here we need to modify 2 things

1: Make the "PermitRootLogin" to "no"
<
$ PermitRootLogin no
>
2: Disable the password based authentication, for this uncomment the PasswordAuthentication and set it to no
<
$ PasswordAuthentication no
>

After this we need to restart the SSH service
<
$ sudo systemctl restart sshd
>

This will enable the ssh access 

===================================================

Now, let's install the ufw (uncomplicated firewall)

<
$ sudo apt install ufw -y
>

In traditional way, ufw is used to allow and deny traffic of the server.

But in Cloud environment we don't have this, but for understanding

we can allow the traffic using this

by running a few commands

<
sudo ufw allow default outgoing
sudo ufw deny default incoming
sudo ufw allow ssh
sudo ufw allow
>

Now, we have to add the requirements.txt file to bundle all the required packages under a file.

So that our deplpyment will know that what are all the packages are required.

We have generated by running the below command.

Make sure you are in your python virtual environment before running this command.

<
$ pip freeze > requirements.txt
>

now, login to the server and install the required packages like python3, python3 pip, python virtual environment

for this, login to the server and run

<
$ sudo apt install python3 -y
$ sudo apt install python3-pip -y
$ sudo apt install python3-venv
>

Now, let's create the python virtual environment

<
$ python3 -m venv <env_name>
$ source <env_name>/bin/activate
$ pip install -r requirements.txt
>

Now, the required files will be installed and available,

Now, in the prod environment, we need to make a few changes before deploying

1st things, will be static directory, we should be using the static directory for static files

for this create a static directory,

open settings.py file and add the

<
STATIC_ROOT = os.environ.join(BASE_DIR, "static")
>

And save the file and now, we have to run the below command to collect all the static files.

<
$ python3 manage.py collectstatic
>

After this start the server with the below command

<
$ python3 manage.py runserver 0.0.0.0:8000
>

Now, we would like to run our application through the web host like apache, Tomcat etc.,

For this we need MOD WSGI (Web Service Gateway Interface).

This will help the Web Server talk to application

Now, let's install it

<
$ sudo apt install apache2 apache2-utils ssl-cert libapache2-mod-wsgi-py3 -y
>

Now, go to /etc/apache2/sites-available

You can find a few files here

Now use the default conf file and copy with any name <any_name>.conf

and now, we have to add some configs under this 

<
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf

         Alias /static /home/ubuntu/python-django-code-repo/g2020wa15340/static
        <Directory /home/ubuntu/python-django-code-repo/g2020wa15340/static>
                Require all granted
        </Directory>

        Alias /media /home/ubuntu/python-django-code-repo/g2020wa15340/media
        <Directory /home/ubuntu/python-django-code-repo/g2020wa15340/media>
                Require all granted
        </Directory>

        <Directory /home/ubuntu/python-django-code-repo/g2020wa15340/g2020wa15340>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>
        WSGIPassAuthorization On
        WSGIScriptAlias / /home/ubuntu/python-django-code-repo/g2020wa15340/g2020wa15340/wsgi.py
        WSGIDaemonProcess g2020wa15340 python-path=/home/ubuntu/python-django-code-repo/g2020wa15340 python-home=/home/ubuntu/python-django-code-repo/g2020wa15340/venv
        WSGIProcessGroup g2020wa15340
</VirtualHost>
>

Here, we have copied and added these lines 

Static and Media home directory of the django

Wsgi.py file path

after adding all these 

we need to run some apache commands to make our application as the default site

<
$ sudo a2ensite <created_conf_file>.conf # to add our application in the apache server
$ sudo a2dissite 001_default.conf # to remove the default site from the apache server
$ chown :www-data /project_path
$ chown :www-data /project_path/media
$ chown :www-data /project_path/static
$ chmod 755 /home/<user>/
$ chown :www-data /project_path/project/dbsqlite3 # to read and write the db data
$ chmod 775 /project_path/project/dbsqlite3
>

Provide as many access as possible to the apache user and we can be able to access the site.

Now, test the application.

Troubleshooting notes:
https://forum.djangoproject.com/t/403-forbidden-apache2-you-dont-have-permission-to-access-this-resource/18709/3

RDS: 
username: blogapp
password: poorna1999

   
Ec2 instance user data:
 
#!/bin/bash
sudo apt update
sudo apt install ruby-full -y
sudo apt install wget
cd /home/ubuntu
sudo wget -P /home/ubuntu/ https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
sudo chmod +x /home/ubuntu/install
sudo /home/ubuntu/install auto > /tmp/logfile

since, we don't have any artifacts for our application, so we have to create a scripts, that are used to deploy our application, successfully.

For this, I have created the configuration folder and put all configuration files

apache conf file for application, 
before install and after install scripts for setting up configs in place and to invoke and setup the environment variables.
We are not using buildspec.yml file.
set_up_conf.py file for fetching the variables from SSM parameters and add to the .env file in the root folder of the project.

by this all the configs will be done.

To run the CI-CD pipelines successfully, we have to use the appspec.yml file, which is used for 

============================================================================================================
setting up the MySQL as the database 

for this, create an RDS in AWS in the same VPC and allow security groups to inbound the traffic from the ec2 instance

then install the mysqlclient library, this will be included in the requirements.txt file, so no for this after installing the mysqlclient

https://pypi.org/project/mysqlclient/ --> check this page for installing the mysqlclient

$ pip freeze >> requirements.txt

and this will add the mysqlclient library, 

then try to connect to the MySQL RDS from the development server, to do this from the terminal

$ mysql -h <RDS-ENDPOINT> -u admin -p 

then enter the password, if connectivity is successful then we can proceed, if not then check the Security groups once again.

Then, create a database in it with the name, you like by using the query,

$ create database <database_name>;
$ show databases;
$ exit;

Now, exit from the sql engine, now, add this stanza in the settings.py file.

--------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db-name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'host-name',
        'PORT': '3306',  # Default MySQL port
    }
}
--------------------------------------------------------------------------

Now, by using the manage.py file, try to make migrations

$ python3 manage.py makemigrations
$ python3 manage.py migrate

Now, our database connectivity is done and successful.

=======================================================================================

Let's write the testcases now.

For this, we will be using Selenium and Django test suite.

========================================================================

As per our requirements, we have to hide the sensitive data, especially when we push into the GitHub.

For this purpose, we are using SSM Parameter store and saving all the important keys and sensitive content in that and fetching from it.

For this, we have created a python file called set_up_conf.py file, which is used for appending the public IP of the machine and to fetch the 
SSM parameters from the AWS services and use it.

By this, we don't have to do anything in the server, when we initiate a webhook, from then the whole process will be complete and successful, without any manual intervention

This will help us to do the activity successful.

We are also initiating this script from the after_install.sh script, so that the process will be complete and successful.

For this we are using the module called - django-environ

$ pip install django-environ

Which by default checks the .env file in the project root directory, where all the Environmental variables will be stored for the applciation.

From this we are fetching the environment variables, for this, we have to import the following module and use it.

---------------------------------------------------------

import environ

env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

and we can import the data by simply giving the format

env("VARIABLE_NAME")

wherever you use.

Check the Settings.py file for more info.

==============================================================================

And we will face some issue when we try to start the application for this, we have to add the attribute in settings.py file - "SECURE_CROSS_ORIGIN_OPENER_POLICY=None"

This will help to open the site without any issues.

==============================================================================

Now, we have a constraint, which is when the user access the application from any of the server and uploads any media files like profile pics, then when he access any
other server he can't be able to access the image, so we have to use a centralized place, where the server should be able to access the content from s3 bucket not just
dependent on the server.

For this, we have to add this configuration in settings.py file.
and also save the .env file
before using this, we have to install the modules - django-storages and boto3 library for this
#########################################
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
########################################

Then set this up and also create a bot user for getting access key id and access key and once it is generated, add the CORS configuration at S3 bucket.

For this add the below configuration under the permissions>CORS
##############################################
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
############################################

This will help to fetch the data from the s3 bucket and also add the policy to the new IAM user to access the s3 bucket and objects in it.

###################################################

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": "*",
            "Resource": [
                "arn:aws:s3:::2020wa15340-blog-app",
                "arn:aws:s3:::2020wa15340-blog-app/*"
            ]
        }
    ]
}

#######################################################

And now we have a function in the profile model called "Save", to work we have to comment it, so the save will work predefinedly.

Now, we have to copy the data from the Media path to s3 bucket and also make sure to leave only static configuration from the settings.py file

#######################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

############################################

and comment out the Media configuration and now, this will be useful to store the profile pics in the S3 bucket.

We have also utilised the ec2 instance metadata, which will be useful to fetch the Public-IP of the ec2 instance dynamically and 

Assign it to the ALLOWED_HOSTS in settings.py file.

This will make the application work with the host name.

This all functionality we have given to the CI-CD, which will help us to automate the things dynamically.

##########################################################################

Make sure, after importing the modules, activate your virtual environment and freeze all the modules into the requirements.txt file.

==========================================================================

Let's set the favicon icon for the application, for this add the 

below line in the dafault.html file under the title 

<link ref="icon" href="{% static 'images/<image_name.ext>' %}"/>

and also make sure to add the images folder under the blog/static folder and then copy the image to this folder,

then automatically, when we run the collectstatic command, it will move the image to the actual static command.

and also make sure to update the collectstatic command with

python manage.py collectstatic --noprompt

This will make the application works with the latest static file.

=================================================================================

Now, what we have to do is to create test cases for everything and the selenium testcases.

for this we are going to use the py files in the tests.py file in all the applications.

For this, let's create a folder called tests in all the apps.

.env file
==========================================
DB_USER=admin
DB_NAME=blogapp
AWS_STORAGE_BUCKET_NAME=2020wa15340-blog-app
EC2_PUBLIC_IP=10.6.88.90
============================================

For testing purpose, we have created a test user

username = testuser
password = blog@123

Webdriver for Selenium ---> https://googlechromelabs.github.io/chrome-for-testing/#stable


Adding buildstage to test the test cases


======================================================================

Adding cloudwatch agent

wget https://amazoncloudwatch-agent-us-east-1.s3.us-east-1.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
wget https://amazoncloudwatch-agent-us-east-1.s3.us-east-1.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb.sig
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json


Finally, we have added the monitors to monitor the infrastructure.
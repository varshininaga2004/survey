# Public Survey Application

A Dynamic Public Survey application built with Python and Django framework, allowing admins to create and manage survey questions of their choices and users to submit their respective responses. And also provides the admin with the result of the survey in the graphical/readable format.

## Installation

### Prerequisites
- Python 3.x
- pip
- git

### Create a Django project
Navigate to the folder where you want to create the django project
~~~
django-admin startproject survey
cd survey
~~~

### Create and activate a virtual environment
~~~
python -m venv venv
venv\Scripts\activate
~~~

### Install the required dependencies
~~~
pip install -r requirements.txt
~~~

### Create a django app
~~~
python manage.py startapp <app-name>
~~~

### Migrate the models
~~~
python manage.py makemigrations
python manage.py migrate
~~~

### Running the applications
~~~
python manage.py runserver
~~~

## Git Commands

### Initiate and configure git repository locally
Navigate to the project root folder
~~~
git init
git branch -M main
git config --global user.name "<username>"
git config --global user.email "<email>"
~~~

### Adding and commiting the files
~~~
git add .
git commit -m "<commit-message>"
~~~

### Pushing the repo to the remote repository
Note: The remote repository name should be same as your root folder name
~~~
git remote add origin <git-repo-url>
git push -u origin main
~~~

### Cloning the remote repository into local
Navigate to the folder where you want to clone the django project
~~~
git clone <git-repo-url>
~~~

### Taking latest pull from remote repository
~~~
git fetch
git pull origin main
~~~
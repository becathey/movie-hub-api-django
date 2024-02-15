# Top Movies API

Top Movies API is a RESTful API that serves movie data. It is built with Django/Django REST Framework

## Clone the Repository

```
git clone https://github.com/becathey/top-movies-api-django
```

## Create & Activate a Virtual Environment

In the project directory, create and activate a virtual environment. For example:

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install the Dependencies

To install the dependencies, run:

```
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in root of project, and add a SECRET_KEY:

```
SECRET_KEY='<create-and-add-your-secret-key-here>'
```

The .env file should be added to a .gitignore file to protect your secret key.

## Apply Migrations

To apply the migrations to the database, run:

```
python manage.py migrate
```

## Create Superuser

To create a superuser account for login, run:

```
python manage.py createsuperuser
```

Enter username, email, and password.

## Run the App

To run the app in development mode, run:

```
python manage.py runserver
```

Open [http://localhost:8000/admin](http://localhost:8000/admin) in the browser, and add your movie data.

Open [http://localhost:8000/movies](http://localhost:8000/movies) in the browser to see your movies.

## Deploy the App

To learn how to make the application production-ready and to deploy it, see the Django documentation:

[How to Deploy Django](https://docs.djangoproject.com/en/4.1/howto/deployment/)

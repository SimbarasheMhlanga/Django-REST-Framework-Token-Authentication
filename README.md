
## Language

- Python v3.10.4

## Framework

- Django v4.0.5
- Djangorestframework v3.13.1

## Database

- SQLite





## API Reference

#### Authentication

```http
  REGISTER FOR AN ACCOUNT            POST                /account/register
  LOGIN WITH AN ACCOUNT              POST                /account/login
  LOGOUT FROM AN ACCOUNT             GET                 /account/logout
```
#### CRUD Parent Data

```http
   GET ALL PARENT DATA               GET                  /user/parent
   CREATE PARENT DATA                POST                 /user/parent


   RETRIEVE/MODIFY                   GET,
   INDIVIDUAL                     PUT,PATCH,              /user/parent/${pk}
   PARENT DATA                      DELETE
```

#### CRUD Child Data

```http
   GET ALL CHILD DATA                 GET                 /user/child
   CREATE CHILD DATA                  POST                /user/parent/${pk}/child/

   RETRIEVE/MODIFY                   GET,
   INDIVIDUAL                     PUT,PATCH,              /user/child/${id}
   CHILD DATA                       DELETE
```
#### Repsitory Structure

```

├─ crudoperations_app
│  ├─ admin.py
│  ├─ api
│  │  ├─ serializers.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ test_child_endpoints.py
│  ├─ test_models.py
│  ├─ test_parent_endpoints.py
│  ├─ views.py
│  └─ __init__.py
├─ datastore_app
│  ├─ asgi.py
│  ├─ mixins.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ py_client
│  └─ app.py
├─ README.md
├─ requirement.txt
└─ user_app
   ├─ admin.py
   ├─ api
   │  ├─ serializers.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ apps.py
   ├─ migrations
   │  └─ __init__.py
   ├─ models.py
   ├─ test_authentication.py
   ├─ views.py
   └─ __init__.py

```

## Installation
## Step 1 - Download and Install Python
- Download [python v3.10.4](https://www.python.org/downloads/release/python-3104/)
- Run the executable file as an administrator
- Add python path to environment variables
## Step 2 - Repository
- Clone the following [repository](https://github.com/mohammadjayeed/data_store_app_assignment.git),
```bash
  git clone  https://github.com/mohammadjayeed/data_store_app_assignment.git
```
## Step 3 - Virtual Environment
- Make a virtual environment with the following command
```bash
  python -m venv venv
```
-  Activate the virtual environment with the command
```bash
  venv/scripts/activate
```
## Step 4 - Dependencies
- Install dependencies
```bash
  pip install -r requirement.txt
```
## Step 5 - Migrations
- Run the following command which creates migrations based on models or change of models
```bash
  python manage.py makemigrations
```
- Run the following command to apply it to the database
```bash
  python manage.py migrate
```
## Step 6 - Superuser
- Run the following command to create a superuser to access admin panel by adding the required information. We will require username and password to login to the admin panel
```bash
  python manage.py createsuperuser
```
## Step 7 - Start App
- Start the application by typing the following command
```bash
  python manage.py runserver
```
## Step 8 - Testing the App
- Start the application by typing the following command
```bash
  python manage.py test
```
# Done !!
## Launching the Python Client
- We can use our python client to reach the endpoints and perform operations.
```bash
  python py_client/app.py
```
## Admin panel
- [URL](http://localhost:8000/admin/)
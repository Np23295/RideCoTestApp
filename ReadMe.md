ReadMe
========================

1. Setup Python
2. Setup Django
    * Check if django is already installed  `python3 -m django --version`
    *  Executing the project `python3 manage.py runserver`. For running on specific port `python manage.py runserver 8080` or `python manage.py runserver 0:8000` 


### Making Migration
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Creating an admin user[¶](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-an-admin-user)

First we’ll need to create a user who can login to the admin site. Run the following command:
```
$ python manage.py createsuperuser
```


Enter your desired username and press enter.


```
Username: admin
```


You will then be prompted for your desired email address:


```
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```


### Create System users who can select from map and share it

* Go to ``BASE_URL/admin`` and login with admin credentials.
* Go to Create User:
    * Required fields:
        * username
        * password
        * Staff member (Currently required, otherwise will need to over-ride the current default authentication system)
        * Add Permissions for CRUD of MAPS and to view USERS


### How it Works

* For Selecting point of interest, user needs to Login(Go to ``BASE_URL/admin`` for login).
* Click on list of MAPS to modify or add

* For Sharing the Point of interest, Select the user who can see.


### Limitations:

There are lot of limitations in the app.

1. User Roles can be defined in much better way. NO need to mark every user as Staff member
2. Maps Currently just allows selecting the co-ordinates. No information regarding the place or location. Third party libraries like google maps or openstreetmap can be used.
3. Currently the main functionality is nested too inside the app. 
4. As the UI is Django Templates, needs to customize media queries for Mobile responsiveness, but still it will not perform similar to native.
5. For the purpose of scaling, it currently does not have REST API which limits the scalability.
6. All of the sub applications can be individually configured for behaving as micro-service. Which will help out to scale from monolith.

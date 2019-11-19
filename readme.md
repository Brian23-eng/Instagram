# [InstaClone](https://instabran.herokuapp.com/)
## InstaClone is a simple clone of Instagram where users can create account, upload photos, comment on these photos
### Nov 17th, 2019
#### By **[Brian Omondi](https://github.com/brian23-eng)**

## Description
InstaClone allow users to upload photos,create an account, comment on photos.





## BDD

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
|Navigate to website | Click on a profile| User profile is displayed |
| Post Image | Click on the post image icon| User redirected to the post image form where they can post the image and write a caption |
| Search | Search users| Redirects you to user's profile page |
| Comment | Click on the comment icon | Takes the user to the page where you can write and post a comment about the specific image|


## Live link

https://instabran.herokuapp.com/

## Set-up and Installation

### Prerequsites
    - Python 3.6
    - Ubuntu software
    - Django

### Clone the Repo
Run the following command on the terminal:
`https://github.com/Brian23-eng/Instagram.git`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Create a database

```
psql

CREATE DATABASE insta;

```

### .env file

```
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'

```

## Run initial Migration
```
python3.6 manage.py makemigrations instagram
python3.6 manage.py migrate

```


### Running the app in development
In the same terminal type:
`python3 manage.py runserver`

Open the browser on `http://localhost:8000/`

## Known bugs

```None so far but i'll be glad to be communicated to if there is one ```


## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Animate CSS
    - Heroku
    - Django2
    - Postgresql

## Support and contact details
Contact me on b.odhiambo.bo@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Brian Omondi**

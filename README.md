# Authentication
A jwt authentication that uses access token when logging in a user

## Motivation
Authentication is a basic user registration backend project. 

### Virtual environment setup
#### Create virtual environment

```
python3 -m venv venv
```

#### Activate virtual environment

```
source venv/bin/activate
```

#### Environment variables setup

Create a .env file in the root directory and add the following variables in the .env.example file.
Note

The default database is sqlite3 on local environment. If you want to use postgresql(or any other), then make sure you set the environment variables in the .env for the database as shown in the .env.example file so that the DB_IS_AVAIL variable in config.settings.local is set to True.

#### Install dependencies

```
pip install requirements.txt
```

#### Run migrations

If you don't set the DB variables in the .env file, then the default database is sqlite3.
```
python manage.py migrate
```
#### Run local server
```
python manage.py runserver
```
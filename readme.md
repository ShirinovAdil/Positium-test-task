
# Setup

1. Create python virtual environment by running: 
`pip install -r requirements.txt`
2. Activate virtual env by running the file `venv/Scripts/activate.bat`
3. Run `pip install mysqlclient`
4. In `positium/settings.py` find database settings and add your database credentials
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'database_name',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'database_host',
            'PORT': '3306',
        }
    }
    ```
5. Migrate database by running first `python manage.py makemigrations gisAPI` and then run `python manage.py migrate gisAPI`
6. Prepopulate the database with the data by running the queries in `main_gisAPI_country.sql` file
7. Run the Django server: `python manage.py runserver` and test the app navigating to `localhost:8000/api/v1/country` or `localhost:8000/home`
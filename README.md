# JFTApp (Just For Today Application): A Django Application

This is the source code for the [*Just For Today Web Application*](https://justfortoday.pythonanywhere.com/).

## Requirements:
**Python==3.5** or later version  
**Django==1.11.0** or later version  

## Dependency:
[*jftapp_extras*](https://github.com/bycomputing/jftapp_extras.git/) for custom Django template filters

## Installation:
1. Create your project and download source.  
    `$ django-admin.py startproject yoursite`  
    `$ cd yoursite`  
    `$ git clone https://github.com/bycomputing/jftapp`  
    `$ git clone https://github.com/bycomputing/jftapp_extras`  

2. Configure your `urls.py` to include `jftapp.urls`.
    ~~~~
    from django.conf.urls import url, include
    from django.contrib import admin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^jft/', include('jftapp.urls')),
    ]
    ~~~~
    **Note:** Don't forget to `import include`
 
3. Install the model. Edit your `settings.py` and add `jftapp` and `jftapp_extras` to your `INSTALLED_APPS`.
    ~~~~
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'jftapp',
        'jftapp_extras',
    ]
    ~~~~

4. Configure your database or leave the default SQLite.

5. Sync database.  
   `$ python manage.py makemigrations jftapp`  
   `$ python manage.py migrate`  

6. Populate the database.  
   `$ cd jftapp/tools`  
   `$ python populate.py --settings=yoursite.settings`  

7. You will be able to view your JFT Django App by visiting your IP plus the URL `/jft/`.

# Just for Today application
A Django application that adds a Just for Today reading by NA to your Django website.

###Requirements:

 - [Just for Today Daily Meditation Subscriptions](http://www.na.org/?ID=jft-sub)
 - [jftapp_extras](https://github.com/jftreading/jftapp_extras)
 - Python 2
 - Django version 1.3.7

###Installation:

Simply add `jftapp` and `jftapp_extras` to your INSTALLED_APPS and configure your urls.py:

        urlpatterns = patterns('',
            # Examples:
            # url(r'^$', 'mysite.views.home', name='home'),
            # url(r'^mysite/', include('mysite.foo.urls')),
        
            # Uncomment the admin/doc line below to enable admin 
    documentation:
            # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
            # Uncomment the next line to enable the admin:
            # url(r'^admin/', include(admin.site.urls)),
            url(r'^jft/', include('mysite.jftapp.urls')), # Assuming mysite is your project's name.

Update runscript.py with your email login information. If you haven't 
changed the default download_path, make sure to make a downloads 
directory inside jftapp.

Download all emails with:

    $ python runscript.py -a

If you don't have all the emails yet, you can create a scheduled task 
which runs: 

    $ python runscript.py # without the -a argument

adjusted to the time an email subscription would be received.

###Usage:

To view Today's reading:

*mysite.com/jft*

or to search for a specific date:

*mysite.com/jft/jan/11*



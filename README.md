#django-skeleton
This is a [project template]() for Django 1.6+ projects. It's based on a lot of ideas from [Two Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-6/), [12 factor](http://12factor.net/) methodology, and plays particularly well with [Heroku](http://heroku.com/) (though doesn't require deploying to Heroku).

I highly recommend reading [Two Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-6) for a number of reasons, starting with a understanding everything happening here.

This skeleton installs a few handy apps alongside Django, including:

* [South](http://south.aeracode.org) for database migrations
* [dj-database-url](https://github.com/kennethreitz/dj-database-url) for easier database configuration
* [dj-static](https://github.com/kennethreitz/dj-static) for serving static assets in production
* [braces](http://django-braces.readthedocs.org/en/latest/index.html) for working with class-based views
* [model utils](https://django-model-utils.readthedocs.org/en/latest/) add a couple of handy model utilities
* [psycopg2](http://initd.org/psycopg/) for connecting to Postgres

## Setting up your environment
The easiest thing to do is use [Vagrant](http://www.vagrantup.com) to build a box configured to run Django apps. Here's a [Vagrantfile and provision.sh](https://gist.github.com/jimray/8925795) that will build a box with Python 2.7.6 and 3.3.3, virtualenv, virtualenvwrapper, Postgres, and the Heroku toolbelt. Download those into an empty folder.

```
$vagrant up
$vagrant ssh
```

Once you ssh into the vagrant virtual machine, a virtualenv will already be configured for you called `django`, a Postgres database will already be created called `django`.

Or, you can set up virtualenv[wrapper] on your local machine.

## Setting up a project
There's a bit of a catch-22 here where you need to install Django before you can set everything else up.

```
pip install Django==1.6.2
```

Now, start a new project

```
django-admin.py startproject --template=https://github.com/jimray/django-skeleton/archive/master.zip --name=Procfile,Procfile.local --extension=py,html,md
```

For local development, install the dependencies defined in the local requirements file.

```
pip install -r requirements/local.txt
```

For production, use `requirements/production`. Since Heroku looks at `requirements.txt` in the root, it points here.

## Acknowledgements
This skeleton borrows liberally from the [Two Scoops project template](https://github.com/twoscoops/django-twoscoops-project). Again, I highly recommend [Two Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-6) for more on Django best practices.
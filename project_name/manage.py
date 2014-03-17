#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Instead of setting the DJANGO_SETTINGS_MODULE here, we set it as an
    # environment variable. Set in .env for local
    # For heroku, set the variable like so
    # heroku config:set DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
    #
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
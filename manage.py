#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.getenv('WAGTAIL_ENV'):
        wagtailenv = "lesgv.settings." + os.getenv('WAGTAIL_ENV')
    else:
        wagtailenv = "lesgv.settings.dev" 

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lesgv.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

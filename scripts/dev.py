#!/usr/bin/env python
"""
Development helper scripts for SantheCTF
"""

import os
import sys
import subprocess


def runserver():
    """Run the Django development server"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "santheCTF.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(["manage.py", "runserver"])


def populate_challenges():
    """Run the challenge population script"""
    script_path = os.path.join(os.path.dirname(__file__), "populate_challenges.py")
    subprocess.run([sys.executable, script_path], check=True)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "runserver":
            runserver()
        elif command == "populate":
            populate_challenges()
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    else:
        print("Available commands: runserver, populate")

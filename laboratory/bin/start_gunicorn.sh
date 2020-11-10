#!/bin/bash
source /home/max/lab/venv/bin/activate
exec gunicorn -c "/home/maxim/lab/laboratory/laboratory/gunicorn_config.py" laboratory.wsgi

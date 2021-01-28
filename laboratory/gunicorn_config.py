command = '/home/maxim/lab/venv/bin/gunicorn'
pythonpath = '/home/max/lab/laboratory/laboratory'
bind = '127.0.0.1:8001'
workers = 3
user = 'maxim'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=laboratory.settings'

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

bind = os.getenv("GUNICORN_BIND", "unix:/run/adsmart/gunicorn.sock")
workers = int(os.getenv("GUNICORN_WORKERS", "3"))
timeout = int(os.getenv("GUNICORN_TIMEOUT", "30"))

chdir = BASE_DIR
wsgi_app = "adsmart.wsgi:application"

accesslog = "-"
errorlog = "-"
loglevel = os.getenv("GUNICORN_LOGLEVEL", "info")




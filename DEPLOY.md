# Деплой ADSmart

## Требования

- Python 3.11+
- PostgreSQL (prod) или SQLite (dev)
- `pip install -r requirements.txt`

## Переменные окружения (.env)

```
SECRET_KEY=...
DEBUG=0
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://USER:PASSWORD@HOST:5432/DBNAME
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

## Локальный запуск

```bash
python manage.py migrate
python manage.py runserver
```

## Продакшен (gunicorn + nginx)

- `deploy/gunicorn.conf.py` — конфиг gunicorn
- `deploy/nginx/adsmart.conf` — конфиг nginx
- `deploy/systemd/gunicorn.service` — systemd unit
- `deploy/systemd/gunicorn.socket` — socket

## Сбор статики

```bash
python manage.py collectstatic --noinput
```

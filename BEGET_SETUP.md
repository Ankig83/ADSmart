# Установка ADSmart на Beget VPS

Инструкция по развёртыванию проекта на Beget VPS (IP: 109.172.46.145, путь: `/var/www/ADSmart/`).

---

## 1. Подготовка сервера

```bash
# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка Python 3.11+, pip, venv, PostgreSQL, nginx
sudo apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib nginx
```

---

## 2. PostgreSQL: создание БД и пользователя

```bash
# Войти в PostgreSQL
sudo -u postgres psql
```

В консоли PostgreSQL:

```sql
-- Создать пользователя (замените PASSWORD на свой пароль)
CREATE USER adsmart_user WITH PASSWORD 'YOUR_DB_PASSWORD';

-- Создать базу данных
CREATE DATABASE adsmart_db OWNER adsmart_user;

-- Права
GRANT ALL PRIVILEGES ON DATABASE adsmart_db TO adsmart_user;
ALTER USER adsmart_user CREATEDB;

-- Выход
\q
```

**Формат DATABASE_URL:**
```
postgres://adsmart_user:YOUR_DB_PASSWORD@localhost:5432/adsmart_db
```

---

## 3. Проект

```bash
# Каталог проекта
cd /var/www
sudo mkdir -p ADSmart
sudo chown $USER:$USER ADSmart
cd ADSmart

# Склонировать репозиторий (или загрузить файлы)
git clone https://github.com/Ankig83/ADSmart_deploy.git .
# или git pull, если уже клонировано
```

---

## 4. Python-окружение и зависимости

```bash
cd /var/www/ADSmart

# Виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate  # Linux
# Windows: .venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```

**requirements.txt** (уже в проекте):
```
Django
python-dotenv
dj-database-url
gunicorn==22.0.0
psycopg[binary]
whitenoise
requests
```

---

## 5. Файл .env (продакшен)

Создайте `/var/www/ADSmart/.env`:

```env
# Django
SECRET_KEY=СГЕНЕРИРУЙТЕ_ДЛИННЫЙ_СЛУЧАЙНЫЙ_КЛЮЧ_50_СИМВОЛОВ
DEBUG=0
ALLOWED_HOSTS=109.172.46.145,localhost,127.0.0.1

# База данных PostgreSQL
DATABASE_URL=postgres://adsmart_user:YOUR_DB_PASSWORD@localhost:5432/adsmart_db

# Telegram (заявки с форм)
TELEGRAM_BOT_TOKEN=ваш_токен_от_BotFather
TELEGRAM_CHAT_ID=ваш_chat_id

# Опционально
LANGUAGE_CODE=ru-ru
TIME_ZONE=Europe/Moscow
```

**Генерация SECRET_KEY:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 6. settings.py для продакшена

Проект уже использует переменные окружения. В продакшене убедитесь, что в `.env` указано:

- `DEBUG=0`
- `ALLOWED_HOSTS` с вашим IP и доменом
- `DATABASE_URL` — строка подключения к PostgreSQL
- `TELEGRAM_BOT_TOKEN` и `TELEGRAM_CHAT_ID`

При необходимости добавьте в `adsmart/settings.py` в конец:

```python
# Production only (если нужны строгие настройки)
if not DEBUG:
    SECURE_SSL_REDIRECT = False  # True, если есть HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

Для работы по IP без домена эти опции можно оставить как есть — `settings.py` уже подставляет значения из `.env`.

---

## 7. Миграции и статика

```bash
cd /var/www/ADSmart
source .venv/bin/activate

# Миграции
python manage.py migrate

# Создать суперпользователя (админка)
python manage.py createsuperuser

# Собрать статику
python manage.py collectstatic --noinput
```

---

## 8. Gunicorn

### Конфиг: `/var/www/ADSmart/deploy/gunicorn.conf.py`

Используется существующий конфиг. Проверьте пути:

- `chdir` = `/var/www/ADSmart`
- `bind` = `unix:/run/adsmart/gunicorn.sock`

Создайте каталог для сокета:

```bash
sudo mkdir -p /run/adsmart
sudo chown www-data:www-data /run/adsmart
```

### systemd: gunicorn.service

Файл: `/etc/systemd/system/gunicorn-adsmart.service`

```ini
[Unit]
Description=gunicorn daemon (adsmart)
Requires=gunicorn-adsmart.socket
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data

WorkingDirectory=/var/www/ADSmart
EnvironmentFile=/var/www/ADSmart/.env
Environment="PATH=/var/www/ADSmart/.venv/bin"

ExecStart=/var/www/ADSmart/.venv/bin/gunicorn --config /var/www/ADSmart/deploy/gunicorn.conf.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

### systemd: gunicorn.socket

Файл: `/etc/systemd/system/gunicorn-adsmart.socket`

```ini
[Unit]
Description=gunicorn socket (adsmart)

[Socket]
ListenStream=/run/adsmart/gunicorn.sock
SocketUser=www-data
SocketGroup=www-data
SocketMode=0660

[Install]
WantedBy=sockets.target
```

### Установка systemd-юнитов

```bash
sudo cp /var/www/ADSmart/deploy/systemd/gunicorn.service /etc/systemd/system/gunicorn-adsmart.service
sudo cp /var/www/ADSmart/deploy/systemd/gunicorn.socket /etc/systemd/system/gunicorn-adsmart.socket
```

Исправьте пути в `/etc/systemd/system/gunicorn-adsmart.service`:
- `WorkingDirectory=/var/www/ADSmart`
- `EnvironmentFile=/var/www/ADSmart/.env`
- `ExecStart=/var/www/ADSmart/.venv/bin/gunicorn --config /var/www/ADSmart/deploy/gunicorn.conf.py`

```bash
# Права на проект для www-data
sudo chown -R www-data:www-data /var/www/ADSmart

# Запуск
sudo systemctl daemon-reload
sudo systemctl enable gunicorn-adsmart.socket gunicorn-adsmart.service
sudo systemctl start gunicorn-adsmart.socket
sudo systemctl start gunicorn-adsmart.service
sudo systemctl status gunicorn-adsmart.service
```

---

## 9. Nginx

### Конфиг: `/etc/nginx/sites-available/adsmart`

```nginx
server {
    listen 80;
    server_name 109.172.46.145;

    client_max_body_size 20m;

    location /static/ {
        alias /var/www/ADSmart/staticfiles/;
        expires 7d;
        add_header Cache-Control "public";
    }

    location /media/ {
        alias /var/www/ADSmart/media/;
        expires 7d;
        add_header Cache-Control "public";
    }

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_pass http://unix:/run/adsmart/gunicorn.sock;
    }
}
```

### Подключение и перезапуск

```bash
sudo ln -sf /etc/nginx/sites-available/adsmart /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## 10. Проверка

- Сайт: http://109.172.46.145/
- Админка: http://109.172.46.145/admin/
- Формы: отправить тестовую заявку и проверить приход в Telegram

---

## Краткий чеклист

1. PostgreSQL: создать БД и пользователя
2. `.env` с `SECRET_KEY`, `DATABASE_URL`, `TELEGRAM_*`, `DEBUG=0`, `ALLOWED_HOSTS`
3. `python manage.py migrate` и `createsuperuser`
4. `python manage.py collectstatic --noinput`
5. systemd: gunicorn socket + service
6. Nginx: конфиг и `sites-enabled`
7. Права `www-data` на `/var/www/ADSmart`

---

## Команды для обновления

```bash
cd /var/www/ADSmart
git pull
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn-adsmart.service
```

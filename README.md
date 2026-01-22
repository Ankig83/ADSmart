## ADSmart — Django + чистый HTML/CSS (pixel-perfect под Figma)

Проект подготовлен под перенос дизайна из **Figma Dev Mode**: страницы собираются из include-компонентов (Django Templates), стили — **чистый CSS** с design tokens (`tokens.css`), JS — минимальный vanilla.

### Быстрый старт (dev)

```bash
cd /home/user/PycharmProjects/ADSmart
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Открыть:
- **Home**: `/`
- **Styleguide**: `/styleguide/`
- **Health**: `/health/`
- **Admin**: `/admin/`

### Переменные окружения

Смотри `.env.example`.

- **sqlite (dev по умолчанию)**: оставь `DATABASE_URL` пустым
- **Postgres (prod)**: выставь `DATABASE_URL=postgres://...`

### Структура проекта

#### Django apps
- `pages/`: страницы сайта (views/urls)
- `components/`: “библиотека” шаблонных компонентов (только templates/стили/JS, без моделей)
- `core/`: настройки, context processors, template tags, утилиты

#### Templates (Django Templates)
- `templates/base.html`: базовый layout (head/meta, CSS/JS, header/footer slots)
- `templates/pages/*.html`: страницы, собираются из include-компонентов
- `templates/components/*.html`: атомарные компоненты (button/input/card/section/nav/badge/modal/toast)

#### Static (без Bootstrap/Tailwind)
- `static/css/tokens.css`: design tokens (CSS variables)
- `static/css/base.css`: reset + базовая типографика + контейнер/грид
- `static/css/components/*.css`: стили компонентов
- `static/css/pages/*.css`: точечные правки страниц
- `static/js/app.js`: меню/модалка/тосты (vanilla)

### Как добавить новую страницу

1) **Шаблон**: создай `templates/pages/<name>.html` (обычно `extends "base.html"`)
2) **View**: добавь функцию в `pages/views.py`
3) **URL**: добавь `path("<name>/", views.<view>, name="<name>")` в `pages/urls.py`
4) (опционально) **Page CSS**: `static/css/pages/<name>.css` и подключи через `{% block page_css %}`

### Как добавить компонент

1) **Шаблон**: `templates/components/<component>.html`
2) **Стили**: `static/css/components/<component>.css`
3) **Подключение**:
   - `templates/base.html` уже подключает базовый набор component CSS
   - новый компонент подключай там же или только на нужных страницах через `{% block page_css %}`

### Продакшн (gunicorn + systemd + nginx)

В репо лежат примеры:
- `deploy/gunicorn.conf.py`
- `deploy/systemd/gunicorn.socket`
- `deploy/systemd/gunicorn.service`
- `deploy/nginx/adsmart.conf`

#### Схема (пример)

- Код: `/srv/adsmart`
- venv: `/srv/adsmart/.venv`
- env: `/srv/adsmart/.env`
- статика: `/srv/adsmart/staticfiles` (после `collectstatic`)
- медиа: `/srv/adsmart/media`
- сокет: `/run/adsmart/gunicorn.sock`

#### Шаги (пример для Ubuntu)

1) Установи пакеты:

```bash
sudo apt update
sudo apt install -y python3-venv nginx
```

2) Залей код в `/srv/adsmart`, создай venv и зависимости:

```bash
cd /srv/adsmart
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

3) Создай `/srv/adsmart/.env` (как минимум `SECRET_KEY`, `DEBUG=0`, `ALLOWED_HOSTS`, `DATABASE_URL` для Postgres).

4) Миграции и статика:

```bash
source /srv/adsmart/.venv/bin/activate
python /srv/adsmart/manage.py migrate
python /srv/adsmart/manage.py collectstatic --noinput
```

5) systemd:

```bash
sudo mkdir -p /run/adsmart
sudo chown www-data:www-data /run/adsmart

sudo cp /srv/adsmart/deploy/systemd/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp /srv/adsmart/deploy/systemd/gunicorn.service /etc/systemd/system/gunicorn.service

sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn.socket
sudo systemctl restart gunicorn
```

6) nginx:

```bash
sudo cp /srv/adsmart/deploy/nginx/adsmart.conf /etc/nginx/sites-available/adsmart.conf
sudo ln -sf /etc/nginx/sites-available/adsmart.conf /etc/nginx/sites-enabled/adsmart.conf
sudo nginx -t
sudo systemctl reload nginx
```

7) Проверка деплоя:
- `curl -i http://example.com/health/` должен вернуть **200 OK**

### Figma Dev Mode → спецификация / экспорт ассетов

Без логина Figma часто не даёт **Inspect**. Поэтому есть два пути:

- **Manual**: смотри `docs/figma-spec.md` → раздел E (как экспортировать ассеты руками).
- **Auto (Figma API)**: если есть токен, можно выгрузить экспортируемые слои автоматом:

```bash
export FIGMA_TOKEN=...                # personal access token
export FIGMA_FILE_KEY=RgixkfQjBcvWPRvylxy0u8

# Dump JSON по node ids (можно подставить твои)
python scripts/figma_export.py dump --ids 140:4885 140:5405

# Или использовать список всех node ids из файла
python scripts/figma_export.py dump --ids-file design/figma_node_ids.txt

# Скачать exportable layers (svg/png) в static/assets/
python scripts/figma_export.py assets --ids 140:4885 --out static/assets --formats svg png --scale 2

# Или скачать ассеты для всех nodes из файла
python scripts/figma_export.py assets --ids-file design/figma_node_ids.txt --out static/assets --formats svg png --scale 2

# Скачать image fills (растровые ассеты по imageRef) в static/assets/images/
python scripts/figma_export.py imagefills --out design/figma-imagefills.json
python scripts/figma_export.py download-imagefills --fills design/figma-imagefills.json --plan design/figma-metrics.json
```

#### DEMO файл (Home / menu / hero)

Если переносим из `DEMO--Copy` (file key `St9lm1ybs5FOfA1GJBVvWW`) — смотри `docs/demo-home-spec.md`.



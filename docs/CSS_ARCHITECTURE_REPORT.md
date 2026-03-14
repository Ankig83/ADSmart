# CSS Architecture Report · ADSmart

Отчёт для фронт-верстальщика: структура CSS, брейкпоинты, стандартные блоки, возможные правки. **Обращаться после каждого запроса на правки.**

---

## 1. Общая архитектура

### 1.1 Поток подключения (base.html)

```
1. css_v2/main.css          — единая точка входа
2. {% block page_css %}     — страничные CSS
3. css_v2/base/hero-full-bleed.css
4. css_v2/base/desktop-1440-lock.css
5. css/components/demo-mobile-lock.css  — (сейчас пустой, только комментарии)
```

### 1.2 Mobile-first

- Стили по умолчанию — для мобилы.
- Усиление — через `@media (min-width: ...)`.
- Исключение: lock-файлы используют `@media (max-width: 833px)` для мобилы (отдельные правки).

### 1.3 Токены (tokens.css)

| Переменная | Значение | Описание |
|------------|----------|----------|
| `--bp-md` | 834px | Tablet start |
| `--bp-md-max` | 1439px | Tablet end |
| `--bp-lg` | 1440px | Desktop |
| `--hero-mobile-w` | 440px | Эталон Figma mobile |
| `--content-mobile-w` | 408px | Ширина контента на 440 |
| `--container-max` | 1120px | Max контейнера desktop |
| `--container-padding-mobile` | 16px | |
| `--font-sans` | Poppins | |
| `--font-display` | Outfit | |

---

## 2. Брейкпоинты

| Зона | Условие | Figma |
|------|---------|-------|
| **Mobile** | `max-width: 833px` | 440px эталон |
| **Mobile small** | `max-width: 439px` | узкий мобайл (hero, design) |
| **Tablet** | `min-width: 834px` and `max-width: 1439px` | 834px |
| **Desktop** | `min-width: 1440px` | 1440px |
| **Desktop lock** | `min-width: 1441px` | без масштабирования |

Доп. брейкпоинты в компонентах: `500px`, `600px`, `1099px`, `1100px`.

---

## 3. Стандартные блоки (main.css)

### Base
- `tokens.css` — переменные
- `reset.css` — сброс
- `typography.css` — шрифты, базовые стили текста
- `layout.css` — `.app`, `.app__main`, `.container`, footer
- `sections.css` — `.section`, `.radio-page`, `.app__main` padding
- `tablet-770.css` — fluid-ширина 770→1330 на планшете для контейнеров

### Компоненты
| Файл | Блоки | Где используется |
|------|-------|------------------|
| `nav.css` | `.c-nav` | styleguide (base header) |
| `button.css` | `.button`, `.button--sm`, `.button--primary` и т.д. | везде |
| `input.css` | поля форм | CTA, модалки |
| `card.css` | `.c-card` | styleguide |
| `section.css` | `.c-section` | секции |
| `badge.css` | `.c-badge` | |
| `modal.css` | `.c-modal` | |
| `toast.css` | `.c-toast` | уведомления |
| `hero.css` | `.hero` | hero без figure |
| `hero-with-figure.css` | `.hero-with-figure` | hero с картинкой |
| `comparison-expertise.css` | `.comparison-expertise` | |
| `content-media-block.css` | `.content-media-block` | |
| `content-media-rows.css` | `.content-media-rows` | |
| `cta-card.css` | `.cta-card` | |
| `benefits.css` | `.benefits` | |
| `media-split.css` | `.media-split` | |
| `billboard-formats.css` | форматы билбордов | billboards |
| `feature-grid.css` | `.feature-grid` | |
| `why-cards.css` | `.why-cards` | |
| `approach-cards.css` | `.approach-cards` | |
| `cta-form.css` | `.cta-form` | CTA с формой |
| `steps.css` | `.steps`, `.demo-steps` | |
| `prod-expertise.css` | `.prod-expertise` | |
| `ai-result.css` | `.ai-result` | AI-блоки |
| `transport-formats.css` | | transport |
| `demo-cookie-consent.css` | | cookie modal |
| `demo-home-calc.css` | | калькулятор |
| `demo-lead-success.css` | | success modal |
| `demo-menu.css` | `.demo-menu` | шапка (все demo-страницы) |
| `demo-footer.css` | `.demo-footer` | подвал demo |

---

## 4. Вспомогательные CSS

| Файл | Назначение |
|------|------------|
| `hero-full-bleed.css` | Hero 100vw на всех страницах, `!important` |
| `desktop-1440-lock.css` | max-width: 1440px при `min-width: 1441px` для страниц |
| `demo-mobile-lock.css` | Пустой (шаблон) |
| `css/pages/*-mobile-lock.css` | Мобильные правки для legacy-страниц |
| `css/pages/*-tablet-lock.css` | Планшетные правки |
| `css/pages/*-desktop.css` | Desktop-правки (print) |

---

## 5. Страницы и их CSS

### Мигрированы в css_v2 (один файл)
| Страница | Файл | body/page class |
|----------|------|-----------------|
| Home | `css_v2/pages/home.css` | `.demo-home` |
| Design | `css_v2/pages/design.css` | `.demo-design` |
| AI Assistants | `css_v2/pages/ai_assistants.css` | `.demo-ai` |

### Legacy (css/pages + lock)
| Страница | Файлы | body/page class |
|----------|-------|-----------------|
| Production | production.css, production-mobile-lock, production-tablet-lock | `.demo-prod` |
| Print | print.css, print-desktop, print-tablet-lock, print-mobile-lock | `.demo-print` |
| Telegram | telegram.css, telegram-tablet-lock, telegram-mobile-lock | `.demo-tg` |
| Transport | transport.css, transport-mobile-lock | `.transport-page` |
| Billboards | billboards.css, billboards-mobile-lock | `.billboards-page` |
| Elevators | elevators.css, elevators-tablet-lock, elevators-mobile-lock | `.elevators-page` |
| Stops | stops.css, stops-tablet-lock, stops-mobile-lock | `.stops-page` |
| Radio | radio.css, radio-tablet-lock | `.radio-page` |
| Cookie Policy | cookie_policy.css | |
| 404 | 404.css | |
| Styleguide | styleguide.css | |

⚠️ **Отсутствуют (404):** `billboards-mobile-lock.css`, `stops-mobile-lock.css`, `elevators-mobile-lock.css` — шаблоны их подключают, файлов нет. Либо создать, либо убрать из page_css.

---

## 6. Шаблон страницы

```html
{% block header %}
  {% include "components/demo/menu.html" %}
{% endblock %}

{% block content %}
  <div class="demo-<page>">  <!-- или .billboards-page, .elevators-page и т.д. -->
    <section class="hero hero--mod section">...</section>
    ...
  </div>
{% endblock %}

{% block footer %}
  {% include "components/demo/footer.html" %}
{% endblock %}
```

---

## 7. Классы страниц для desktop-1440-lock

В `desktop-1440-lock.css` используются:  
`.demo-prod`, `.demo-print`, `.demo-design`, `.demo-tg`, `.demo-ai`, `.demo-home`,  
`.elevators-page`, `.radio-page`, `.stops-page`, `.transport-page`, `.billboards-page`.

---

## 8. Fluid-расчёты (tablet 834–1439)

Шаблон: `clamp(770px, calc(770 * 100vw / 834), 1330px)` — линейное масштабирование 770→1330 при 834→1440.

Используется в: `tablet-770.css`, `content-media-block`, `cta-form`, `prod-expertise`, `ai_assistants`, `design`, `home`.

---

## 9. Проблемы и рекомендации

### 9.1 !important
- **Где:** `demo-menu.css` (~100), `demo-footer.css` (~100), lock-файлы (десятки в каждом), `hero-full-bleed.css`, `sections.css`, `layout.css`, `tablet-770.css`.
- **Что делать:** по мере правок — повышать специфичность, убирать `!important`. В новых файлах не использовать.

### 9.2 Мёртвый/дублирующий код
- `static/css/` vs `static/css_v2/`: main.css тянет только css_v2. Legacy-страницы используют `css/pages/*`. Часть компонентов есть в обоих (demo-menu, demo-footer, toast и т.д.).
- `demo-mobile-lock.css` — пустой; можно удалить подключение или наполнить.

### 9.3 Костыли
- `hero-full-bleed.css` с `!important` — перебивает hero.css. Лучше встроить логику в hero и убрать отдельный файл.
- Много lock-файлов с дублированием — можно постепенно объединять в `css_v2/pages/<page>.css`.

### 9.4 Mobile-first
- main.css и css_v2 в целом mobile-first.
- Lock-файлы — desktop-first (правила через `max-width`). При миграции приводить к mobile-first.

### 9.5 Соответствие Figma
- Эталон mobile: **440px**.
- Эталон tablet: **834px**.
- Эталон desktop: **1440px**.

---

## 10. План правок по странице (440 и далее)

1. Открыть макет Figma для 440 (834, 1440).
2. Проверить, использует страница `css_v2` или `css/pages` + lock.
3. Для legacy: либо править lock-файлы, либо начать миграцию в `css_v2/pages/<page>.css` (см. `docs/PAGE_MIGRATION_ALGORITHM.md`).
4. Стили писать mobile-first, без `!important`.
5. Использовать токены (`--space-*`, `--text-*`, `--font-sans` и т.д.).
6. Убирать мёртвый код и дублирование при каждом правке.

---

## 11. Быстрая шпаргалка

| Что | Где |
|-----|-----|
| Токены | `css_v2/base/tokens.css` |
| Контейнер | `layout.css` → `.container` |
| Hero | `hero.css`, `hero-with-figure.css`, `hero-full-bleed.css` |
| CTA форма | `cta-form.css` |
| Меню | `demo-menu.css` |
| Подвал | `demo-footer.css` |
| Секции | `sections.css`, `section.css` |
| Fluid tablet | `tablet-770.css` |
| 1440 lock | `desktop-1440-lock.css` |

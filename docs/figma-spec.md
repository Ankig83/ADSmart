## Figma → Django Templates + чистый CSS: спецификация переноса (Dev Mode / Inspect)

Важно: по требованию проекта **значения не угадываем**. Все размеры/цвета/шрифты/отступы берём из **Figma Dev Mode → Inspect** или через **Figma API** (см. `scripts/figma_export.py`).

### Входные nodes (источник правды)

File key: `RgixkfQjBcvWPRvylxy0u8`

Nodes:
- Формат A: `140:4885`, `140:5405`, `140:5488`, `140:5549`, `140:5641`, `140:4957`, `140:5134`, `140:5226`, `140:5304`
- Формат B: `140:5885`, `140:6041`, `140:6133`, `140:6240`, `140:6361`, `140:6492`, `140:6607`, `140:6684`, `140:6787`, `140:6863`, `140:6944`
- Формат C: `140:8078`, `140:7117`, `140:7209`, `140:7314`, `140:7436`, `140:7566`, `140:7679`, `140:7751`, `140:7850`, `140:7922`, `140:7999`

---

## A) Карта страниц

Заполняется по каждому node:

- **Node ID**:
- **Frame name (точно как в Figma)**:
- **Frame size (W×H)**:
- **Тип страницы**: Home / Раздел / Навигационная / Вариант (A/B/C)
- **Основные блоки (сверху вниз)**:
  - Hero:
  - Section 1:
  - List / Cards:
  - CTA:
  - Footer:
- **Навигация**:
  - Primary CTA → куда ведёт:
  - Secondary CTA → куда ведёт:
  - Внутренние ссылки/табы → куда ведут:
- **Состояния** (если есть на макете):
  - Empty state:
  - Loading:
  - Error:
  - Disabled:

Рекомендация по шаблонам:
- `templates/pages/<slug>.html` — страница
- `templates/components/sections/<slug>__<block>.html` — блок страницы (компоновка)
- атомарные компоненты остаются в `templates/components/*.html`

---

## B) Design tokens → `static/css/tokens.css`

Снимаем из Inspect:

### Colors (role-based)
- `--bg`:
- `--surface`:
- `--surface-2`:
- `--text`:
- `--muted`:
- `--border`:
- `--primary`:
- `--primary-2` (если есть градиенты/hover):
- `--success`:
- `--warning`:
- `--danger`:

Важно: если в макете есть темы/светлая версия — фиксируем отдельные роли (например `--bg-light`) или отдельный `[data-theme="light"]`.

### Typography
Для каждого текст-стиля из Dev Mode (например: H1/H2/Body/Caption/Button):
- **name**:
- `font-family`
- `font-size`
- `font-weight`
- `line-height`
- `letter-spacing`

### Spacing scale
Снимаем сетку/step (обычно 4/8) и реальные значения отступов:
- `--space-1` … `--space-n`

### Radius / Shadow / Z-index
- `--radius-*`
- `--shadow-*` (описать в px + rgba)
- `--z-*` (nav/modal/toast/tooltip)

### Breakpoints
Если A/B/C — это разные ширины фреймов:
- width A:
- width B:
- width C:

Рекомендуемые брейкпоинты (без пересечений: mobile ≤833 | tablet 834-1439 | desktop ≥1440):
- `--bp-md`: 834px
- `--bp-md-max`: 1439px
- `--bp-lg`: 1440px

---

## C) Компоненты (реюз)

Подход: **атомарные** + **секционные** компоненты.

### Atomic
- **Button**
  - variants: primary/secondary/ghost/danger (как в Figma)
  - sizes: sm/md/lg (если есть)
  - states: default/hover/active/disabled/loading
  - include:
    - `{% include "components/button.html" with label="..." href="..." variant="primary" size="md" disabled=False %}`
- **Input**
  - types: text/email/password/search
  - states: default/focus/error/disabled
  - include:
    - `{% include "components/input.html" with label="..." name="..." value="..." placeholder="..." error="..." %}`
- **Card**
  - виды: перечислить по макету (например info-card/media-card/stat-card)
  - include:
    - `{% include "components/card.html" with title="..." subtitle="..." content="..." %}`
- **Badge/Chip**
- **Nav / Tabs**
- **Accordion**
- **Modal**
- **Toast**

### Section-level (page blocks)
Для каждого блока страницы заводим include:
- `templates/components/sections/<page>__hero.html`
- `templates/components/sections/<page>__list.html`
- `templates/components/sections/<page>__cta.html`

---

## D) Таблица сборки (page → components → data)

Формат:

| Page template | Components used | Data needed (mocks) |
|---|---|---|
| `pages/home.html` | `nav`, `hero`, `...` | `user`, `items[]`, `stats` |

---

## E) Ассеты и экспорт

### Структура в проекте
- `static/assets/icons/*.svg`
- `static/assets/images/*.{png,webp}`
- `static/assets/brand/*` (logo/favicons)

### Manual export (новичку)
1) Открой node → найди layer с иконкой/картинкой.
2) В правой панели `Export`:
   - **icons**: `SVG` (outline strokes → “Include stroke” по необходимости)
   - **images/photos**: `PNG` или `WebP` (если доступно)
   - scale: `1x` и `2x` (3x — только если в макете реально нужна ультра-плотность)
3) Имена файлов: `kebab-case` (например `icon-search.svg`, `hero-bg@2x.webp`)
4) Сохрани в соответствующий каталог `static/assets/...`.

### Auto export (через Figma API)
Требует переменные окружения:
- `FIGMA_TOKEN` (Personal Access Token)
- `FIGMA_FILE_KEY=RgixkfQjBcvWPRvylxy0u8`

Сценарий:
1) Сформировать список node ids (из Dev Mode links) в формате `140:4885`.
2) Вызвать `GET /v1/files/{file_key}/nodes?ids=...` и найти слои с `exportSettings`.
3) Вызвать `GET /v1/images/{file_key}?ids=...&format=svg|png&scale=1|2`.
4) Скачать и сохранить в `static/assets/...`.

Команда: см. `scripts/figma_export.py`.




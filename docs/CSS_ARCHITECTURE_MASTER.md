# CSS Architecture Master · ADSmart

**Отчёт для фронт-верстальщика.** Обращаться к этому файлу после каждого запроса на правки страниц/брейкпоинтов.

**Цель:** доведение всех страниц и брейкпоинтов до идеала (схожесть с Figma). Mobile-first, без мёртвого кода, минимум `!important`, без костылей.

---

## 1. Порядок загрузки CSS (base.html)

```
1. css_v2/main.css              — единая точка входа (импорты base + components)
2. {% block page_css %}         — страничные CSS (см. §5)
3. css_v2/base/hero-full-bleed.css
4. css_v2/base/desktop-1440-lock.css
5. css/components/demo-mobile-lock.css   — сейчас пустой (шаблон)
```

**Важно:** `hero-full-bleed.css` идёт после main.css и перебивает hero через `!important`. Lock-файлы (mobile/tablet) подключаются в block page_css и имеют последнее слово для своих страниц.

---

## 2. Брейкпоинты (Figma)

| Зона | Условие | Figma эталон |
|------|---------|--------------|
| **Mobile S** | `max-width: 439px` | узкий мобайл (используется в ai-result, hero-with-figure) |
| **Mobile M** | `440px – 833px` | **440px эталон** (не трогаем без необходимости) |
| **Tablet** | `min-width: 834px` and `max-width: 1439px` | **834px** |
| **Desktop** | `min-width: 1440px` | **1440px** |
| **Desktop lock** | `min-width: 1441px` | без масштабирования на широких экранах |

**Стандартные MQ (mobile-first):**
- `@media (max-width: 439px)` — mobile small
- `@media (max-width: 833px)` — mobile (в lock-файлах)
- `@media (min-width: 834px)` — tablet+
- `@media (min-width: 834px) and (max-width: 1439px)` — только tablet (fluid)
- `@media (min-width: 1440px)` — desktop
- `@media (min-width: 1441px)` — desktop lock (desktop-1440-lock.css)

**Доп. брейкпоинты в компонентах (по возможности привести к стандарту):**
- `500px` — demo-home-calc
- `600px` — hero-with-figure (фигура)
- `1099px` / `1100px` — home.css
- `360px` — ai-result

---

## 3. Токены (tokens.css)

| Переменная | Значение | Описание |
|------------|----------|----------|
| `--bp-md` | 834px | Tablet start |
| `--bp-md-max` | 1439px | Tablet end |
| `--bp-lg` | 1440px | Desktop |
| `--hero-mobile-w` | 440px | Эталон mobile |
| `--content-mobile-w` | 408px | Ширина контента на 440 |
| `--container-max` | 1120px | Max контейнера desktop |
| `--space-4` … `--space-12` | 16px … 48px | Отступы |
| `--font-sans` | Poppins | Основной шрифт |
| `--font-display` | Outfit | Заголовки |

**Токены в MQ:** в `@media` пока везде литералы `834px`, `1439px`. CSS custom properties в MQ ограничены.

---

## 4. Стандартные блоки (main.css → components)

| Файл | Блоки | Где используется |
|------|-------|------------------|
| `layout.css` | `.app`, `.app__main`, `.container`, footer | везде |
| `sections.css` | `.section`, `.radio-page`, отступы | секции |
| `tablet-770.css` | fluid 770→1330 для контейнеров | планшет |
| `hero.css` | `.hero` | hero без figure |
| `hero-with-figure.css` | `.hero-with-figure` | AI, Design, Telegram, Print, Home |
| `content-media-block.css` | `.content-media-block` | Design, AI |
| `content-media-rows.css` | `.content-media-rows` | Print |
| `comparison-expertise.css` | `.comparison-expertise` | AI |
| `why-cards.css` | `.why-cards` | Design, Telegram |
| `approach-cards.css` | `.approach-cards` | Telegram |
| `benefits.css` | `.benefits` | Design, Production, Telegram |
| `media-split.css` | `.media-split` | AI |
| `feature-grid.css` | `.feature-grid` | Print |
| `cta-form.css` | `.cta-form` | CTA с формой |
| `cta-card.css` | `.cta-card` | карточки CTA |
| `steps.css` | `.steps`, `.demo-steps` | Home |
| `prod-expertise.css` | `.prod-expertise` | Production |
| `ai-result.css` | `.ai-result` | AI |
| `billboard-formats.css` | форматы билбордов | Billboards |
| `transport-formats.css` | форматы транспорта | Transport |
| `demo-menu.css` | `.demo-menu` | шапка demo |
| `demo-footer.css` | `.demo-footer` | подвал demo |
| `demo-home-calc.css` | модалка калькулятора | Home |
| `demo-cookie-consent.css` | cookie modal | везде |

---

## 5. Страницы и их CSS

### Мигрированы в css_v2 (один файл, mobile-first)

| Страница | Файл | Page class |
|----------|------|------------|
| Home | `css_v2/pages/home.css` | `.demo-home` |
| Design | `css_v2/pages/design.css` | `.demo-design` |
| AI Assistants | `css_v2/pages/ai_assistants.css` | `.demo-ai` |

### Legacy (css/pages + lock)

| Страница | Файлы | Page class | Примечание |
|----------|-------|------------|------------|
| Production | production.css, production-mobile-lock, production-tablet-lock | `.demo-prod` | css/pages |
| Print | print.css, print-desktop, print-tablet-lock, print-mobile-lock | `.demo-print` | 4 файла |
| Telegram | telegram.css, telegram-tablet-lock, telegram-mobile-lock | `.demo-tg` | |
| Transport | transport.css, transport-mobile-lock | `.transport-page` | нет tablet-lock |
| Billboards | billboards.css, **billboards-mobile-lock** | `.billboards-page` | ⚠️ billboards-mobile-lock.css 404 |
| Elevators | elevators.css, elevators-tablet-lock, **elevators-mobile-lock** | `.elevators-page` | ⚠️ elevators-mobile-lock.css 404 |
| Stops | stops.css, stops-tablet-lock, **stops-mobile-lock** | `.stops-page` | ⚠️ stops-mobile-lock.css 404 |
| Radio | — | `.radio-page` | **без page_css** — только main.css |
| Cookie Policy | cookie_policy.css | — | |
| 404 | 404.css | — | |
| Styleguide | styleguide.css | — | |

### Отдельные lock-файлы (css/pages), не связанные с css_v2

- `design-mobile-lock.css` — Design (подключен? проверять template design.html — **не подключен**, Design использует только css_v2)
- `ai_assistants-mobile-lock.css`, `ai_assistants-tablet-lock.css` — AI (подключены? **не подключены**, AI только css_v2)

---

## 6. Desktop 1440 Lock (desktop-1440-lock.css)

Для `min-width: 1441px` — max-width: 1440px для страниц:
`.demo-prod`, `.demo-print`, `.demo-design`, `.demo-tg`, `.demo-ai`, `.demo-home`,  
`.elevators-page`, `.radio-page`, `.stops-page`, `.transport-page`, `.billboards-page`.

Hero full-bleed: для demo-tg, demo-ai, demo-home — hero внутри lock-контейнера.

---

## 7. Hero Full-Bleed (hero-full-bleed.css)

```css
.hero, .hero-with-figure {
  width: 100vw !important;
  max-width: 100vw !important;
  margin-left: calc(50% - 50vw) !important;
  margin-right: calc(50% - 50vw) !important;
}
```

**Костыль:** перебивает hero.css через `!important`. Идеал — встроить в hero/hero-with-figure.

---

## 8. Fluid tablet (834→1439)

Шаблон: `clamp(770px, calc(770 * 100vw / 834), 1330px)` — линейное масштабирование.

Используется в: `tablet-770.css`, `content-media-block`, `layout`, lock-файлах.

**Конфликт:** `static/css/tablet-770.css` — с `!important`; `static/css_v2/base/tablet-770.css` — без. main.css импортирует `css_v2/base/tablet-770.css`. В base.html нет прямого `css/tablet-770.css` — он подтягивается только через legacy страницы, если где-то ссылаются. **Проверено:** base.html НЕ подключает `css/tablet-770.css`, main.css импортирует `base/tablet-770.css` (из css_v2). Но `css/tablet-770.css` существует и содержит !important — возможно legacy-страницы его не подключают. Оставляем как есть.

---

## 9. Проблемы и план исправлений

### 9.1 !important

| Файл | ~кол-во | Контекст |
|------|---------|----------|
| demo-menu.css | ~81 | mobile/tablet/desktop правила |
| demo-footer.css | ~80 | то же |
| hero-full-bleed.css | 4 | hero full-bleed |
| base.css (css/) | 4 | tablet centering |
| sections.css | 1 | app__main padding-bottom |
| tablet-770.css (css/) | ~26 | container fluid |
| hero-with-figure.css | 1 | right: 0 на 600px |
| Lock-файлы | десятки каждый | перебивают page styles |

**План:** при каждой правке — убирать `!important` через повышение специфичности или переупорядочивание.

### 9.2 Мёртвый / дублирующий код

- `css/` vs `css_v2/`: main.css только css_v2. Legacy — css/pages/*. Компоненты demo-menu, demo-footer есть в обоих; main импортирует css_v2.
- `demo-mobile-lock.css` — пустой. Либо наполнить общими мобильными правками, либо убрать из base.html.
- `design-mobile-lock.css`, `ai_assistants-mobile-lock.css`, `ai_assistants-tablet-lock.css` — существуют, но не подключаются в шаблонах (Design и AI используют только css_v2). Либо удалить, либо не трогать.

### 9.3 404 lock-файлы

- `billboards-mobile-lock.css` — шаблон ссылается, файла нет → 404.
- `stops-mobile-lock.css` — то же.
- `elevators-mobile-lock.css` — то же.

**Действие:** создать минимальные файлы или убрать ссылки из шаблонов.

### 9.4 Костыли

- `hero-full-bleed.css` — отдельный файл с !important. Встроить в hero.
- Lock-файлы — desktop-first (`max-width`). При миграции — mobile-first.
- `/* Tablet hard-fix */`, `/* home-tablet-overrides */` в home.css — по возможности убрать.

### 9.5 Дублирование tablet-770

- `static/css/tablet-770.css` — с !important.
- `static/css_v2/base/tablet-770.css` — без !important.

main.css импортирует `base/tablet-770.css` (относительно css_v2) — значит используется css_v2 версия. `css/tablet-770.css` — legacy, возможно нигде не подключается. Проверить: grep по templates — base.html не подключает. Legacy-страницы подключают только `css/pages/*`. Вывод: `css/tablet-770.css` скорее не используется. Оставить в отчёте для справки.

---

## 10. Чек-лист при правке страницы (440 / 834 / 1440)

1. Открыть макет Figma для нужного брейкпоинта (440, 834, 1440).
2. Определить, страница в **css_v2** или **css/pages** + lock.
3. **Для css_v2:** править `css_v2/pages/<page>.css`. Mobile-first, без `!important`.
4. **Для legacy:** править lock-файлы (mobile-lock последний) или начать миграцию в css_v2.
5. Использовать токены: `--space-*`, `--text-*`, `--font-sans`.
6. Удалять мёртвый код и дублирование при каждом касании.
7. Проверить соответствие: отступы, шрифты, размеры, layout.

---

## 11. Быстрая шпаргалка «Где что менять»

| Что | Где |
|-----|-----|
| Токены | `css_v2/base/tokens.css` |
| Контейнер | `layout.css` → `.container` |
| Hero | `hero.css`, `hero-with-figure.css`, `hero-full-bleed.css` |
| Секции | `sections.css`, `section.css` |
| Fluid tablet | `tablet-770.css` |
| 1440 lock | `desktop-1440-lock.css` |
| Меню | `demo-menu.css` |
| Подвал | `demo-footer.css` |
| Home блоки | `home.css` (Blok1–Blok8, Contact, FAQ) |

---

## 12. Работа со страницей 440

**Правило из css-responsive.mdc:** блоки на 440px считаются готовыми. Вносить изменения только для tablet (834+) и desktop (1440). Фокус на планшетах.

**Если правка касается 440:**
- Mobile-first: базовые стили = 440. Проверить, не конфликтует ли mobile-lock.
- Порядок: page.css → tablet-lock → mobile-lock (mobile-lock последний).
- Не добавлять в page.css то, что перебьётся mobile-lock.

---

## 13. Возможные исправления (рекомендации инженера)

### Приоритет 1 — критичные

1. **404 lock-файлы** — создать `billboards-mobile-lock.css`, `stops-mobile-lock.css`, `elevators-mobile-lock.css` (минимальный сброс) или убрать ссылки из шаблонов.
2. **hero-full-bleed** — перенести логику в `hero-with-figure.css` / `hero.css`, убрать отдельный файл и `!important`.
3. **base.css** — дублирует layout (box-sizing, body, container). main.css не использует base.css (импортирует reset, layout). base.css подключается только в legacy? Проверить использование и при возможности удалить дублирование.

### Приоритет 2 — рефакторинг

4. **demo-menu / demo-footer** — ~160 `!important`. Разнести стили по breakpoints, повысить специфичность селекторов (`.demo-home .demo-menu` и т.п.), убрать !important.
5. **tablet-770** — в css/ с !important; css_v2 — без. Унифицировать, оставить одну версию.
6. **Орфан lock-файлы** — `design-mobile-lock.css`, `ai_assistants-mobile-lock.css`, `ai_assistants-tablet-lock.css` не подключаются. Удалить или интегрировать в css_v2.

### Приоритет 3 — миграция

7. **Legacy → css_v2** — Production, Print, Telegram, Transport, Billboards, Elevators, Stops, Radio — постепенно мигрировать в `css_v2/pages/<page>.css`, убирать lock-цепочки.
8. **Радио без page_css** — страница полагается на main.css. Проверить, нужен ли отдельный `radio.css` для page-specific стилей.
9. **variables.css vs tokens.css** — конфликт `--container-max`. Оставить только tokens.

### Приоритет 4 — полировка

10. **Брейкпоинты 500, 600, 1100** — привести к 439/440, 834, 1440 где возможно.
11. **Хардкод** — `left: 178px`, `width: 1440px` и т.п. заменить на clamp/проценты/токены.
12. **demo-mobile-lock.css** — либо наполнить общими мобильными правками, либо убрать подключение.

---

*Отчёт обновлён: 2025-03-15. Обращаться после каждого запроса.*

# ADSmart · Фронтенд Master Report

**Единый справочник для верстальщика.** Обращаться к этому файлу после каждого запроса на правки страниц/брейкпоинтов.

**Цель:** доведение всех страниц и брейкпоинтов до идеала (схожесть с Figma). Mobile-first, без мёртвого кода, минимум `!important`, без костылей.

---

## 1. Порядок загрузки CSS (base.html)

```
1. css_v2/main.css                    ← единая точка входа (base + components)
2. {% block page_css %}               ← страничные CSS (см. §6)
3. css_v2/base/hero-full-bleed.css    ← hero 100vw (!important)
4. css_v2/base/desktop-1440-lock.css  ← фикс широких экранов
5. css/components/demo-mobile-lock.css ← общие мобильные правки (сейчас пустой)
```

**Важно:** `hero-full-bleed.css` перебивает hero через `!important`. Lock-файлы в block page_css — последнее слово для своих страниц.

---

## 2. Брейкпоинты (Figma-эталон)

| Зона | Условие | Figma | Примечание |
|------|---------|-------|------------|
| **Mobile S** | `max-width: 439px` | узкий мобайл | ai-result, hero-with-figure, hero |
| **Mobile M** | `440px – 833px` | **440px эталон** | эталон мобилки, не трогать без необходимости |
| **Tablet** | `min-width: 834px` and `max-width: 1439px` | **834px** | fluid 834→1439 |
| **Desktop** | `min-width: 1440px` | **1440px** | эталон десктопа |
| **Desktop lock** | `min-width: 1441px` | — | без масштабирования на широких экранах |

**Стандартные MQ (mobile-first):**
```css
@media (max-width: 439px)   { /* mobile small */ }
@media (max-width: 833px)   { /* mobile (в lock-файлах) */ }
@media (min-width: 440px) and (max-width: 833px)  { /* mobile M */ }
@media (min-width: 834px)   { /* tablet+ */ }
@media (min-width: 834px) and (max-width: 1439px) { /* только tablet */ }
@media (min-width: 1440px)  { /* desktop */ }
@media (min-width: 1441px)  { /* desktop lock */ }
```

**Нерегламентированные (привести к стандарту):**
- `500px` — demo-home-calc, demo-lead-success
- `600px` — hero-with-figure (фигура)
- `1099px` / `1100px` — home.css
- `360px` — ai-result
- `770px` — tablet-770 (fluid контейнеров)

---

## 3. Токены (tokens.css)

| Переменная | Значение | Описание |
|------------|----------|----------|
| `--bp-md` | 834px | Tablet start |
| `--bp-md-max` | 1439px | Tablet end |
| `--bp-lg` | 1440px | Desktop |
| `--hero-mobile-w` | 440px | Эталон mobile |
| `--content-mobile-w` | 408px | Контент на 440 |
| `--container-max` | 1120px | Max контейнера desktop |
| `--container-padding-mobile` | 16px | |
| `--container-padding-tablet` | 32px | |
| `--space-4` … `--space-12` | 16px … 48px | Отступы |
| `--font-sans` | Poppins | Основной |
| `--font-display` | Outfit | Заголовки |

**⚠️ Конфликт:** `variables.css` имеет `--container-max: 1440px`, `tokens.css` — `1120px`. main.css импортирует tokens, variables не импортируется напрямую. Ориентир — tokens.

---

## 4. Стандартные блоки (components)

| Файл | Блоки | Где используется |
|------|-------|------------------|
| **layout.css** | `.app`, `.app__main`, `.container`, footer | везде |
| **sections.css** | `.section`, `.radio-page` | секции |
| **tablet-770.css** | fluid 770→1330 для контейнеров | планшет |
| **hero.css** | `.hero`, `.hero--elevators`, `.hero--billboards` и т.д. | hero без figure |
| **hero-with-figure.css** | `.hero-with-figure` | Home, AI, Design, Telegram, Print |
| **content-media-block.css** | `.content-media-block` | Design, AI |
| **content-media-rows.css** | `.content-media-rows` | Print |
| **comparison-expertise.css** | `.comparison-expertise` | AI |
| **why-cards.css** | `.why-cards` | Design, Telegram |
| **approach-cards.css** | `.approach-cards` | Telegram |
| **benefits.css** | `.benefits` | Design, Production, Telegram |
| **media-split.css** | `.media-split` | AI |
| **feature-grid.css** | `.feature-grid` | Print |
| **cta-form.css** | `.cta-form` | CTA с формой |
| **cta-card.css** | `.cta-card` | карточки CTA |
| **steps.css** | `.demo-steps` | Home |
| **prod-expertise.css** | `.prod-expertise` | Production |
| **ai-result.css** | `.ai-result` | AI |
| **billboard-formats.css** | форматы билбордов | Billboards |
| **transport-formats.css** | форматы транспорта | Transport |
| **demo-menu.css** | `.demo-menu` | шапка demo (все страницы с demo) |
| **demo-footer.css** | `.demo-footer` | подвал demo |
| **demo-cookie-consent.css** | cookie modal | глобально |
| **demo-home-calc.css** | калькулятор | Home |
| **demo-lead-success.css** | lead success | Home, CTA |

---

## 5. Где что менять (шпаргалка)

| Что менять | Где файл |
|------------|----------|
| Токены | `css_v2/base/tokens.css` |
| Контейнер | `css_v2/base/layout.css` → `.container` |
| Hero | `hero.css`, `hero-with-figure.css`, `hero-full-bleed.css` |
| Секции | `sections.css`, `section.css` |
| Fluid tablet | `tablet-770.css` |
| 1440 lock | `desktop-1440-lock.css` |
| Меню | `demo-menu.css` |
| Подвал | `demo-footer.css` |
| **Home** | `css_v2/pages/home.css` (Blok1–8, Contact, FAQ) |
| **Design** | `css_v2/pages/design.css` |
| **AI Assistants** | `css_v2/pages/ai_assistants.css` |
| **Production** | `css/pages/production.css` + lock |
| **Print, Telegram** | `css/pages/*.css` + lock |
| **Transport, Billboards, Elevators, Stops** | `css/pages/*.css` + lock |

---

## 6. Страницы и CSS-файлы

### css_v2 (mobile-first, один файл на страницу)

| Страница | Файл | Page class |
|----------|------|------------|
| Home | `css_v2/pages/home.css` | `.demo-home` |
| Design | `css_v2/pages/design.css` | `.demo-design` |
| AI Assistants | `css_v2/pages/ai_assistants.css` | `.demo-ai` |

### Legacy (css/pages + lock-цепочка)

| Страница | Файлы | Page class | 404? |
|----------|-------|------------|------|
| Production | production.css, production-mobile-lock, production-tablet-lock | `.demo-prod` | — |
| Print | print.css, print-desktop, print-tablet-lock, print-mobile-lock | `.demo-print` | — |
| Telegram | telegram.css, telegram-tablet-lock, telegram-mobile-lock | `.demo-tg` | — |
| Transport | transport.css, transport-mobile-lock | `.transport-page` | transport-mobile-lock **НЕТ** |
| Billboards | billboards.css, **billboards-mobile-lock** | `.billboards-page` | billboards-mobile-lock **404** |
| Elevators | elevators.css, elevators-tablet-lock, **elevators-mobile-lock** | `.elevators-page` | elevators-mobile-lock **404** |
| Stops | stops.css, stops-tablet-lock, **stops-mobile-lock** | `.stops-page` | stops-mobile-lock **404** |
| Radio | — (только main.css) | `.radio-page` | — |
| Cookie Policy | cookie_policy.css | — | — |
| 404 | 404.css | — | — |
| Styleguide | styleguide.css | — | — |

### Орфан-файлы (есть, но не подключаются)

- `design-mobile-lock.css`
- `ai_assistants-mobile-lock.css`
- `ai_assistants-tablet-lock.css`

---

## 7. Проблемы и план исправлений

### 7.1 !important (≈1700+ вхождений по проекту)

| Файл | ~кол-во | Контекст |
|------|---------|----------|
| demo-menu.css (v2) | ~100 | mobile/tablet/desktop |
| demo-footer.css (v2) | ~100 | то же |
| hero-full-bleed.css | 10 | hero 100vw, overflow |
| Lock-файлы (legacy) | десятки каждый | max-width, mobile overrides |
| sections.css | 1 | app__main padding-bottom |
| hero-with-figure.css | 1 | right: 0 на 600px |
| home.css | 1 | |
| design.css | 1 | |
| base.css (legacy) | 4 | tablet |
| tablet-770.css (legacy) | 26 | container fluid |

**План:** при каждой правке убирать `!important` через селекторы с большей специфичностью (`.demo-home .demo-menu` и т.п.).

### 7.2 Мёртвый / дублирующий код

- **variables.css vs tokens.css** — конфликт `--container-max`. variables не импортируется в main.css — legacy.
- **demo-mobile-lock.css** — пустой (только комментарии). Либо наполнить, либо убрать из base.html.
- **css/ vs css_v2/** — дублирование demo-menu, demo-footer в обоих. main.css импортирует только css_v2.
- **tablet-770** — есть в css/ (с !important) и css_v2/ (без). Используется css_v2.

### 7.3 404 lock-файлы

- `billboards-mobile-lock.css` — ссылается billboards.html, **файла нет**
- `elevators-mobile-lock.css` — ссылается elevators.html, **файла нет**
- `stops-mobile-lock.css` — ссылается stops.html, **файла нет**
- `transport-mobile-lock.css` — ссылается transport.html, **файла нет**

**Действие:** создать минимальные файлы-заглушки или убрать ссылки из шаблонов.

### 7.4 Костыли

| Костыль | Где | Решение |
|---------|-----|---------|
| hero-full-bleed.css | отдельный файл, !important | встроить в hero/hero-with-figure |
| `/* Tablet hard-fix */` | demo-menu.css | заменить на layout |
| `/* home-tablet-overrides */` | home.css | вынести в отдельный блок |
| Lock desktop-first | max-width: 833px | при миграции — mobile-first |

### 7.5 Рекомендуемые исправления (приоритет)

1. **Критично:** Создать 404 lock-файлы или убрать ссылки.
2. **Критично:** hero-full-bleed — перенести в hero, убрать !important.
3. **Рефакторинг:** demo-menu/demo-footer — убрать !important (селекторы + page class).
4. **Рефакторинг:** Брейкпоинты 500, 600, 1100 → 439/440, 834, 1440 где возможно.
5. **Полировка:** Хардкод `left: 178px`, `width: 1440px` → clamp/токены.
6. **Миграция:** Legacy → css_v2 для Production, Print, Transport, Billboards и т.д.

---

## 8. Чек-лист при правке страницы (440 / 834 / 1440)

1. Открыть макет Figma для нужного брейкпоинта.
2. Определить: страница в **css_v2** или **css/pages** + lock.
3. **css_v2:** править `css_v2/pages/<page>.css`. Mobile-first, без !important.
4. **Legacy:** править lock-файлы (mobile-lock последний).
5. Использовать токены: `--space-*`, `--text-*`, `--font-sans`.
6. Удалять мёртвый код и дубли при каждом касании.
7. Сверять: отступы, шрифты, размеры, layout с Figma.

---

## 9. Работа с брейкпоинтом 440

**Правило (css-responsive.mdc):** блоки на 440px считаются готовыми. Изменения — только для tablet (834+) и desktop (1440). Фокус на планшетах.

**Если правка всё же касается 440:**
- Mobile-first: базовые стили = mobile (440). Проверить конфликт с mobile-lock.
- Порядок: page.css → tablet-lock → mobile-lock (mobile-lock последний).
- Не добавлять в page.css то, что перебьётся mobile-lock.

---

## 10. Fluid-формулы

**440 → 834 (mobile):**
```css
clamp(min, calc(X * 100vw / 440), max)
```
320px → 72.7% | 440px → 100% | 833px → 189.3%

**834 → 1439 (tablet):**
```css
clamp(770px, calc(770 * 100vw / 834), 1330px)
```

---

---

## 11. Строгое правило: не трогать

**Billboards**, **Home**, **Transport**, **Stops**, **Elevators**, **Radio**, **Telegram**, **AI Assistants** — не вносить изменения на любых брейкпоинтах.

---

*Отчёт создан: 2025-03-15. Обращаться после каждого запроса.*

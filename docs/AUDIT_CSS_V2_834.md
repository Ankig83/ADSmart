# Аудит css_v2 — отчёт для проверки 834

**Дата:** 14.03.2025  
**Правило:** 440px — не трогать (проверен).  
**Фокус:** проверка брейкпоинта 834 (планшет).

---

## 1. Структура css_v2

```
static/css_v2/
├── main.css              # Точка входа
├── base/
│   ├── tokens.css        # --bp-md: 834px, --bp-md-max: 1439px
│   ├── variables.css     # Legacy (конфликт с tokens: --container-max 1120 vs 1440)
│   ├── reset.css, typography.css, layout.css
│   ├── container.css, sections.css
│   └── tablet-770.css    # Ширина контейнера 770→1330 на планшете
├── components/           # 28 компонентов
└── pages/
    ├── home.css          # ~5 800 строк
    ├── design.css
    └── ai_assistants.css
```

---

## 2. Использование брейкпоинта 834

| Тип MQ | Описание | Файлы |
|--------|----------|-------|
| `min-width: 834px` | Планшет и выше | nav, button, section, hero, steps, ai-result, billboard-formats, benefits, feature-grid, media-split, prod-expertise, transport-formats, content-media-rows, cta-form |
| `min-width: 834px) and (max-width: 1439px)` | Только планшет (834–1439) | layout, tablet-770, demo-menu, demo-footer, comparison-expertise, content-media-block, approach-cards, cta-card, why-cards, hero, hero-with-figure, design, ai_assistants, demo-home-calc, **home.css** (много блоков) |
| `min-width: 834px) and (max-width: 1099px)` | Узкий планшет | home.css (1 блок) |

### Главные файлы для проверки 834

1. **base/layout.css** — контейнер, `.app__section`
2. **base/tablet-770.css** — ширина секций на планшете
3. **base/sections.css** — отступы
4. **components/demo-menu.css** — меню 834–1439 (с !important)
5. **components/demo-footer.css** — футер 834–1439 (с !important)
6. **components/hero.css** — Hero tablet
7. **components/hero-with-figure.css** — Hero с фигурой
8. **pages/home.css** — все блоки Home (Blok1–Blok8, Contact, FAQ)

---

## 3. !important — проблемы

| Файл | Кол-во | Контекст |
|------|--------|----------|
| **demo-menu.css** | ~81 | Почти все правила mobile/tablet/desktop |
| **demo-footer.css** | ~80 | То же самое |
| **home.css** | 4 | `.demo-footer` на 834–1439: width, max-width, margin |
| **sections.css** | 1 | `.app__main { padding-bottom }` mobile |
| **hero-with-figure.css** | 1 | `right: 0` на 600px |

**Итого ~167 использований.** В `main.css` заявлено «без !important», но в demo-компонентах это не соблюдается.

---

## 4. Код и паттерны

### Костыли и хардкоды

- `demo-menu.css:316` — `/* Tablet menu hard-fix */`
- `home.css:3739` — `/* Tablet hard-fix for nodes 140:8177 / 140:8192 */`
- `home.css:3903` — `/* ═══ home-tablet-overrides.css ═══ */`

### Пиксель-идеальные Figma-метрики

- `left: 178px`, `left: 482px`, `width: 1440px`, `grid-template-columns: 288px 239px 346px` и т.п.
- Трудно масштабировать и переиспользовать.

### Конфликты переменных

- `tokens.css`: `--container-max: 1120px`
- `variables.css`: `--container-max: 1440px` (если есть)

### Токены в media queries не используются

В `tokens.css` есть `--bp-md: 834px`, но в `@media` везде литералы `834px`, `1439px`.

---

## 5. Чек-лист проверки 834

Для проверки брейкпоинта 834 на каждом блоке/странице:

- [ ] **base/layout.css** — ширина контейнера, отступы
- [ ] **base/tablet-770.css** — секции с clamp(770px … 1330px)
- [ ] **base/sections.css** — отступы секций
- [ ] **demo-menu** — меню 834–1439
- [ ] **demo-footer** — футер 834–1439
- [ ] **hero** — hero tablet
- [ ] **hero-with-figure** — hero с фигурой
- [ ] **home.css** — Blok1 (Hero), Blok2–Blok8, Contact, FAQ
- [ ] **design.css** — страница Дизайн
- [ ] **ai_assistants.css** — страница AI Assistants

### Блоки home.css по нодам Figma

| Блок | Figma node | Строки (примерно) |
|------|------------|-------------------|
| Общие | — | 14, 292, 628, 3306, 3531, 3740, 3904 |
| Blok1 Hero | — | — |
| Blok2 шаги | 140:8092 | 2559–2561 |
| Blok3 экспертиза | 140:8081 | 292–293 |
| Blok4 технологии | 140:8121 | 685–687 |
| Blok4 feature | 140:8128 | 1167–1169 |
| Blok7 Contact + FAQ | 140:7415 | 1858–1981 |
| FINAL LOCK | — | 4178–4179 |
| 834–1099 | — | 4571 |
| demo-footer override | — | 5780 |

---

## 6. Рекомендации перед чисткой

1. **!important** — заменить на селекторы с большей специфичностью в demo-menu и demo-footer.
2. **Токены** — использовать `var(--bp-md)` в media queries (в postcss или с env()).
3. **hard-fix** — вынести в отдельные блоки и заменить на нормальные layout-решения.
4. **home.css** — разбить на блоки или файлы по секциям для удобства проверки.
5. **440** — не трогать (по правилу).

---

## 7. Следующий шаг

**Проверка 834.** Идти постранично и поблочно, сверяя с макетом Figma:

1. Home — блоки 1–8, Contact, FAQ
2. Design
3. AI Assistants

С каких страниц/блоков начать?

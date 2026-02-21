# Страница Радио — навигация по коду

## MCP Figma
MCP Figma подключён. Можно использовать `get_design_context` / `get_screenshot` для нод.

---

## Файлы

| Файл | Назначение |
|------|------------|
| `templates/pages/radio.html` | Шаблон страницы |
| `static/css/pages/radio.css` | Базовые стили (desktop 1440px) |
| `static/css/pages/radio-tablet-lock.css` | Планшет 834–1439px |
| `static/css/pages/radio-mobile-lock.css` | Мобильные ≤833px (загружается последним) |

---

## HTML — что где искать (radio.html)

| Секция | Строка | Класс | Описание |
|--------|--------|-------|----------|
| Обёртка | ~35 | `.demo-radio` | Контейнер всей страницы |
| Hero | ~38 | `.demo-radio-hero` | Фон, заголовок, кнопки |
| Benefits | ~65 | `.demo-radio-benefits` | «Радио — для скорости и доверия» |
| — заголовок | ~68 | `.demo-radio-benefits__title` | Строки 1 и 2 для переноса |
| — карточки | ~75 | `.demo-radio-benefits__cards` | ul с 4 li |
| — карточка | ~76 | `.demo-radio-benefits__card` | ring + body (h3 + p) |
| — кольцо | ~79 | `.demo-radio-benefits__ring` | 94×94px, иконка внутри |
| — body | ~87 | `.demo-radio-benefits__body` | h3 + p |
| Measure | ~125 | `.demo-radio-measure` | «Эфирный ролик + AI-ассистент» |
| Steps | ~200 | `.demo-radio-steps` | 5 карточек step_card |
| Ideal | ~222 | `.demo-radio-ideal` | «Для каких задач идеально» |
| CTA | ~258 | `.demo-radio-cta` | Форма заявки |

---

## CSS — что где искать

### radio.css (desktop)
- **стр.1–25** — шапка файла, список секций
- **стр.28–35** — `.demo-radio` обёртка
- **стр.37–100** — Hero
- **стр.102–215** — Benefits (ring, icon-wrap, body, h3, p)
- **стр.218+** — Measure (@media 1440px)

### radio-tablet-lock.css (834–1439px)
- **стр.1–12** — шапка
- **стр.17+** — Hero tablet
- **стр.95+** — Benefits tablet (grid 4 колонки)
- **стр.170+** — Measure, Steps, Ideal, CTA

### radio-mobile-lock.css (≤833px)
- **стр.1–25** — шапка с нумерацией секций
- **стр.28–95** — Hero, Benefits (padding 44 16 56!)
- **стр.100–225** — Benefits: ring, icon-wrap (25px/26px), body
- **стр.228–335** — Measure (flex column gap 42px)
- **стр.340–445** — Steps (иконка СВЕРХУ)
- **стр.448–510** — Ideal, CTA
- **стр.615+** — @media (max-width: 439px) экстра-малые

---

## Исправление пересечения Benefits ↔ Measure
Текст под нижними карточками (Локализация, Наш подход) пересекался с Measure.
**Файл:** `radio-mobile-lock.css`  
**Строка:** ~93  
**Изменение:** `padding: 44px 16px 56px` — увеличен padding-bottom до 56px.

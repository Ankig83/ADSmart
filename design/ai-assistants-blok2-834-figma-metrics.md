# Отступы и размеры Blok2 (Comparison) для 834px — из Figma

Источник: `design/figma-nodes.json`, нода 140:7692.

Страница: AI ассистенты (140:7679). Блок: Blok2 (140:7692).

## 140:7692 — Blok2 (корневой фрейм)

Секция `.demo-ai-comparison`.

## 140:7693 — Frame 427321865 (обёртка: title + grid)

Содержит заголовок и два блока сравнения.

## 140:7694 — Заголовок

- **Текст**: «Мы привносим экспертизу туда, где технологии нуждаются в стратегии»
- **Размер**: 770×62
- **fontSize**: 24px
- **lineHeight**: 31.2px
- **letterSpacing**: 0.48px
- **fontWeight**: 600 (SemiBold)
- **цвет**: #ffffff

## Отступ между заголовком и grid (из координат)

- **margin-bottom заголовка / gap**: 42px (18166 − 18124)

## 140:7695 — Frame 427321864 (grid двух блоков)

- **layoutMode**: VERTICAL (блоки друг под другом)
- **Размер**: 770×395 (каждый блок)
- **itemSpacing между блоками**: 22px (18583 − 18561)

## 140:7696, 140:7707 — Блоки (platform / partner)

- **border-radius**: 8px
- **overflow**: hidden
- **border**: none (в tablet макете)

## 140:7697, 140:7708 — Заголовки блоков (Frame 427321606)

- **padding**: 10px 12px
- **fontSize**: 18px
- **lineHeight**: 23.4px
- **letterSpacing**: 0.18px
- **border-radius**: 8px 8px 0 0
- Платформа (140:7697): **background** #FFB661, **color** #000000
- Партнёр (140:7708): **background** #FF7B00, **color** #ffffff

## 140:7699, 140:7701, 140:7703, 140:7705, 140:7710, 140:7712, 140:7714, 140:7716 — ячейки

- **padding**: 3px 12px
- **height**: 82px (FIXED)
- **background**: #19161c
- **border-top**: 1px solid rgba(255, 255, 255, 0.2)
- **fontSize**: 14px
- **lineHeight**: 18.2px
- **letterSpacing**: 0.18px
- **color**: #ffffff

## Итоговые значения для CSS (834–1439px)

| Элемент | Свойство | Значение |
|---------|----------|----------|
| .demo-ai-comparison | padding | 44px clamp(32px, 2.6vw, 40px) |
| .demo-ai-comparison__title | max-width | 770px |
| .demo-ai-comparison__title | margin-bottom | 42px |
| .demo-ai-comparison__title | font-size | 24px |
| .demo-ai-comparison__title | line-height | 31.2px |
| .demo-ai-comparison__grid | max-width | 770px |
| .demo-ai-comparison__grid | gap | 22px |
| .demo-ai-comparison__block-header | padding | 10px 12px |
| .demo-ai-comparison__block-cell | padding | 3px 12px |
| .demo-ai-comparison__block-cell | min-height | 82px |

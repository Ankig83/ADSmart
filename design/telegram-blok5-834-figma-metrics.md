# Отступы и размеры Blok5 (Comparison) для 834px — из Figma

Источник: `design/node-140-7808.json`, нода 140:7808.

Страница: Телеграм (140:7751). Блок: Blok5 (140:7808).

## 140:7808 — Blok5 (корневой фрейм)

- **Размер**: 834×973
- **padding**: 15px left/right, 44px top/bottom
- **background**: #000000

## 140:7809 — Frame 427321865 (title + grid)

- **itemSpacing** между заголовком и grid: **42px**
- **itemSpacing** между блоками: **22px**

## 140:7810 — Заголовок

- **Текст**: «Экспертиза там, где другие жмут «Запустить рекламу»»
- **Размер**: 804×31
- **fontSize**: 24px
- **lineHeight**: 31.2px
- **letterSpacing**: 0.48px
- **fontWeight**: 600

## 140:7811 — Frame 427321864 (grid двух блоков)

- **layoutMode**: VERTICAL
- **Ширина контента**: 804px
- **itemSpacing**: 22px

## 140:7812, 140:7823 — Блоки (platform / partner)

- **border-radius**: 8px
- **overflow**: hidden

## Заголовки блоков (140:7813, 140:7824)

- **padding**: 10px 12px
- **fontSize**: 18px
- **lineHeight**: 23.4px
- **border-radius**: 8px 8px 0 0
- Платформа: **#FFB661**, color #000000
- Партнёр: **#FF7B00**, color #ffffff

## Ячейки (140:7815–140:7822, 140:7826–140:7832)

- **padding**: 3px 12px
- **min-height**: 82px (некоторые 83px)
- **background**: #19161c
- **border-top**: 1px solid rgba(255, 255, 255, 0.2)
- **fontSize**: 14px
- **lineHeight**: 18.2px
- Последняя ячейка: **border-radius** 0 0 8px 8px

## Итоговые значения для CSS (834–1439px)

| Элемент | Свойство | Значение |
|---------|----------|----------|
| .demo-tg-comparison | padding | 44px clamp(15px, 2vw, 32px) |
| .demo-tg-comparison__title | max-width | 804px |
| .demo-tg-comparison__title | margin-bottom | 42px |
| .demo-tg-comparison__grid | max-width | 804px |
| .demo-tg-comparison__grid | gap | 22px |
| .demo-tg-comparison__block-header | padding | 10px 12px |
| .demo-tg-comparison__block-cell | padding | 3px 12px |
| .demo-tg-comparison__block-cell | min-height | 82px |

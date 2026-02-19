# Отступы и размеры Blok7 (Contact) для 834px — из Figma

Источник: `design/stops-contact-834-nodes.json`.

**Как получить данные из Figma снова:**
```bash
# В корне проекта (нужны FIGMA_TOKEN и FIGMA_FILE_KEY в .env)
python scripts/figma_export.py dump --ids 140:7415 140:7416 140:7427 140:7418 --out design/stops-contact-834-nodes.json
```
В JSON ищи: `absoluteBoundingBox` (x, y, width, height), `paddingLeft/Right/Top/Bottom`, `itemSpacing`, `layoutMode`, `counterAxisAlignItems`.

## 140:7415 — Blok7 (корневой фрейм)
- **Размер**: 833×500
- **Padding**: 44px top, 44px bottom, 32px left, 32px right
- **itemSpacing**: 10

## 140:7416 — Frame (внутренний контейнер, две колонки)
- **Размер**: 769×412
- **layoutMode**: HORIZONTAL
- **itemSpacing (gap между колонками)**: **42px**
- **counterAxisAlignItems**: CENTER (вертикальное выравнивание по центру)

## 140:7418 — левая колонка (заголовок + подзаголовок)
- **itemSpacing между заголовком и подзаголовком**: **22px**
- Заголовок: fontSize 32, lineHeight 41.6px, letterSpacing -0.96
- Подзаголовок: fontSize 18, lineHeight 23.4px, letterSpacing -0.54

## Родитель текста и кнопок (140:7417)
- **itemSpacing между блоком текста и кнопками**: **32px**

## Кнопки (Frame 427321855 / Buttons)
- **Padding**: 16px top/bottom, 32px left/right
- **itemSpacing между кнопками**: 12px

## 140:7427 — форма (оранжевая рамка)
- **Размер**: 408×412
- **border**: 1px solid #ff7b00, border-radius 12px
- **background**: #19161c
- Поля ввода: paddingLeft 22, paddingRight 22, paddingTop 18, paddingBottom 18
- **itemSpacing между полями формы**: 10px
- Заголовок формы «Получить комплексное предложение»: fontSize 28, lineHeight 36.4, letterSpacing -0.84

## Итоговые значения для CSS (834px)
| Элемент | Свойство | Значение |
|---------|----------|----------|
| .demo-stops-contact | padding | 44px 32px |
| .demo-stops-contact__inner | max-width | 769px (или 770) |
| .demo-stops-contact__inner | gap (column-gap) | 42px |
| .demo-stops-contact__inner | align-items | center |
| .demo-stops-contact__title | margin-bottom | 22px |
| .demo-stops-contact__text | margin-bottom | 32px |
| .demo-stops-contact__dl | margin между кнопками | 12px |
| .demo-stops-contact__dl | padding | 16px 32px |
| .demo-stops-contact__formbox | width | 408px, height 412px |
| .demo-stops-contact__formbox | padding | по макету (≈ 32px top, 20px sides) |
| .demo-contact полей | gap / margin между полями | 10px или по 18px между полями |

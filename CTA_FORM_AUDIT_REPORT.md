# Технический аудит блока cta-form

## 1. Использование

| Страница | Файл |
|----------|------|
| Остановки/Афиши | stops.html |
| Лифты/Домофоны | elevators.html |
| Радио | radio.html |

Классы: `.cta-form`, `.cta-form__form`, `.cta-form__fields`, `input`, `textarea` — нет. Кнопка: `.button`, не `.cta-form__submit`.

---

## 2. По страницам

| Свойство | stops | elevators | radio |
|----------|-------|-----------|-------|
| gap у .cta-form | 40px / 48px / 64px | 40px / 48px / 64px | 40px / 48px / 64px |
| gap у .cta-form__form | var(--space-8)=32px | var(--space-8)=32px | var(--space-8)=32px |
| gap у .cta-form__fields | 16px | 16px | 16px |
| margin у input | нет | нет | нет |
| margin у textarea | нет | нет | нет |
| margin у кнопки | нет | нет | нет |
| padding у .cta-form__form | 32px | 32px | 32px |
| display у .cta-form__form | flex | flex | flex |
| align-items | нет | нет | нет |
| Page-specific override | .container gap 32/40/48 | .container gap 32/40/48 | .container gap 32/40/48 |

---

## 3. Проверка

| Вопрос | Ответ |
|--------|-------|
| .cta-form__fields и кнопка как отдельные flex-элементы | НЕТ — form (block) не flex, поля и кнопка — block-поток |
| Кнопка внутри .cta-form__fields | НЕТ |
| Margin-collapse | Возможен между .cta-form__fields и button |
| Переопределение gap в page-specific | НЕТ — gap задаётся в cta-form.css |
| Сброс margin у input глобально | НЕТ — reset.css только font: inherit |

---

## 4. Уникальные значения

| Свойство | Значения |
|----------|----------|
| gap | 4, 12, 16, 32, 40, 48, 64 |
| padding | 18, 22, 32 |
| margin | 0 |
| display | flex |

---

## 5. Эталон компонента (реализовано)

```
.cta-form__form
  display: flex
  flex-direction: column
  gap: var(--space-8)

.cta-form__form form
  display: flex
  flex-direction: column
  gap: var(--space-6)

.cta-form__fields
  display: flex
  flex-direction: column
  gap: 16px
```

Добавлено: `form { display: flex; flex-direction: column; gap: var(--space-6); }`.

---

## 6. Проверка после правки

| Критерий | Результат |
|----------|-----------|
| Расстояние между последним input и кнопкой ≥ 16px | ДА — gap 24px (var(--space-6)) |
| Новые значения вне системы | НЕТ — 24px = var(--space-6) |
| Page-specific стили формы | НЕТ — только layout .container |

---

## Отчёт

### Причина проблемы

`form` — дочерний элемент `.cta-form__form`. У `.cta-form__form` flex с gap только для прямых детей (form-title, form). У `form` по умолчанию `display: block`, поэтому его дети (.cta-form__fields и кнопка) идут в блочном потоке без gap.

### Где было переопределение

Page-specific: нет переопределений gap для формы. Только `.cta-form--stops .container`, `.cta-form--elevators .container`, `.cta-form--radio .container` задают layout контейнера (flex, gap 32/40/48).

### Что исправлено

Добавлено в `cta-form.css`:
```css
.cta-form__form form {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}
```

### Подтверждение

Форма оформлена единым компонентом в `static/css_v2/components/cta-form.css`. Page-specific CSS не задаёт стили формы, только layout `.container`.

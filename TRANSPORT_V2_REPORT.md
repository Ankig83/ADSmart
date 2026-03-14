# Отчёт: Transport v2, cta-form, legacy cleanup

## 1. cta-form — централизация

- Весь код формы: `static/css_v2/components/cta-form.css`
- Страницы stops, elevators, radio, transport: локальных стилей формы нет
- page-specific gap для формы: нет (только `.cta-form--* .container` layout)
- margin у кнопки: нет
- display:block у form: нет (form имеет `display: flex`)

## 2. Legacy — удалено

- `static/css/pages/stops-mobile-lock.css`
- `static/css/pages/stops-tablet-lock.css`
- `static/css/pages/transport-mobile-lock.css`
- Убраны ссылки на lock-файлы из stops.html

stops.css, elevators.css, radio.css — без legacy, только layout-модификаторы.

## 3. Transport v2 — реализовано

Секции:
- `hero hero--transport`
- `benefits benefits--transport`
- `media-split media-split--poster media-split--transport`
- `steps steps--transport`
- `feature-grid feature-grid--transport`
- `cta-form cta-form--transport`

transport.css — только модификаторы: `.hero--transport`, `.media-split--transport`, `.cta-form--transport`.

## 4. Проверка ограничений

| Критерий | Результат |
|----------|-----------|
| Новые значения spacing | НЕТ — только 32, 40, 48 |
| fixed height | НЕТ (на странице не добавлено) |
| Новые font-size | НЕТ |
| Новые radius | НЕТ |
| Централизованный cta-form | ДА |
| Удалены старые CSS | ДА — stops-mobile-lock.css, stops-tablet-lock.css, transport-mobile-lock.css |

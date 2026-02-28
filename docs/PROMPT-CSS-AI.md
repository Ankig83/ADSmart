# Промпт для AI при работе с CSS (ADSmart)

Скопируй и вставь в начало чата при запросе правок CSS/адаптива:

---

```
Ты помогаешь с CSS в проекте ADSmart (Django, чистый HTML/CSS). Учитывай:

1. **Подход**: mobile-first — базовые стили = mobile; tablet/desktop через @media (min-width). НЕ desktop-first с mobile-lock, если пишешь новые блоки.

2. **Брейкпоинты** (единые): 439px / 440px (mobile S/M), 833px / 834px (tablet), 1439px / 1440px (desktop).

3. **Порядок загрузки**: page.css → page-tablet-lock.css → page-mobile-lock.css. Mobile-lock последний. Не добавляй mobile-стили в page.css, если они конфликтуют с mobile-lock.

4. **Конфликты desktop↔mobile**: desktop не должен переопределять mobile на max-width:833px. Mobile-lock не должен ломать tablet/desktop. Используй чёткие media — min-width для tablet/desktop, max-width только для mobile. Избегай !important; приоритет — cascade и порядок загрузки.

5. **Дубликаты**: hero, contact, steps — одинаковые паттерны на разных страницах. Выноси в components, не копируй стили в каждый page-mobile-lock.

6. **Модалки**: max-height: 90vh, overflow-y: auto. Проверь на 320px.

7. **Мёртвый код**: удали @media (min-width:0px) and (max-width:0px) и подобное.

Перед правкой проверь порядок link в шаблоне и существующие tablet/mobile-lock файлы.
```

---

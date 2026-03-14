# Отчёт: страница «Лифты» на базе дизайн-системы v2

## Реализация

- **hero hero--elevators** — фон, overlay, title, subtitle, actions (2 кнопки)
- **benefits benefits--elevators** — 4 карточки (Аудитория в плену, Гиперлокальный таргетинг, Высокая частота контакта, Контекстное влияние)
- **media-split media-split--poster media-split--elevators** — изображение, 3 карточки (Захват внимания, Мгновенный диалог, Квалификация и передача)
- **steps steps--elevators** — 5 карточек (Анализ и геотаргетинг, Умный креатив, Автоматизация, Запуск под ключ, Аналитика)
- **feature-grid feature-grid--elevators** — 4 карточки (Локальный ритейл, Бытовые услуги, Интернет-сервисы, Локальный B2B)
- **cta-form cta-form--elevators** — заголовок, текст, форма (3 поля, кнопка)

---

## 1. Новые значения spacing вне системы (8, 16, 24, 32, 40, 48, 64, 80, 120)

**НЕТ**

В elevators.css: gap 32, 40, 48 — все допустимы.

---

## 2. Fixed height

**НЕТ**

В elevators.css и шаблоне нет height и min-height.

---

## 3. Новые font-size

**НЕТ**

Используются только системные hero, section-title, card-title, base text.

---

## 4. Новые radius

**НЕТ**

Карточки: background #19161C, border-radius 24px из v2.

---

## 5. Только системные кнопки

**ДА**

Используются только: `.button`, `.button--lg`, `.button--primary`, `.button--outline`.

---

## 6. Page-specific CSS

**Минимален**

Файл `elevators.css`:
- `.hero--elevators` — object-position
- `.cta-form.cta-form--elevators .container` — layout контейнера (gap 32/40/48)

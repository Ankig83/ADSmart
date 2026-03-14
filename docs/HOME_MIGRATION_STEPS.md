# Миграция Home по алгоритму PAGE_MIGRATION_ALGORITHM.md

Пошаговый перенос `home.css` в формат ai_assistants: без !important, без костылей.

## Структура страницы Home

- `.demo-home` — контейнер hero
- `.demo-steps` — блок «От стратегии до аналитики» (home_desktop_15)
- `.demo-exp` — блок «Экспертиза» (home_desktop_16)
- `.demo-tech19` — блок «Умные технологии» (home_desktop_19)
- `.demo-ad` — блок с формой/CTA (home_ad)
- `.demo-team` — блок «Профессионалы» (home_desktop_20)
- `.demo-contact` — блок «Свяжитесь с нами» (home_contact_us)
- `.demo-faq` — FAQ (home_faq)
- Модалки: demo-home-calc, demo-lead-success — в components

## Порядок миграции

1. **Базовые** — .app, .app__main, .demo-home
2. **Hero** — .demo-home .hero-with-figure (mobile, tablet, desktop)
3. **demo-steps** — mobile, tablet, desktop
4. **demo-tech19** — mobile, tablet, desktop
5. **demo-ad** — mobile, tablet, desktop
6. **demo-exp** — mobile, tablet, desktop
7. **demo-team** — mobile, tablet, desktop
8. **demo-contact** — mobile, tablet, desktop
9. **demo-faq** — mobile, tablet, desktop
10. **Модалки** — если нужны home-специфичные правки

## Структура файла (как ai_assistants)

```
/* home.css — страница Home. Эталон: 440, 834, 1440 */

/* ─── Глобальные ─── */
.app { ... }
.app__main { ... }
.demo-home { ... }

/* ─── Desktop 1440+ ─── */
@media (min-width: 1440px) { ... }

/* ─── Mobile ≤833 ─── */
@media (max-width: 833px) { ... }

/* ─── Tablet 834–1439 ─── */
@media (min-width: 834px) and (max-width: 1439px) { ... }
```

## Правила

- Скоуп через .demo-home где нужно
- Без !important — cascade через специфичность
- Один media-блок на брейкпоинт (не разбросанные)
- Удалить legacy demo-home-hero (не используется)

## Выполнено

- **Шаг 1:** Hero — без !important
- **Шаг 2:** demo-steps + все секции — убран !important (2643 вхождения)

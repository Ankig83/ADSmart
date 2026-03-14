# План миграции CSS → css_v2

**Подход:** mobile-first, без костылей, общие блоки вынесены отдельно. При нестыковках — модификаторы.

**Брейкпоинты:** 440px (mobile), 834px (tablet), 1440px (desktop).

---

## 1. Общая стратегия

1. **Базовые стили** — `css_v2/base/` (reset, variables, typography, sections, container)
2. **Компоненты** — `css_v2/components/` (button, hero, cta-card, cta-form и т.д.)
3. **Страницы** — `css_v2/pages/` (пока пусто; page-specific только модификаторы и layout)
4. **Lock-файлы** — постепенно убрать: стили перенести в mobile-first media queries внутри компонентов

---

## 2. Очередность миграции

### Фаза 1: Base (базовый слой)
- [ ] tokens → variables.css
- [ ] base.css (layout) → частично в reset/sections
- [ ] nav, input, card, section, badge, modal, toast → css_v2/components/
- [ ] demo-cookie-consent, demo-home-calc, demo-mobile-lock → вынести/упорядочить

### Фаза 2: Страницы с частичной миграцией
- [x] **design** — hero, content-media-block, why-cards, benefits, feature-grid, cta-card (блок контакт)
- [ ] **telegram** — аналогично design, убрать lock-файлы
- [ ] **ai_assistants** — hero-with-figure, comparison-expertise, content-media-block, cta-card
- [ ] **billboards, transport, production, elevators, stops** — убрать page overrides в модификаторы
- [ ] **radio** — ai-result, cta-form

### Фаза 3: Страницы без миграции
- [ ] **home** — demo-home-hero → hero/hero-with-figure, demo-steps → steps
- [ ] **print** — demo-print-* → hero, content-media-block, cta-form
- [ ] **404, cookie_policy** — демо-классы → v2 эквиваленты
- [ ] **styleguide** — c-section, sg → v2

### Фаза 4: Финализация
- [ ] Удалить lock-файлы (design-mobile-lock, design-tablet-lock и т.д.)
- [ ] Очистить design.css, telegram.css от перенесённых блоков
- [ ] Подключить только css_v2 в base.html (сформировать единую точку входа)

---

## 3. Вынесенные компоненты — статус

| Компонент | css_v2 | Шаблон | Используется |
|-----------|--------|--------|--------------|
| hero | hero.css | inline | billboards, transport, elevators, stops, radio |
| hero-with-figure | hero-with-figure.css | hero_with_figure.html | design, telegram, ai_assistants |
| content-media-block | content-media-block.css | content_media_block.html | design, ai_assistants |
| why-cards | why-cards.css | why_cards.html | design, telegram |
| approach-cards | approach-cards.css | approach_cards.html | design, telegram |
| comparison-expertise | comparison-expertise.css | comparison_expertise.html | design, telegram, ai_assistants |
| benefits | benefits.css | inline | design, transport, production, elevators |
| feature-grid | feature-grid.css | inline | design, billboards, transport и др. |
| cta-card | cta-card.css | cta_card.html | ai_assistants, **design** |
| cta-form | cta-form.css | inline | transport, telegram, stops, radio, production, elevators |
| media-split | media-split.css | inline | ai_assistants, stops |
| billboard-formats | billboard-formats.css | inline | billboards |
| transport-formats | transport-formats.css | inline | transport |
| ai-result | ai-result.css | inline | radio |

---

## 4. Текущая задача: Design — блок контакт (440px)

**Было:** `.demo-design-cta` в design.css, design-mobile-lock.css, design-tablet-lock.css, design-desktop.css

**Стало:** компонент `cta-card` (css_v2/components/cta-card.css) + include `cta_card.html`

**Figma 440:**
- Контейнер: padding 44px 16px, gap 10px, background #19161C
- Inner: flex column center, gap 26px, width 408px
- Заголовок: 24px, 600, white, center
- Текст: 18px, 400, rgba(255,255,255,0.8), center
- Кнопки: row, gap 12px; primary 16×32, 52px, #14F195, 64px radius; outline 1px white

`cta-card.css` уже реализует эти specs. Миграция: заменить секцию на `{% include "components/cta_card.html" %}` и удалить `.demo-design-cta` из design.css.

---

## 5. Правила

- Mobile-first: базовые стили = mobile; tablet/desktop через `@media (min-width: Npx)`
- Избегать !important
- Общие блоки — в css_v2/components/, при отличиях — модификатор (например `cta-card--design`)

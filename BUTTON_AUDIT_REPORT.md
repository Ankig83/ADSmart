# Аудит кнопок проекта ADSmart

## 1. Все кнопки

| Тег | Класс | Файл | Компонент |
|-----|-------|------|-----------|
| button | hero__btn hero__btn--primary | stops.html | Hero (Stops) |
| a | hero__btn hero__btn--outline | stops.html | Hero (Stops) |
| button | cta-form__submit | stops.html | CTA Form (Stops) |
| a | cta-form__link | stops.html | CTA Form (Stops) |
| button | demo-print-hero__btn demo-print-hero__btn--primary | print.html | Hero (Print) |
| a | demo-print-hero__btn demo-print-hero__btn--outline | print.html | Hero (Print) |
| button | demo-print-contact__btn | print.html | Contact (Print) |
| button | demo-lead-success__btn | lead_success_modal.html | Lead Success Modal |
| button | demo-btn demo-btn--primary | home.html | Hero (Home) |
| a | demo-btn demo-btn--outline | home.html | Hero (Home) |
| button | demo-billboards-hero__btn | billboards.html | Hero (Billboards) |
| button | demo-billboards-contact__btn | billboards_contact_us.html | Contact (Billboards) |
| button | demo-ai-hero__btn demo-ai-hero__btn--primary | ai_assistants.html | Hero (AI) |
| a | demo-ai-hero__btn demo-ai-hero__btn--outline | ai_assistants.html | Hero (AI) |
| a | demo-ai-cta__btn demo-ai-cta__btn--primary | ai_assistants.html | CTA (AI) |
| a | demo-ai-cta__btn demo-ai-cta__btn--outline | ai_assistants.html | CTA (AI) |
| button | c-toast__close | toast.html | Toast |
| button | demo-transport-hero__btn | transport.html | Hero (Transport) |
| button | demo-transport-contact__btn | transport_contact_us.html | Contact (Transport) |
| button | demo-contact__btn | home_contact_us.html | Contact (Home) |
| button | demo-prod-hero__btn demo-prod-hero__btn--primary | production.html | Hero (Production) |
| a | demo-prod-hero__btn demo-prod-hero__btn--outline | production.html | Hero (Production) |
| button | demo-prod-contact__btn | production.html | Contact (Production) |
| button | demo-tg-hero__btn demo-tg-hero__btn--primary | telegram.html | Hero (Telegram) |
| a | demo-tg-hero__btn demo-tg-hero__btn--outline | telegram.html | Hero (Telegram) |
| button | demo-tg-contact__btn | telegram.html | Contact (Telegram) |
| button | demo-design-hero__btn demo-design-hero__btn--primary | design.html | Hero (Design) |
| a | demo-design-hero__btn demo-design-hero__btn--outline | design.html | Hero (Design) |
| a | demo-design-cta__btn demo-design-cta__btn--primary | design.html | CTA (Design) |
| a | demo-design-cta__btn demo-design-cta__btn--outline | design.html | CTA (Design) |
| button | demo-menu__toggle | menu.html | Header |
| a | demo-radio-hero__btn demo-radio-hero__btn--primary | radio.html | Hero (Radio) |
| a | demo-radio-hero__btn demo-radio-hero__btn--outline | radio.html | Hero (Radio) |
| button | demo-radio-cta__submit | radio.html | CTA (Radio) |
| button | demo-cookie__btn | cookie_consent_modal.html | Cookie Modal |
| button | c-btn c-btn--ghost c-btn--sm | modal.html | Modal close |
| button | demo-elevators-hero__btn demo-elevators-hero__btn--primary | elevators.html | Hero (Elevators) |
| a | demo-elevators-hero__btn demo-elevators-hero__btn--outline | elevators.html | Hero (Elevators) |
| button | demo-elevators-contact__btn | elevators_contact_us.html | Contact (Elevators) |
| a | demo-404__btn | 404.html | 404 |
| button | demo-home-calc__close | home_calc_modal.html | Calc Modal close |
| button | demo-home-calc__btn | home_calc_modal.html | Calc Modal |
| button | demo-home-calc__btn demo-home-calc__btn--secondary | home_calc_modal.html | Calc Modal |
| button | demo-ad__btn | home_ad.html | Home Ad |
| button | c-btn c-btn--secondary (c-btn--sm) | styleguide.html, card.html | Styleguide |
| button | c-btn c-btn--secondary | styleguide.html | Styleguide |

---

## 2. Стили по кнопкам

### c-btn (button.css)
| Свойство | Значение |
|----------|----------|
| font-size | var(--text-sm) = 14px (md/sm) |
| font-weight | (inherit) |
| line-height | (inherit) |
| padding | 10px 14px (md); 8px 12px (sm) |
| border-radius | var(--radius-2)=8px (md); var(--radius-1)=4px (sm) |
| background | transparent; primary: gradient; secondary: rgba(255,255,255,.06); ghost: transparent; danger: rgba(255,77,79,.12) |
| border | 1px solid transparent; secondary: var(--border); danger: rgba(255,77,79,.25) |
| color | primary: #fff; secondary: var(--text); ghost: var(--muted); danger: #ffd0d0 |
| height | — |
| min-height | — |
| width | — |
| display | inline-flex |
| align-items | center |
| justify-content | center |
| gap | var(--space-2)=8px |

### hero__btn (hero.css v2)
| Свойство | Значение |
|----------|----------|
| font-size | (inherit) |
| font-weight | (inherit) |
| padding | 12px 20px |
| border-radius | var(--radius-md) — переменная не определена |
| background | --primary: black; --outline: transparent |
| border | --primary: none; --outline: 1px solid white |
| color | --primary: white; --outline: white |

### cta-form__link (cta-form.css)
| Свойство | Значение |
|----------|----------|
| font-size | 16px |
| font-weight | (inherit) |
| padding | 16px 32px |
| border-radius | 64px |
| background | transparent |
| border | 1px solid #ffffff |
| color | #ffffff |
| min-height | 52px |
| display | inline-flex |
| align-items | center |
| justify-content | center |

### cta-form__submit (cta-form.css)
| Свойство | Значение |
|----------|----------|
| font-size | 18px |
| font-weight | 500 |
| padding | 18px 22px |
| border-radius | 100px |
| background | #14f195 |
| border | none |
| color | #000000 |
| height | 56px |
| width | 100% |

### demo-btn (home.css)
| Свойство | Значение |
|----------|----------|
| padding | 16px 32px |
| border-radius | 64px |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| background | --primary: #14f195; --outline: transparent |
| border | --outline: 1px solid #ffffff |
| color | --primary: #000000; --outline: #ffffff |
| display | inline-flex |

### demo-billboards-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 265px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| color | #000000 |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| padding | — |
| display | inline-flex |

### demo-billboards-contact__btn
| Свойство | Значение |
|----------|----------|
| width | 145px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| padding | — |

### demo-transport-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 265px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |

### demo-transport-contact__btn
| Свойство | Значение |
|----------|----------|
| width | 145px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| padding | — |

### demo-radio-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 218px |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| background | --primary: #14f195; --outline: transparent |
| border | --outline: 1px solid #ffffff |

### demo-radio-cta__submit
| Свойство | Значение |
|----------|----------|
| width | 383px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| padding | — (margin-top: 6px) |

### demo-elevators-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 218px |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| background | --primary: #14f195; --outline: transparent |

### demo-elevators-contact__btn
| Свойство | Значение |
|----------|----------|
| width | 220px / 100% (responsive) |
| height | 56px / 52px (responsive) |
| border-radius | 100px / 64px |
| background | #14f195 |
| font-size | 18px |

### demo-ai-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 177px |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| padding | — |

### demo-ai-cta__btn
| Свойство | Значение |
|----------|----------|
| width | 218px / 250px / 232px (modifiers) |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |

### demo-tg-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 177px |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |

### demo-tg-contact__btn
| Свойство | Значение |
|----------|----------|
| width | 383px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |

### demo-design-hero__btn
| Свойство | Значение |
|----------|----------|
| width | 177px |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |
| font-weight | 500 |

### demo-design-cta__btn
| Свойство | Значение |
|----------|----------|
| width | 218px / 250px / 232px |
| height | 52px |
| border-radius | 64px |
| font-size | 18px |

### demo-prod-hero__btn
| Свойство | Значение |
|----------|----------|
| width | clamp(177px, ... 315px) |
| height | clamp(52px, ... 93px) |
| border-radius | 64px |
| font-size | clamp(18px, ... 32px) |

### demo-prod-contact__btn
| Свойство | Значение |
|----------|----------|
| width | clamp(383px, ... 682px) |
| height | clamp(52px, ... 93px) |
| border-radius | 64px |
| font-size | clamp(18px, ... 32px) |

### demo-print-hero__btn
| Свойство | Значение |
|----------|----------|
| width | clamp(177px, ... 315px) |
| height | clamp(52px, ... 93px) |
| border-radius | 64px |
| font-size | clamp(18px, ... 32px) |

### demo-print-contact__btn (print-desktop.css)
| Свойство | Значение |
|----------|----------|
| width | clamp(383px, ... 682px) |
| height | clamp(52px, ... 93px) |
| border-radius | 64px |
| font-size | clamp(18px, ... 32px) |

### demo-lead-success__btn
| Свойство | Значение |
|----------|----------|
| width | 136px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |
| padding | — |

### demo-home-calc__close
| Свойство | Значение |
|----------|----------|
| width | 24px |
| height | 24px |
| border-radius | 999px |
| padding | 0 |
| background | transparent |
| font-size | 20px |

### demo-home-calc__btn
| Свойство | Значение |
|----------|----------|
| width | 374px / 100% (responsive) |
| height | 56px / 44px / 48px (responsive) |
| border-radius | 64px |
| padding | 16px 32px |
| font-size | 18px / 15px (responsive) |
| background | #14f195; --secondary: transparent |

### demo-cookie__btn
| Свойство | Значение |
|----------|----------|
| width | 142px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| font-weight | 500 |
| line-height | 20px |

### demo-menu__toggle
| Свойство | Значение |
|----------|----------|
| width | 42px |
| height | 38px |
| border-radius | var(--radius-2)=8px |
| padding | — |
| border | 1px solid rgba(255,255,255,0.12) |
| background | transparent |

### demo-ad__btn
| Свойство | Значение |
|----------|----------|
| width | 100% / 383px / clamp(...) / 341px |
| height | 56px / 43px |
| border-radius | 100px / 76.86px |
| padding | 18px 22px / 13.83px 16.91px |
| font-size | 18px / 13.83px |

### demo-contact__btn
| Свойство | Значение |
|----------|----------|
| width | 100% / 383px |
| height | 56px |
| border-radius | 100px |
| font-size | 18px |
| background | #14f195 |

### demo-404__btn
| Свойство | Значение |
|----------|----------|
| width | 265px |
| height | 52px |
| border-radius | 64px |
| background | #14f195 |
| font-size | 18px |
| font-weight | 500 |

### c-toast__close
| Свойство | Значение |
|----------|----------|
| width | 28px |
| height | 28px |
| border-radius | var(--radius-1)=4px |
| padding | — |
| background | rgba(255,255,255,.06) |

---

## 3. Уникальные значения (расхождения)

### padding
| Значение | Где |
|----------|-----|
| 8px 12px | c-btn--sm |
| 10px 14px | c-btn |
| 12px 20px | hero__btn |
| 14px 18px | billboards/transport-contact (mobile lock) |
| 16px 32px | demo-btn, cta-form__link, demo-home-calc__btn |
| 18px 22px | cta-form__submit, demo-tg-contact (tablet), elevators-contact (tablet), print-contact (tablet) |
| 0 | demo-home-calc__close |
| clamp(11px…24px) clamp(22px…48px) | demo-design-cta (mobile) |
| clamp(13.83…16.91) | demo-ad__btn (834-1439) |

### border-radius
| Значение | Где |
|----------|-----|
| 4px (--radius-1) | c-btn--sm, c-toast__close |
| 8px (--radius-2) | c-btn, demo-menu__toggle |
| 12px | — |
| 64px | большинство demo-hero, demo-contact, demo-radio-cta, demo-lead-success |
| 100px | cta-form__submit, cta-form__link эквивалент, demo-contact, elevators-contact, billboards-contact (mobile) |
| 999px / 9999px | demo-home-calc__close, demo-radio-cta (mobile lock) |
| 76.86px | demo-ad__btn (834-1439) |
| var(--radius-md) | hero__btn — переменная не определена |

### font-size
| Значение | Где |
|----------|-----|
| 11px (--text-xs) | — |
| 14px (--text-sm) | c-btn |
| 15px | demo-home-calc__btn (mobile), billboards-contact (mobile) |
| 16px | cta-form__link, demo-design-cta (tablet), elevators-contact (439px) |
| 18px | hero, cta-form__submit, demo-btn, demo-billboards/transport/radio/elevators/ai/tg/design/prod/print, demo-lead-success, demo-cookie, demo-contact |
| 20px | demo-home-calc__close |
| clamp(14px…27px) | demo-design-cta (mobile) |
| clamp(15px…18px) | billboards/transport-contact (mobile) |
| clamp(16px…20px) | demo-print-contact (mobile) |
| clamp(18px…32px) | demo-prod, demo-print |
| 13.83px | demo-ad__btn (834-1439) |

### height
| Значение | Где |
|----------|-----|
| 24px | demo-home-calc__close |
| 28px | c-toast__close |
| 38px | demo-menu__toggle |
| 44px | demo-home-calc__btn (mobile), demo-elevators-hero (439px) |
| 48px | demo-home-calc__btn (tablet/desktop), billboards/transport-contact (mobile) |
| 52px | большинство hero/contact кнопок |
| 56px | cta-form__submit, demo-contact, elevators-contact, demo-ad, demo-home-calc__btn |
| clamp(44px…52px) | demo-lead-success (mobile) |
| clamp(48px…56px) | demo-print-contact (mobile) |
| clamp(52px…93px) | demo-prod, demo-print |

### background
| Значение | Где |
|----------|-----|
| transparent | c-btn (base), hero__btn--outline, cta-form__link |
| black | hero__btn--primary |
| #14f195 | demo-btn--primary, billboards/transport/radio/elevators/ai/tg/design/prod/print/contact, demo-lead-success, demo-cookie |
| #00ff8c | demo-radio-cta__submit (mobile lock) |
| linear-gradient(...) | c-btn--primary |
| rgba(255,255,255,.06) | c-btn--secondary |

---

## 4. Проверки

### Fixed height
- Да: demo-billboards-hero__btn 52px, demo-transport-hero__btn 52px, demo-radio-hero__btn 52px, demo-elevators-hero__btn 52px, demo-ai-hero__btn 52px, demo-tg-hero__btn 52px, demo-design-hero__btn 52px, demo-lead-success__btn 52px, demo-cookie__btn 52px, demo-404__btn 52px
- Да: cta-form__submit 56px
- Да: demo-home-calc__close 24px, c-toast__close 28px, demo-menu__toggle 38px
- Clamp: demo-prod-hero 52–93px, demo-print-hero 52–93px, demo-prod-contact 52–93px, demo-print-contact 48–56 (mobile), 52–93 (desktop)

### Разные border-radius
- Да: 4px, 8px, 64px, 100px, 999px, 9999px, 76.86px

### Разные padding
- Да: 8px 12px, 10px 14px, 12px 20px, 14px 18px, 16px 32px, 18px 22px

### Разные hover-стили
- c-btn--primary: filter brightness(1.02)
- c-btn--secondary: background rgba(255,255,255,.08)
- c-btn--ghost: background rgba(255,255,255,.06)
- c-btn--danger: background rgba(255,77,79,.16)
- cta-form__link: opacity 0.9
- demo-tg-hero__btn, demo-design-hero__btn, demo-ai-hero__btn: transform scale(1.05)
- demo-prod-hero__btn: transform scale(1.05)
- demo-prod-contact__btn, demo-tg-contact__btn, demo-print-contact__btn: transform scale(1.02)
- demo-elevators-contact__btn: transform translateX(-50%) scale(1.02)
- c-toast__close: background rgba(255,255,255,.10)

### Inline-стили
- Не обнаружено в HTML

---

## 5. По компонентам

### Hero
- hero__btn (Stops): padding 12px 20px, border-radius var(--radius-md) — не определена
- demo-btn (Home): 16px 32px, 64px
- demo-billboards-hero__btn: 265×52, 64px
- demo-transport-hero__btn: 265×52, 64px
- demo-radio-hero__btn: 218×52, 64px
- demo-elevators-hero__btn: 218×52, 64px
- demo-ai-hero__btn: 177×52, 64px
- demo-tg-hero__btn: 177×52, 64px
- demo-design-hero__btn: 177×52, 64px
- demo-prod-hero__btn: clamp, 64px
- demo-print-hero__btn: clamp, 64px

### Media-split
- Кнопок нет

### Feature-grid
- Кнопок нет

### CTA-form
- cta-form__link: min-height 52px, padding 16px 32px, 64px
- cta-form__submit: 56px, padding 18px 22px, 100px

### Header
- demo-menu__toggle: 42×38px, 8px

### Footer
- demo-footer__link — ссылки, не кнопки

---

## 6. Итог

| Метрика | Значение |
|---------|----------|
| Общее количество кнопочных стилей | ~45 уникальных селекторов/классов |
| Количество уникальных вариантов | ~25 групп по визуальному поведению |
| Конфликтующие значения | padding (8–18px), height (24–93px), border-radius (4–100px), font-size (14–32px) |
| Модификаторы (--) | hero__btn--primary/outline, demo-btn--primary/outline, demo-*-hero__btn--primary/outline, demo-home-calc__btn--secondary, demo-ai-cta__btn--primary/outline, demo-design-cta__btn--primary/outline |
| Неопределённые переменные | var(--radius-md), var(--transition-fast) в hero.css |

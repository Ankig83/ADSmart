# Отчёт Button v2

## 1. Удалённые стили

- hero__btn, hero__btn--primary, hero__btn--outline
- cta-form__submit, cta-form__link
- demo-btn, demo-btn--primary, demo-btn--outline
- demo-billboards-hero__btn, demo-billboards-contact__btn
- demo-transport-hero__btn, demo-transport-contact__btn
- demo-radio-hero__btn (--primary, --outline), demo-radio-cta__submit
- demo-elevators-hero__btn (--primary, --outline), demo-elevators-contact__btn
- demo-ai-hero__btn (--primary, --outline), demo-ai-cta__btn (--primary, --outline)
- demo-design-hero__btn (--primary, --outline), demo-design-cta__btn (--primary, --outline)
- demo-prod-hero__btn (--primary, --outline), demo-prod-contact__btn
- demo-tg-hero__btn (--primary, --outline), demo-tg-contact__btn
- demo-print-hero__btn (--primary, --outline), demo-print-contact__btn
- demo-lead-success__btn, demo-cookie__btn
- demo-home-calc__close (внешний вид), demo-home-calc__btn (внешний вид)
- demo-ad__btn, demo-contact__btn, demo-404__btn
- demo-menu__toggle (внешний вид)
- c-toast__close
- c-btn (вся система)

**Удалено:** ~120+ правил (базовые + media queries + lock-файлы)

## 2. Оставшиеся стили

Файл `static/css_v2/components/button.css`:
- .button (базовый)
- .button--sm, .button--md, .button--lg
- .button--primary, .button--secondary, .button--outline, .button--ghost
- hover для каждого типа

**Осталось:** 1 файл, 12 правил

## 3. Fixed height

**НЕТ** — в button.css v2 нет height, min-height

## 4. Border-radius

**3 значения:**
- button--sm: 24px
- button--md: 32px
- button--lg: 40px

## 5. Padding

**3 набора:**
- button--sm: 8px 16px
- button--md: 12px 20px
- button--lg: 16px 24px

## 6. Inline-стили

**НЕТ** — в шаблонах нет style= на кнопках

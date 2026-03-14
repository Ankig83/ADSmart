# Алгоритм переноса страницы в css_v2

Пошаговый алгоритм миграции страницы с legacy `static/css/pages/*` в `static/css_v2/pages/*` без потери адаптивности.

---

## 1. Подготовка

1. **Определи legacy-файлы** страницы:
   - `css/pages/<page>.css`
   - `css/pages/<page>-tablet-lock.css`
   - `css/pages/<page>-mobile-lock.css`
   - `css/pages/<page>-tablet-overrides.css` (если есть)

2. **Собери эталон**: визуально проверь страницу на 440px, 834px и 1440px. Зафиксируй, как должны выглядеть hero, секции, CTA, футер.

---

## 2. Создай новый файл

Создай `static/css_v2/pages/<page>.css` (можно пустой или с базовыми правилами).

---

## 3. Подключи параллельно (без удаления legacy)

В шаблоне страницы:

```html
{% block page_css %}
  <link rel="stylesheet" href="{% static 'css_v2/pages/<page>.css' %}" />
  <link rel="stylesheet" href="{% static 'css/pages/<page>.css' %}" />
  <!-- остальные legacy... -->
{% endblock %}
```

Новый файл подключай **перед** legacy. Визуально ничего не должно измениться.

---

## 4. Перенеси правила по порядку

### 4.1. Базовые (вне media)

- `.app`, `.app__main` (если используются)
- Контейнер страницы (например `.demo-<page>`): `width`, `max-width`, `background`, `overflow`
- Страничные модификаторы (цвета, мелкие правки)

### 4.2. Mobile (max-width: 833px)

Перенеси из `*-mobile-lock.css`:

- Hero: позиционирование, размеры, overlay
- Блоки секций: padding, gap, grid/flex
- Кнопки, типографика
- CTA / контакт (если есть)

### 4.3. Tablet (834–1439px)

Объедини правила из основного `*.css` и `*-tablet-lock.css`, `*-tablet-overrides.css`. При конфликтах приоритет — у более позднего в cascade.

### 4.4. Desktop (1440px+)

Перенеси desktop-правила из основного файла.

---

## 5. Структура нового файла

```
/* <page>.css — страница X. Эталон: 440, 834, 1440 */

/* ─── Базовые ─── */
.app { ... }
.demo-<page> { ... }

/* ─── Desktop 1440+ ─── */
@media (min-width: 1440px) { ... }

/* ─── Mobile ≤833 ─── */
@media (max-width: 833px) { ... }

/* ─── Tablet 834–1439 ─── */
@media (min-width: 834px) and (max-width: 1439px) { ... }
```

Порядок media не критичен (специфичность одинакова), но удобнее: base → desktop → mobile → tablet.

---

## 6. Скоуп через класс страницы

Используй родительский класс (например `.demo-ai`, `.demo-home`), чтобы не трогать другие страницы:

```css
.demo-ai .hero-with-figure { ... }
.demo-ai .cta-card { ... }
```

Глобальные правила (`.app`, `body`) оставляй без скоупа.

---

## 7. Убрать !important

- В legacy часто `!important` из‑за cascade.
- В новом файле, без конкурирующих правил, достаточно специфичности (`.demo-page .component`).
- Если что‑то ломается — можно временно вернуть `!important`, но лучше повысить специфичность.

---

## 8. Отключить legacy и проверить

1. Удали из `{% block page_css %}` все ссылки на legacy-файлы.
2. Оставь только:  
   `{% static 'css_v2/pages/<page>.css' %}`
3. Пройди все брейкпоинты: 320, 440, 600, 834, 1024, 1440.
4. Убедись, что hero, секции, CTA, футер совпадают с эталоном.

---

## 9. Удалить legacy-файлы

Когда всё ок:

```bash
rm static/css/pages/<page>.css
rm static/css/pages/<page>-mobile-lock.css
rm static/css/pages/<page>-tablet-lock.css
rm static/css/pages/<page>-tablet-overrides.css  # если был
```

Сделай коммит.

---

## 10. Пример: AI ассистенты

- Legacy: `ai_assistants.css`, `ai_assistants-tablet-lock.css`, `ai_assistants-mobile-lock.css`
- Новый: `css_v2/pages/ai_assistants.css`
- Объём: ~250 строк, mobile + tablet + desktop
- Результат: один файл, без `*-lock`, без legacy.

---

## Чеклист

- [ ] Эталон зафиксирован (440, 834, 1440)
- [ ] Создан `css_v2/pages/<page>.css`
- [ ] Подключён параллельно с legacy
- [ ] Перенесены базовые правила
- [ ] Перенесён mobile
- [ ] Перенесён tablet
- [ ] Перенесён desktop
- [ ] Legacy отключены
- [ ] Визуально всё совпадает
- [ ] Legacy-файлы удалены
- [ ] Коммит сделан

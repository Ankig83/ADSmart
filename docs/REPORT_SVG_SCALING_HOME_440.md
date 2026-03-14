# Отчёт: Масштабируемость SVG-блока Home 440 (demo-tech19) vs Radio (ai-result)

## Цель
Блок «Умные технологии, которые работают на вас» (demo-tech19) на Home mobile 440 должен масштабироваться так же, как блок «Эфирный ролик + AI-ассистент» (ai-result) на Radio.

---

## 1. Radio (ai-result) — рабочая эталонная реализация

### HTML-структура
```html
<section class="ai-result">
  <div class="ai-result__inner">
    <h2 class="ai-result__title">...</h2>
    <div class="ai-visual">
      <div class="ai-visual__container">
        <img class="ai-visual__diagram" src="Group 834.svg" width="426" height="361" />
      </div>
    </div>
    <div class="ai-result__card">...</div>
  </div>
</section>
```

### CSS (ai-result.css)
| Селектор | Свойства, обеспечивающие масштабирование |
|----------|------------------------------------------|
| `.ai-visual` | `width: 100%`, `max-width: 800px`, `margin: 0 auto` |
| `.ai-visual__container` | `position: relative`, `width: 100%`, `overflow: hidden` |
| `.ai-visual__diagram` | `display: block`, `width: 100%`, `max-width: 100%`, `height: auto`, `object-fit: contain` |

### Ключевые моменты
- Контейнер `.ai-visual__container` имеет **явную ширину 100%**
- Картинка получает `width: 100%`, `height: auto` — fluid-масштабирование
- Родитель `.ai-result__inner` — flex column, `align-items: center`

---

## 2. Home (demo-tech19) — текущая реализация

### HTML-структура
```html
<section class="demo-tech19">
  <div class="demo-tech19__inner">
    <h2 class="demo-tech19__title">...</h2>
    <div class="demo-tech19__left">
      <div class="demo-tech19__glow"></div>
      <picture class="demo-tech19__chip">...</picture>
      <div class="demo-tech19__diagram">
        <img class="demo-tech19__diagram-img" src="home_svg.svg" />
      </div>
      <div class="demo-tech19__features">...</div>
    </div>
    <aside class="demo-tech19__card">...</aside>
  </div>
</section>
```

### Проблемы
1. **`.demo-tech19__left`** — `max-width: 413px` жёстко ограничивает ширину; при viewport 320–440 нет плавного fluid-масштабирования как у Radio.
2. **Отсутствие обёртки-контейнера** — в Radio есть `.ai-visual__container` с `width: 100%` и `overflow: hidden`; у Home `.demo-tech19__diagram` напрямую содержит img без такой обёртки.
3. **Flex и width** — `.demo-tech19__left` с `display: flex` и `justify-content: center` может приводить к тому, что flex-потомок не получает явной ширины для корректного масштабирования img.

---

## 3. Файлы, влияющие на demo-tech19 / home_svg

| Файл | Медиа | Влияние |
|------|-------|---------|
| `static/css/pages/home.css` | `@media (min-width: 834px)` | Базовые стили desktop/tablet — **на mobile 440 НЕ применяются** |
| `static/css/pages/home-tablet-overrides.css` | `@media (min-width: 834px) and (max-width: 1439px)` | Таблет — **на mobile 440 НЕ применяются** |
| `static/css/pages/home-tablet-lock.css` | `@media (min-width: 834px) and (max-width: 1439px)` | Таблет — **на mobile 440 НЕ применяются** |
| **`static/css/pages/home-mobile-lock.css`** | `@media (max-width: 833px)` | **Основной файл для mobile 440** — переопределяет demo-tech19, __left, __diagram, __diagram-img |
| `static/css/tablet-770.css` | `@media (min-width: 834px) and (max-width: 1439px)` | Таблет — **на mobile 440 НЕ применяется** |
| `static/css/base.css` (через main) | — | `img, svg, video { max-width: 100%; height: auto }` — применяется глобально |

### Порядок загрузки CSS (home.html)
1. `css_v2/main.css` (включает base, reset, ai-result, tablet-770 и др.)
2. `css/pages/home.css`
3. `css/pages/home-tablet-overrides.css`
4. `css/pages/home-tablet-lock.css`
5. `css/pages/home-mobile-lock.css` ← **последний для mobile, имеет приоритет**

---

## 4. Решение: привести Home mobile к структуре Radio

### Изменения в `home-mobile-lock.css`

1. **`.demo-tech19__left`**  
   - Убрать жёсткий `max-width: 413px`.  
   - Заменить на fluid: `max-width: min(100%, clamp(288px, calc(413 * 100vw / 440), 413px))` для эталонного масштаба 320→440.

2. **`.demo-tech19__diagram`**  
   - Добавить обёртку-поведение как у `.ai-visual__container`:  
     `position: relative`, `width: 100%`, `overflow: hidden`.

3. **`.demo-tech19__diagram-img`**  
   - Полностью совпасть с `.ai-visual__diagram`:  
     `display: block`, `width: 100%`, `max-width: 100%`, `height: auto`, `object-fit: contain`.

4. **Совместимость flex**  
   - Убедиться, что диаграмма не сжимается некорректно:  
     `.demo-tech19__diagram { flex: 1 1 100%; min-width: 0; }`  
     (если нужна стабильная работа во flex-контейнере).

---

## 5. Итог и внесённые правки

- **Эталон**: Radio `ai-result` / `ai-visual__container` / `ai-visual__diagram`.
- **Основной файл для правок**: `static/css/pages/home-mobile-lock.css`.
- **Внесённые изменения** (в `home-mobile-lock.css`):
  - `.demo-tech19__left`: `max-width: 413px` заменён на `max-width: min(100%, clamp(288px, calc(413 * 100vw / 440), 413px))` для fluid 320→440.
  - `.demo-tech19__diagram`: добавлены `position: relative`, `overflow: hidden`, `flex: 1 1 100%`, `min-width: 0` по аналогии с `.ai-visual__container`.
  - `.demo-tech19__diagram-img`: добавлены `max-width: 100%`, `margin: 0 auto`, `object-fit: contain` по аналогии с `.ai-visual__diagram`.

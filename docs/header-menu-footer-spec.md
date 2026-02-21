## Figma → Django Templates + чистый CSS — сгенерированная спецификация

Источник: `design/figma-nodes.json` (Figma API nodes dump).
Все числовые значения ниже взяты из JSON; роли/семантика (bg/surface/primary) требуют верификации по стилям/Dev Mode.

### A) Карта страниц (по frames)

### Breakpoints / форматы

| Frame width (px) | Count |
|---:|---:|

### B) Tokens (сырые данные из макета)

#### Colors (top 40 по частоте)
| Color | Count | Where (top) |
|---|---:|---|

#### Typography (уникальные TEXT стили)
| font-family | size | weight | line-height | letter-spacing | count |
|---|---:|---:|---|---|---:|

#### Spacing (Auto-layout paddings / gaps)
| px | count |
|---:|---:|

#### Radius
| px | count |
|---:|---:|

#### Shadows / effects (top)

### C) Компоненты (INSTANCE из макета)

| Instance name | componentId | count |
|---|---|---:|

### D) Таблица сборки (page → компоненты → данные)

| Page (node) | Template | Components (top-level instances) | Data (mocks) |
|---|---|---|---|

### E) Ассеты (image fills по imageRef)

Найдено imageRef: **0**

| Suggested path | format | density | imageRef | Where used (sample) |
|---|---|---:|---|---|

Примечание: это **image fills** (raster) по `imageRef`. Для скачивания нужен endpoint Figma API "get image fills" (URL по `imageRef`).

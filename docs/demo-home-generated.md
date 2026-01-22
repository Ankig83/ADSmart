## Figma → Django Templates + чистый CSS — сгенерированная спецификация

Источник: `design/figma-nodes.json` (Figma API nodes dump).
Все числовые значения ниже взяты из JSON; роли/семантика (bg/surface/primary) требуют верификации по стилям/Dev Mode.

### A) Карта страниц (по frames)

- **Home** (`46:562`) — 1440×6755
  - **Блоки верхнего уровня**:
    - `Rectangle` (RECTANGLE)
    - `Ваш билборд умеет принимать заказы 24/7?` (TEXT)
    - `Превращаем наружную рекламу в автономный канал продаж с AI-ассистентами. Сокращаем путь от интереса к заявке до 60 секунд` (TEXT)
    - `Меню` (INSTANCE)
    - `20251218_2113_image 1` (RECTANGLE)
    - `Desktop - 15` (FRAME)
    - `Buttons` (INSTANCE)
    - `Desktop - 16` (FRAME)
    - `Desktop - 19` (INSTANCE)
    - `Frame 427321533` (FRAME)
    - `Desktop - 20` (FRAME)
    - `Contcat us` (FRAME)
    - `Faq` (FRAME)
    - `Footer` (INSTANCE)
    - `Buttons` (INSTANCE)

- **Билборды** (`46:806`) — 1440×5402
  - **Блоки верхнего уровня**:
    - `FIGMA 1` (RECTANGLE)
    - `Frame 427321549` (FRAME)
    - `Frame 427321551` (FRAME)
    - `Меню` (INSTANCE)
    - `Desktop - 22` (FRAME)
    - `Footer` (INSTANCE)
    - `Desktop - 15` (FRAME)
    - `Group 79` (GROUP)
    - `Contcat us` (INSTANCE)
    - `Format` (FRAME)

### Breakpoints / форматы

| Frame width (px) | Count |
|---:|---:|
| 1440 | 2 |

### B) Tokens (сырые данные из макета)

#### Colors (top 40 по частоте)
| Color | Count | Where (top) |
|---|---:|---|
| `#ffffff` | 242 | TEXT:156, INSTANCE:54, VECTOR:23, FRAME:stroke:7, INSTANCE:stroke:1 |
| `#ffb661` | 67 | VECTOR:47, VECTOR:stroke:10, ELLIPSE:10 |
| `#19161c` | 40 | FRAME:21, INSTANCE:19 |
| `#000000` | 36 | VECTOR:19, FRAME:9, TEXT:5, INSTANCE:3 |
| `#ff7b00` | 35 | FRAME:stroke:16, TEXT:9, FRAME:5, VECTOR:stroke:4, RECTANGLE:1 |
| `#14f195` | 5 | INSTANCE:5 |
| `#c4c4c4` | 2 | TEXT:2 |

#### Typography (уникальные TEXT стили)
| font-family | size | weight | line-height | letter-spacing | count |
|---|---:|---:|---|---|---:|
| `Poppins` | 16 | 400 | `24px` | `0` | 30 |
| `Poppins` | 18 | 400 | `23.4px` | `0` | 20 |
| `Poppins` | 22 | 400 | `28.6px` | `0` | 13 |
| `Poppins` | 48 | 600 | `62.4px` | `0` | 11 |
| `Poppins` | 24 | 700 | `31.2px` | `0` | 10 |
| `Outfit` | 24 | 700 | `30.24px` | `0` | 10 |
| `Outfit` | 18 | 300 | `25.2px` | `0` | 10 |
| `Poppins` | 16 | 400 | `26px` | `0` | 9 |
| `Poppins` | 24 | 600 | `31.2px` | `0` | 8 |
| `Poppins` | 22 | 400 | `96px` | `0` | 7 |
| `Poppins` | 18 | 500 | `20px` | `0` | 6 |
| `Poppins` | 16 | 700 | `20.8px` | `0` | 6 |
| `Poppins` | 18 | 400 | `27px` | `0` | 6 |
| `Poppins` | 24 | 700 | `36px` | `0` | 5 |
| `Poppins` | 18 | 700 | `23.4px` | `0` | 4 |
| `Poppins` | 18 | 600 | `26px` | `0` | 3 |
| `Poppins` | 18 | 600 | `23.4px` | `0` | 3 |
| `Poppins` | 16 | 400 | `20.8px` | `0` | 3 |
| `Poppins` | 21 | 400 | `31.5px` | `0` | 2 |
| `Poppins` | 48 | 800 | `62.4px` | `0` | 1 |
| `Poppins` | 22 | 500 | `96px` | `0` | 1 |
| `Poppins` | 38 | 600 | `49.4px` | `0` | 1 |
| `Poppins` | 65 | 800 | `84.5px` | `0` | 1 |
| `Poppins` | 24 | 500 | `36px` | `0` | 1 |
| `Poppins` | 28 | 600 | `36.4px` | `0` | 1 |

#### Spacing (Auto-layout paddings / gaps)
| px | count |
|---:|---:|
| 18 | 14 |
| 22 | 13 |
| 12 | 10 |
| 14 | 7 |
| 176 | 4 |
| 100 | 4 |
| 17 | 4 |
| 422 | 4 |
| 10 | 3 |
| 36 | 3 |
| 8 | 3 |
| 7 | 3 |
| 41 | 2 |
| 4 | 2 |
| 68 | 2 |
| 26 | 2 |
| 53 | 2 |
| 30 | 1 |

#### Radius
| px | count |
|---:|---:|
| 12 | 32 |
| 1000 | 12 |
| 64 | 4 |
| 22 | 4 |
| 8 | 4 |
| 100 | 3 |

#### Shadows / effects (top)

### C) Компоненты (INSTANCE из макета)

| Instance name | componentId | count |
|---|---|---:|
| `Component 3` | `1:18` | 10 |
| `Blok` | `1:138` | 8 |
| `chevron-down` | `46:463` | 5 |
| `Format` | `46:482` | 4 |
| `Buttons` | `1:42` | 3 |
| `Blok` | `46:270` | 3 |
| `plus` | `1:172` | 3 |
| `Меню` | `1:5` | 2 |
| `chevron-down` | `1:3` | 2 |
| `Frame` | `46:362` | 2 |
| `Footer` | `1:188` | 2 |
| `Frame` | `1:175` | 2 |
| `Frame` | `1:179` | 2 |
| `Frame` | `1:183` | 2 |
| `Frame 427321510` | `1:22` | 2 |
| `Frame 427321511` | `1:22` | 2 |
| `Frame` | `1:129` | 2 |
| `Frame 427321512` | `1:22` | 2 |
| `Frame` | `1:78` | 2 |
| `Frame 427321513` | `1:22` | 2 |
| `Eye` | `1:14` | 2 |
| `Frame 427321514` | `1:22` | 2 |
| `Button` | `1:127` | 2 |
| `Frame` | `46:374` | 1 |
| `Frame` | `46:378` | 1 |
| `Frame` | `46:382` | 1 |
| `Frame` | `46:429` | 1 |
| `Frame` | `46:433` | 1 |
| `Frame` | `46:437` | 1 |
| `Frame` | `46:440` | 1 |

### D) Таблица сборки (page → компоненты → данные)

| Page (node) | Template | Components (top-level instances) | Data (mocks) |
|---|---|---|---|
| `Home` | `templates/pages/home.html` | `Меню`, `Buttons`, `Desktop - 19`, `Footer`, `Buttons` | TBD |
| `Билборды` | `templates/pages/asset.html` | `Меню`, `Footer`, `Contcat us` | TBD |

### E) Ассеты (image fills по imageRef)

Найдено imageRef: **6**

| Suggested path | format | density | imageRef | Where used (sample) |
|---|---|---:|---|---|
| `static/assets/images/20251218-2113-image-1-993807bd.png` | `png` | 2x | `993807bd9d92a0912ec86fa93d7434c705f93bd5` | Home · Home / 20251218_2113_image 1 · 708×741 |
| `static/assets/images/figma-1-1d61b4da.png` | `png` | 2x | `1d61b4da92c8559bd009e1498428ec3e6ecbfa4e` | Билборды · Билборды / FIGMA 1 · 1440×751 |
| `static/assets/images/frame-427321580-526249db.png` | `png` | 2x | `526249db7a87ec7c96fbcf90d2b3f3247c19a956` | Билборды · Билборды / Format / Наши форматы и интеллектуальные решения / Format / Frame 427321580 · 421×271 |
| `static/assets/images/image-12-cf0ca1e7.png` | `png` | 2x | `cf0ca1e77aaf8f8f8f05f9c4a85fe5fb72ac8f16` | Билборды · Билборды / Меню / image 12 · 74×46 |
| `static/assets/images/vecteezy-3d-illustration-of-a-growing-bar-graph-57642939-1-e21d9191.png` | `png` | 2x | `e21d919160abc8b01b13ecc733505f8489db7b89` | Home · Home / Frame 427321533 / vecteezy_3d-illustration-of-a-growing-bar-graph_57642939 1 · 397×397 |
| `static/assets/images/vecteezy-wonderful-classic-a-levitating-microchip-with-visible-exclusive-60335987-1-d2923d42.png` | `png` | 2x | `d2923d42ec66949bb7881908cdde6127e8a2e76a` | Home · Home / Desktop - 19 / Group 70 / vecteezy_wonderful-classic-a-levitating-microchip-with-visible-exclusive_60335987 1 · 274×274 |

Примечание: это **image fills** (raster) по `imageRef`. Для скачивания нужен endpoint Figma API "get image fills" (URL по `imageRef`).

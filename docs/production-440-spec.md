## Figma → Django Templates + чистый CSS — сгенерированная спецификация

Источник: `design/figma-nodes.json` (Figma API nodes dump).
Все числовые значения ниже взяты из JSON; роли/семантика (bg/surface/primary) требуют верификации по стилям/Dev Mode.

### A) Карта страниц (по frames)

- **Производство рекламы** (`140:6944`) — 440×4791
  - **Блоки верхнего уровня**:
    - `Меню` (INSTANCE)
    - `#2` (FRAME)
    - `Blok2` (FRAME)
    - `Blok3` (FRAME)
    - `Block4` (FRAME)
    - `Blok5` (FRAME)
    - `Blok` (FRAME)
    - `Footer` (INSTANCE)
    - `StatusBar` (INSTANCE)

### Breakpoints / форматы

| Frame width (px) | Count |
|---:|---:|
| 440 | 1 |

### B) Tokens (сырые данные из макета)

#### Colors (top 40 по частоте)
| Color | Count | Where (top) |
|---|---:|---|
| `#ffffff` | 84 | TEXT:47, INSTANCE:16, VECTOR:11, FRAME:stroke:3, GROUP:2 |
| `#ffb661` | 32 | VECTOR:32 |
| `#19161c` | 21 | INSTANCE:11, FRAME:10 |
| `#000000` | 10 | FRAME:7, TEXT:2, INSTANCE:1 |
| `#ff7b00` | 10 | FRAME:stroke:6, TEXT:3, RECTANGLE:1 |
| `#c9cad6` | 4 | TEXT:4 |
| `#c4c4c4` | 3 | TEXT:3 |
| `#dadada` | 3 | VECTOR:3 |
| `#14f195` | 2 | INSTANCE:2 |
| `#ff3b30` | 2 | TEXT:1, RECTANGLE:1 |
| `#d9d9d9` | 2 | ELLIPSE:2 |
| `#71e582` | 2 | ELLIPSE:stroke:2 |
| `#3f6d34` | 1 | FRAME:1 |
| `#4a6940` | 1 | FRAME:1 |
| `#8deb92` | 1 | TEXT:1 |
| `#0e101f` | 1 | ELLIPSE:1 |
| `#01031a` | 1 | ELLIPSE:1 |

#### Typography (уникальные TEXT стили)
| font-family | size | weight | line-height | letter-spacing | count |
|---|---:|---:|---|---|---:|
| `Poppins` | 16 | 400 | `24px` | `0` | 13 |
| `Poppins` | 18 | 700 | `23.4px` | `0` | 8 |
| `Poppins` | 24 | 600 | `31.2px` | `0` | 5 |
| `Poppins` | 16 | 400 | `20.8px` | `0` | 5 |
| `Poppins` | 22 | 400 | `96px` | `0` | 4 |
| `Poppins` | 14 | 400 | `18.2px` | `0` | 4 |
| `Poppins` | 14 | 400 | `21px` | `0` | 3 |
| `Poppins` | 18 | 400 | `23.4px` | `0` | 3 |
| `Poppins` | 16 | 500 | `20.8px` | `0` | 3 |
| `Poppins` | 16 | 500 | `24px` | `0` | 2 |
| `Poppins` | 18 | 600 | `26px` | `0` | 2 |
| `SF Pro Text` | 15 | 400 | `22px` | `0` | 2 |
| `Poppins` | 32 | 800 | `41.6px` | `0` | 1 |
| `Poppins` | 20 | 600 | `26px` | `0` | 1 |
| `Poppins` | 18 | 500 | `20px` | `0` | 1 |
| `Poppins` | 28 | 600 | `36.4px` | `0` | 1 |
| `Poppins` | 22 | 700 | `28.6px` | `0` | 1 |
| `SF Pro Text` | 17 | 600 | `22px` | `0` | 1 |
| `SF Pro Text` | 11 | 600 | `22px` | `0` | 1 |

#### Spacing (Auto-layout paddings / gaps)
| px | count |
|---:|---:|
| 16 | 19 |
| 44 | 10 |
| 10 | 7 |
| 24 | 6 |
| 4 | 4 |
| 18 | 4 |
| 22 | 4 |
| 17 | 4 |
| 42 | 3 |
| 8 | 3 |
| 20 | 3 |
| 14 | 2 |
| 32 | 2 |
| 41 | 1 |
| 36 | 1 |
| 12 | 1 |
| 39 | 1 |
| 35 | 1 |

#### Radius
| px | count |
|---:|---:|
| 12 | 12 |
| 1000 | 4 |
| 4 | 4 |
| 100 | 2 |
| 64 | 2 |
| 2 | 2 |
| 32 | 1 |
| 40 | 1 |

#### Shadows / effects (top)

### C) Компоненты (INSTANCE из макета)

| Instance name | componentId | count |
|---|---|---:|
| `Blok` | `133:5326` | 4 |
| `Blok` | `133:5318` | 3 |
| `Footer` | `140:7056` | 2 |
| `Меню` | `114:3086` | 1 |
| `chevron-down` | `1:3` | 1 |
| `menu` | `114:3082` | 1 |
| `Buttons` | `114:3036` | 1 |
| `Buttons` | `114:3038` | 1 |
| `Icon` | `133:4980` | 1 |
| `Frame` | `133:5113` | 1 |
| `Frame` | `133:5116` | 1 |
| `Frame` | `133:5206` | 1 |
| `Location` | `133:5138` | 1 |
| `Printer` | `133:5212` | 1 |
| `Gift` | `133:5216` | 1 |
| `clipboard` | `133:5219` | 1 |
| `File` | `133:5223` | 1 |
| `Settings` | `133:5227` | 1 |
| `Tool` | `133:5230` | 1 |
| `Button` | `1:127` | 1 |
| `Footer` | `140:7039` | 1 |
| `Footer` | `140:7060` | 1 |
| `Frame` | `133:5075` | 1 |
| `Frame` | `133:5079` | 1 |
| `Frame` | `133:5083` | 1 |
| `StatusBar` | `114:3174` | 1 |
| `_StatusBar-battery` | `114:3099` | 1 |
| `Silent - Right` | `114:3133` | 1 |
| `Silent - Left` | `114:3135` | 1 |
| `Charging - Right` | `114:3138` | 1 |

### D) Таблица сборки (page → компоненты → данные)

| Page (node) | Template | Components (top-level instances) | Data (mocks) |
|---|---|---|---|
| `Производство рекламы` | `templates/pages/asset.html` | `Меню`, `Footer`, `StatusBar` | TBD |

### E) Ассеты (image fills по imageRef)

Найдено imageRef: **6**

| Suggested path | format | density | imageRef | Where used (sample) |
|---|---|---:|---|---|
| `static/assets/images/2-55cbcda6.png` | `png` | 2x | `55cbcda6b82fb7a3a04f9f18ae8871b9f8a4b7fc` | Производство рекламы · Производство рекламы / #2 · 440×483 |
| `static/assets/images/frame-427321574-57a9360d.png` | `png` | 2x | `57a9360d81b4a8d410d5674025ec2143e3fb1798` | Производство рекламы · Производство рекламы / Blok5 / Blok2 / Frame 427321574 · 408×238 |
| `static/assets/images/image-12-cf0ca1e7.png` | `png` | 2x | `cf0ca1e77aaf8f8f8f05f9c4a85fe5fb72ac8f16` | Производство рекламы · Производство рекламы / Меню / image 12 · 58×36 |
| `static/assets/images/image-3-9ca4e461.png` | `png` | 2x | `9ca4e4612e3b60536497623e64f4930c8655fc60` | Производство рекламы · Производство рекламы / StatusBar / Island / Airpods - Left / image 3 · 10×17 |
| `static/assets/images/image-4-4d62487d.png` | `png` | 2x | `4d62487d8c8457a422086f0b9e859cf15c888a20` | Производство рекламы · Производство рекламы / StatusBar / Island / Airpods - Left / image 4 · 11×18 |
| `static/assets/images/vecteezy-ai-chip-with-half-brain-symbolizing-artificial-intelligence-71143548-1-885f642f.png` | `png` | 2x | `885f642f9404148674ecf0f14f83fbd7479bb4f4` | Производство рекламы · Производство рекламы / #2 / AI / vecteezy_ai-chip-with-half-brain-symbolizing-artificial-intelligence_71143548 1 · 274×274 |

Примечание: это **image fills** (raster) по `imageRef`. Для скачивания нужен endpoint Figma API "get image fills" (URL по `imageRef`).

# Telegram Mobile Page — Figma Design Metrics (440×5404)

**Source:** Figma node **140:6684** (Телеграм), fileKey `RgixkfQjBcvWPRvylxy0u8`  
**Export:** `design/telegram-440-nodes.json` (Figma API dump), `design/figma-metrics.json`

---

## Page & Block Node Mapping

| Block        | Node ID   | Figma Name | Size (W×H)     |
|-------------|-----------|------------|----------------|
| Page        | 140:6684  | Телеграм   | 440×5404       |
| Меню        | 140:6685  | Меню       | 440×70 (shared)|
| Hero #2     | 140:6686  | #2         | 440×483        |
| Blok2       | 140:6699  | Blok2      | 440×~580       |
| Blok3       | 140:6706  | Blok3      | 440×~680       |
| Block4      | 140:6715  | Block4     | 440×~620       |
| Blok5       | 140:6743  | Blok5      | 440×~530       |
| Blok (CTA)  | 140:6769  | Blok       | 440×~870       |
| Footer      | 140:6785  | Footer     | 440×505 (shared)|

*Shared: Меню and Footer use the same 440×70 / 440×505 components across mobile pages.*

---

## Global Layout (from absoluteBoundingBox)

Figma canvas origin for this frame: content left **x=12068**, horizontal padding **16px** each side.

- **Content width:** 408px  
- **Section padding:** paddingLeft/Right **16px**, paddingTop/Bottom **44px** (main section frames)

### Y positions (relative to page top, from Figma absoluteBoundingBox)

| Element              | Node ID   | y      | Height / Notes              |
|----------------------|-----------|--------|-----------------------------|
| Hero image           | 140:6689  | 9342   | 267×293                     |
| Hero title           | 140:6694  | 9368   | 408×84, fontSize 24        |
| Blok2 title          | 140:6701  | 9774   | 408×48, fontSize 24        |
| Blok3 title          | 140:6709  | 10661  | 408×48, fontSize 24        |
| Block4 title         | 140:6717  | 11642  | 408×~62, fontSize 24       |
| Blok5 title          | 140:6745  | 12365  | 409×~62, fontSize 24       |

**Implied section spacing (vertical gaps):**
- Hero → Blok2: ~63px  
- Blok2 → Blok3: ~89px  
- Blok3 → Block4: ~98px  
- Block4 → Blok5: ~72px  

---

## Hero #2 (140:6686) — 440×483

| Element       | x   | y   | width | height | fontSize |
|---------------|-----|-----|-------|--------|----------|
| Hero frame    | 0   | 70  | 440   | 483    | —        |
| Title         | 16  | ~98 | 408   | 84     | 24px     |
| Subtitle      | 16  | —   | 408   | —      | 16px     |
| Hero image    | —   | —   | 267   | 293    | —        |
| CTA buttons   | 16  | —   | —     | —      | 17px     |

- **paddingTop/Bottom:** 44px (Frame 427321552)  
- **itemSpacing:** 41px (title → buttons)  
- **Font:** Poppins ExtraBold (24), Poppins Regular (16, 17)  

---

## Blok2 (140:6699) — "Telegram центр цифровой гравитации бизнеса"

| Element    | x   | y   | width | height | fontSize |
|------------|-----|-----|-------|--------|----------|
| Title      | 16  | ~44 | 408   | 48     | 24px     |
| Cards      | 16  | —   | 408   | —      | —        |

- **Section padding:** 16px L/R, 44px T/B  
- **itemSpacing:** 42px (title → cards), 22px (between cards)  
- **Card padding:** 14px L/R, 28px T/B; itemSpacing 10px  
- **Title:** Poppins SemiBold 24px, lineHeight 31.2px, letterSpacing -0.72  

---

## Blok3 (140:6706) — "Комплексный подход: от создания сообщества до закрытия сделки"

| Element    | x   | y   | width | height | fontSize |
|------------|-----|-----|-------|--------|----------|
| Title      | 16  | ~44 | 408   | 48     | 24px     |
| Cards      | 16  | —   | 408   | —      | 18px     |

- **Section padding:** 16px L/R, 44px T/B  
- **itemSpacing:** 42px (title → cards), 22px (between cards)  
- **Card padding:** 14px L/R, 35px T/B; itemSpacing 12px  

---

## Block4 (140:6715) — "Почему это работает там, где другие каналы «молчат»"

| Element    | x   | y   | width | height | fontSize |
|------------|-----|-----|-------|--------|----------|
| Title      | 16  | ~44 | 408   | ~62    | 24px     |
| Grid       | 16  | —   | 408   | —      | 18px     |

- **Section padding:** 16px L/R, 44px T/B  
- **itemSpacing:** 42px (title → grid), 22px (between items)  
- **Icon cells:** padding 14px L/R, 35px T/B; itemSpacing 12px  

---

## Blok5 (140:6743) — "Экспертиза там, где другие жмут «Запустить рекламу»"

| Element    | x   | y   | width | height | fontSize |
|------------|-----|-----|-------|--------|----------|
| Title      | 16  | ~44 | 409   | ~62    | 24px     |
| Blocks     | 16  | —   | 408   | —      | 18px     |

- **Section padding:** 16px L/R, 44px T/B  
- **itemSpacing:** 42px (title → blocks), 22px (between blocks)  
- **Block header:** padding 10px 12px; fontSize 18px  
- **Block cells:** padding 3px 12px; min-height ~82px; background #19161c  

---

## Blok (140:6769) — Contact / "Начните диалог с клиентами в самом перспективном канале"

| Element       | x   | y   | width | height | fontSize |
|---------------|-----|-----|-------|--------|----------|
| Title         | 16  | ~44 | 408   | —      | 24px     |
| Description    | 16  | —   | 408   | —      | 16px     |
| CTA button     | 16  | —   | 408   | ~55    | 17px     |
| Form fields    | 16  | —   | 408   | ~50    | 15px     |
| Submit button  | 16  | —   | 408   | ~55    | 17px     |

- **itemSpacing:** 17px (title→desc), 16px (between fields), 12px (buttons)  
- **Form container:** padding ~20–30px  

---

## Footer (140:6785) — 440×505

- Shared component; logo 58×36, footer links fontSize 14–18px  
- **Padding:** per `design/demo-footer.css` — Figma 140:7025  

---

## Typography Summary

| Use            | Font         | Size | Line height | Letter spacing |
|----------------|--------------|------|-------------|----------------|
| Hero title     | Poppins ExBd | 24px | 31.2px      | —              |
| Hero subtitle  | Poppins      | 16px | —           | —              |
| Section titles | Poppins SemiBold | 24px | 31.2px  | -0.72          |
| Card titles    | Poppins      | 18px | 23.4px      | —              |
| Body/cards     | Poppins      | 16px | 18.2px      | —              |
| CTA buttons    | Poppins      | 17px | —           | —              |
| Placeholders   | Poppins      | 15px | —           | —              |

---

## Key Padding & Spacing

| Context              | paddingTop | paddingBottom | paddingLeft | paddingRight | itemSpacing |
|----------------------|------------|--------------|------------|-------------|-------------|
| Section (Blok2–Blok5)| 44px       | 44px         | 16px       | 16px        | 42 (title→content), 22 (cards) |
| Hero content frame   | 44px       | 44px         | 16px       | 16px        | 41          |
| Feature cards        | 28px       | 28px         | 14px       | 14px        | 10–12       |
| Blok5 block header   | 10px       | 10px         | 12px       | 12px        | —           |
| Blok5 block cells    | 3px        | 3px          | 12px       | 12px        | —           |
| CTA buttons         | 16px       | 16px         | 32px       | 32px        | 10          |

---

## Design Tokens (from production-440-metrics)

- **Primary:** #ff7b00, #ffb661  
- **Background:** #000000, #19161c  
- **Text:** #ffffff, #c4c4c4, #c9cad6  

---

## Files & References

- `design/telegram-440-nodes.json` — full Figma node dump  
- `design/figma-metrics.json` — pages list, image plan  
- `design/figma_node_ids.txt` — includes 140:6684  
- `docs/figma-spec.md` — fileKey, tokens  
- Print page reference: `design/print-440-6863-hero.json` (similar Hero 440×483)

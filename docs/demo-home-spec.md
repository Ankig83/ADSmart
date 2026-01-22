## DEMO (Figma) → Home (/home/) — перенос в Django Templates

Источник nodes:
- Hero title: `46:806`
- Menu: `46:566`
- Frame: `46:562`

Figma file key: `St9lm1ybs5FOfA1GJBVvWW`

### Как сгенерировать JSON + выгрузить картинки (через Figma API)

В терминале, где у тебя уже задан `FIGMA_TOKEN`:

```bash
cd /home/user/PycharmProjects/ADSmart
export FIGMA_FILE_KEY=St9lm1ybs5FOfA1GJBVvWW

# 1) Скачать nodes JSON по нужным id
python scripts/figma_export.py dump --ids-file design/demo_node_ids.txt --out design/demo-nodes.json

# 2) Сгенерировать спеки/метрики из JSON (без угадываний)
python scripts/figma_analyze.py --in design/demo-nodes.json --out-md docs/demo-home-generated.md --out-json design/demo-metrics.json

# 3) Скачать растровые image fills (если есть) в static/assets/images/
python scripts/figma_export.py imagefills --out design/demo-imagefills.json
python scripts/figma_export.py download-imagefills --fills design/demo-imagefills.json --plan design/demo-metrics.json
```

После этого я:
- соберу страницу `templates/pages/home.html` (route `/home/`) по структуре из `docs/demo-home-generated.md`
- подключу `static/css/pages/home.css`
- вставлю `{% static %}` ссылки на скачанные ассеты




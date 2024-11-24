# Web Crawler

## Aprašymas
Šis projektas leidžia nuskaityti duomenis iš tinklapių `lrytas.lt` ir `eurovaistine.lt`, grąžinant duomenis įvairiais formatais.

### Pavyzdys:
```python
from my_module.crawler import crawl

data = crawl(time_limit=60, source='lrytas', return_format='csv')
# Vod.Film Test Automation

Automatyzacja testów dla strony Vod.Film wykorzystująca Playwright i Python.

## Wybrana technologia: Playwright

**Uzasadnienie wyboru:**

- Szybsze wykonanie testów w porównaniu do Selenium
- Wbudowane mechanizmy oczekiwania (auto-wait)
- Łatwa obsługa iframe i popup'ów
- Wsparcie dla nowoczesnych aplikacji webowych
- Prosta konfiguracja i uruchamianie

## Wymagania

- Python 3.10+
- Playwright
- pytest

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/your-username/vod-film-tests.git
cd vod-film-tests
```

2. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

Zainstaluj przeglądarki Playwright:

```bash
playwright install
```

## Uruchomienie testów:

1. Wszystkie testy

```bash
pytest --browser chromium --browser-channel chrome -s
```

```bash
pytest
```

2. Tylko testy E2E

```bash
pytest tests/test_e2e.py --browser chromium --browser-channel chrome -s
```

```bash
pytest tests/test_e2e.py -v
```

3. Tylko testy API

```bash
pytest tests/test_api.py --browser chromium --browser-channel chrome -s
```

```bash
pytest tests/test_api.py -v
```

## Zidentyfikowany endpoint API

Endpoint: POST https://vod.film/api/search-route

Opis: Endpoint odpowiedzialny za wyszukiwanie na żywo (live search) podczas wpisywania frazy w polu wyszukiwania.

## Raporty znalezionych błędów (analiza manualna)

Raporty błędów: Manualne raporty błędów znajdują się w folderze reports/

## Uruchamianie z Docker

Budowanie i uruchamianie

```bash
docker-compose up --build
```

Tylko budowanie

```bash
docker build -t vod-film-tests
```

Uruchamianie

```bash
docker run -v $(pwd)/reports:/app/reports vod-film-testsmianie z Docker
```

## Analiza SQL (teoretyczna)

```sql
SELECT
    f.title AS film_title,
    c.name AS category_name,
    fc.created_at AS association_date
FROM films f
JOIN film_categories fc ON f.id = fc.film_id
JOIN categories c ON fc.category_id = c.id
WHERE f.title ILIKE '%the pickup%'
ORDER BY fc.created_at DESC;
```

## Problemy podczas uruchamiania testów

- podczas uruchamiana test "test_search_positive_the_pickup" przeglądarka Chromium nie odtwarza plików wideo dlatego komendy uruchamianie wszystkich testów orez osobno testów e2e i api uwzględnia uruchomienie na prawdziwym Chromie

## Struktura projektu

- `pages/` - Implementacja Page Object Model

- `tests/` - Testy E2E i API

- `reports/` - Raporty testowe i raporty błędów

- `requirements.txt` - Zależności Pythona

- `.github/workflows/` - CI/CD z GitHub Actions

- `conftest.py` - Definicje fixture dla pytest

- `pytest.ini` - Globalna konfiguracja frameworka pytest

- `Dockerfile` - Konfiguracja Docker

- `docker-compose.yml` - Konfiguracja wielokontenerowej aplikacji Docker

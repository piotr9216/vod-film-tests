import pytest


@pytest.fixture(scope="session")
def base_url():
    """Fixture zwracająca bazowy URL"""
    return "https://vod.film"

@pytest.fixture(scope="class")
def api_request_context(playwright, base_url):
    """Fixture do zarządzania kontekstem żądań API"""
    context = playwright.request.new_context(
        base_url=base_url,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Origin": base_url,
            "Referer": f"{base_url}/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        }
    )
    yield context
    context.dispose()

@pytest.fixture
def search_payload():
    """Fixture zwracająca podstawowy payload dla wyszukiwania"""
    def _payload(search_term="the pickup", locale="pl"):
        return {
            "host": "vod.film",
            "locale": locale,
            "searchTerm": search_term
        }
    return _payload

@pytest.fixture
def api_headers(base_url):
    """Fixture zwracająca nagłówki dla API"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Origin": base_url,
        "Referer": f"{base_url}/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

# Hook dla konfiguracji pytest
def pytest_configure(config):
    """Konfiguracja pytest"""
    config.addinivalue_line(
        "markers", "api: mark test as API test"
    )
    config.addinivalue_line(
        "markers", "e2e: mark test as end-to-end test"
    )
import pytest
import re
from playwright.sync_api import Page
import urllib
from pages.home_page import HomePage
from pages.movie_page import MoviePage

class TestE2ESearchAndPlay:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.home_page = HomePage(page)
        self.movie_page = MoviePage(page)
        self.home_page.navigate_to_home()

    def test_search_positive_the_pickup(self):
        query = "the pickup"

        self.home_page.open_search()
        self.home_page.search_movie(query)
        self.page.wait_for_timeout(2000)

        # sprawdź, że pierwszy wynik zawiera frazę i kliknij go
        assert self.home_page.is_query_in_first_result(query), "Expected first result to contain query"
        clicked = self.home_page.click_first_result_if_contains(query)
        self.page.wait_for_timeout(2000)
        assert clicked, "Failed to click the first matching search result"

        # walidacja na stronie filmu
        movie_title = self.movie_page.get_movie_title()
        assert query.lower() in movie_title.lower(), f"Expected '{query}' in movie title '{movie_title}'"
        print(f"Movie page loaded: {movie_title}")
        
        # sprawdź czy widoczny jest odtwarzacz wideo i odtwórz
        if self.movie_page.is_video_player_visible():
            self.movie_page.play_video()

        # czekaj na popup i kliknij przycisk "Zarejestruj się", potem sprawdź URL
        assert self.movie_page.wait_for_popup(timeout=60000), "Expected popup to appear"
        url = self.movie_page.click_register_and_capture_url(timeout=10000)
        assert url is not None, "Expected register click to navigate or change URL"

        resolved = urllib.parse.urljoin(self.page.url, url)
        # podstawowa walidacja formatu URL
        assert re.match(r"^https?://", resolved), f"Expected http(s) URL, got: {resolved}"

    def test_search_negative_no_result(self):

        query = "abcxyz123"

        self.home_page.open_search()
        self.home_page.search_movie(query)
        self.page.wait_for_timeout(2000)
        first = self.home_page.get_first_search_result()
        if first is None:
            # brak wyników = oczekiwany rezultat
            return
                # jeśli zwrócono wynik — to błąd (negatywny przypadek powinien nie znaleźć nic)
        pytest.fail(f"Unexpected search result found for '{query}': {first.get('title') if isinstance(first, dict) else first}")

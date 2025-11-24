from typing import Optional
from .base_page import BasePage

class HomePage(BasePage):
    NO_RESULTS_TEXT = "Nie znaleziono filmów i seriali dla podanej frazy"
    
    def navigate_to_home(self):
        self.page.goto("https://vod.film/")
        self.handle_cookie_popup()
    
    def open_search(self):
        search_icon = self.page.get_by_role("img", name="search icon")
        search_icon.wait_for(state="visible", timeout=10000)
        search_icon.click()
    
    def search_movie(self, query: str):
        search_box = self.page.get_by_role("textbox", name="search icon")
        search_box.wait_for(state="visible", timeout=5000)
        search_box.fill(query)
        search_box.press("Enter")

    def get_first_search_result(self) -> Optional[dict]:
        try:
            # sprawdź czy pojawił się komunikat "brak wyników"
            try:
                nores = self.page.get_by_text(self.NO_RESULTS_TEXT)
                if nores.count() > 0 and nores.first.is_visible():
                    return None
            except Exception:
                pass

            # znajdź pierwszą kartę wyników wewnątrz kontenera wyników
            card = self.page.locator("div.search__ResultsContainer-sc-87cf44fc-7 article.production__ProductionCard-sc-77f87755-0").first
            if card.count() == 0:
                return None

            # tytuł zwykle w <p class*="production__Title..."> <a>...</a>
            title_loc = card.locator("p.production__Title-sc-77f87755-7 a")
            if title_loc.count() > 0:
                title = (title_loc.first.text_content() or "").strip()
            else:
                # fallback: ostatni <a> w karcie (często link do strony filmu)
                anchors = card.locator("a")
                if anchors.count() > 0:
                    title = (anchors.nth(anchors.count() - 1).text_content() or "").strip()
                else:
                    title = ""

            # href pierwszego linku prowadzącego do zasobu (filmu/serialu)
            anchor = card.locator('a').first
            href = (anchor.get_attribute("href") or "").strip()

            return {"title": title, "href": href, "card": card}
        except Exception as e:
            print(f" Error getting first search result: {e}")
            return None

    def is_query_in_first_result(self, query: str) -> bool:
        first = self.get_first_search_result()
        if not first:
            return False
        return query.lower() in (first["title"] or "").lower()

    def click_first_result_if_contains(self, query: str) -> bool:
        first = self.get_first_search_result()
        if not first:
            return False
        if query.lower() not in (first["title"] or "").lower():
            return False
        try:
            anchor = first["card"].locator("a").first
            anchor.wait_for(state="visible", timeout=5000)
            anchor.click()
            # czekaj na nawigację do strony filmu/serialu (próbujemy filmy, potem seriale)
            try:
                self.page.wait_for_url("**/filmy/**", timeout=8000)
            except Exception:
                pass

            # czekaj na pojawienie się tytułu/sensownego elementu na stronie filmu
            title_selectors = "h1"
            try:
                self.page.wait_for_selector(title_selectors, state="visible", timeout=10000)
                return True
            except Exception:
                # fallback: poczekaj na ustanie ruchu sieciowego (dla SPA)
                try:
                    self.page.wait_for_load_state("networkidle", timeout=5000)
                    return True
                except Exception:
                    return False
        except Exception:
            return False
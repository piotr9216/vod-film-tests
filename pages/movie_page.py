from typing import Optional
from .base_page import BasePage
from playwright.sync_api import Page

class MoviePage(BasePage):
    MOVIE_TITLE  = "h1"
    VIDEO_PLAYER = "#player-container"
    PLAY_BUTTON = "button.plyr__controls__item.plyr__control[data-plyr='play']"
    POPUP = "#popup"
    
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self._popup_page = None

    def get_movie_title(self) -> str:
        return self.get_text(self.MOVIE_TITLE)
    
    def is_video_player_visible(self) -> bool:
        return self.is_element_visible(self.VIDEO_PLAYER)
    
    def play_video(self):
        try:
            self.scroll_to(self.PLAY_BUTTON)
        except Exception:
            pass
        self.click_element(self.PLAY_BUTTON)
    
    def wait_for_popup(self, timeout: int = 60000):
        try:
            self.page.wait_for_selector(self.POPUP, state="visible", timeout=timeout)
            return True
        except:
            return False
    
    def get_current_url(self) -> str:
        return self.page.url

    def click_register_and_capture_url(self, timeout: int = 10000) -> Optional[str]:
        try:
            with self.page.expect_navigation(timeout=timeout):
                self.page.click("#popup #register-now")
            return self.page.url
        except Exception:
            pass
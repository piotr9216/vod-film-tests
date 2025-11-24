from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def wait_for_element(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
    
    def click_element(self, selector: str):
        self.wait_for_element(selector)
        self.page.click(selector)
    
    def get_text(self, selector: str) -> str:
        self.wait_for_element(selector)
        return self.page.text_content(selector)
    
    def is_element_visible(self, selector: str) -> bool:
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=5000)
            return True
        except:
            return False
    
    def handle_cookie_popup(self):
        self.page.wait_for_timeout(3000)
        try:
            cookie_button = self.page.get_by_role("button", name="Zgadzam się", exact=True)
            if cookie_button.is_visible(timeout=3000):
                cookie_button.click()
                self.page.wait_for_timeout(1000)
                return True
        except:
            return False
        return False
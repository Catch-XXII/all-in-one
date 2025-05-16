from playwright.async_api import Page
from env import Config
from pages import Base


class LoginPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.tckn = page.locator("#validation-email")
        self.password = page.locator("#validation-password")
        self.kvkk = page.locator("#ReadedKvkk")
        self.company = page.locator("#Companylist")
        self.enter_button = page.get_by_role("button", name="Giriş")
        self.company_link = page.get_by_role("link", name="isnet test")

        self.main_page = page.get_by_role("link", name="Anasayfa")
        self.user_menu = page.get_by_role("link", name="Test Kullanıcısı")
        self.safe_exit = page.get_by_role("link", name="Güvenli Çıkış")

    async def fill_tckn(self):
        await self.tckn.fill(Config.TCKN)

    async def fill_password(self):
        await self.password.fill(Config.PASSWORD)

    async def check_kvkk(self):
        await self.kvkk.check()

    async def click_enter_button(self):
        await self.enter_button.click()

    async def fill_company(self):
        await self.company.fill(Config.COMPANY)

    async def do_login(self):
        await self.go_to("/login")
        await self.fill_tckn()
        await self.fill_password()
        await self.check_kvkk()
        await self.click_enter_button()
        await self.company.dblclick()
        await self.fill_company()
        await self.company_link.click()
        await self.click_enter_button()

        # Remove notifications
        await self.close_first_notification()
        await self.close_second_notification()
        await self.close_hint_notification()
        await self.close_cookie_message()

    async def do_logout(self):
        await self.main_page.click()
        await self.user_menu.click()
        await self.safe_exit.click()

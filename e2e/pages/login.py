from . import Base
from playwright.async_api import Page


class LoginPage(Base):
    def init(self, page: Page):
        super().__init__(page)

    async def do_login(self): ...
    async def do_logout(self): ...

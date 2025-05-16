from playwright.async_api import Page
from pages import Document


class FastInvoice(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create(self): ...

from playwright.async_api import Page
from pages import Base


class Document(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.e_document = "e-Belge Oluştur"
        self.e_invoice_e_archive = "e-Fatura/e-Arşiv Oluştur"
        self.e_dispatch_note = "e-İrsaliye Oluştur"
        self.e_mm = "e-MM Oluştur"
        self.e_smm = "e-SMM Oluştur"

    async def navigate_to(self, first: str, second: str):
        await self.click_menu(first)
        await self.click_menu(second)

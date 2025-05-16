from playwright.async_api import Page, expect
from pages import Document
from env import Config


class ESmm(Document):
    def __init__(self, page: Page):
        super().__init__(page)
        self.document_no: str = ""
        self.document_time = page.locator("#DocumentTime")
        self.notes = page.locator("#Notes")
        self.create_new_document_button = page.get_by_role(
            "button", name="Yeni Doküman Oluştur!"
        )

    async def select_e_invoice_customer(self):
        await self.e_archive_button.click()

    async def click_document_time(self):
        await self.document_time.click()

    async def fill_notes(self, note: str):
        await self.notes.fill(note)

    async def click_create_new_document(self):
        await self.create_new_document_button.click()

    async def return_document_number(self) -> str:
        await self.page.wait_for_selector(
            "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
        )
        await expect(self.page.get_by_text("başarıyla")).to_be_visible()

        full_text = await self.save_message.text_content()
        if full_text:
            self.document_no: str = full_text.split(":")[-1].strip()
            print(f"Document Number: {self.document_no}")
        else:
            print("Document number not found")

        await expect(self.page.get_by_role("paragraph")).to_contain_text(
            f"Doküman başarıyla kaydedilmiştir.Döküman no : {self.document_no}"
        )
        return self.document_no

    async def create(self) -> str:
        await self.navigate_to(self.e_document, self.e_smm)
        await self.click_search_recipient()
        await self.select_e_invoice_customer()
        await self.fill_title_tckn_input_field(
            recipient=Config.E_SMM_E_INVOICE_CUSTOMER
        )
        await self.click_recipient(recipient=Config.E_SMM_E_INVOICE_CUSTOMER)
        await self.click_today_button()
        await self.click_document_time()
        await self.click_next_button()
        await self.click_search_product()
        await self.fill_product(product=Config.PRODUCT)
        await self.click_product_item(product=Config.PRODUCT)
        await self.click_next_button()
        await self.click_next_button()
        await self.fill_notes(note=Config.TAX_EXEMPTION_REASON)
        await self.click_finish_button()
        await self.click_yes_save_button()
        self.document_no = await self.return_document_number()
        await self.click_create_new_document()
        return self.document_no

    async def send(self, document_no): ...

    async def download(self, document_no): ...


class Inbox(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def download(self): ...


class Credit(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def purchase(self): ...


class Reports(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def check(self): ...


class FastInvoice(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create(self): ...

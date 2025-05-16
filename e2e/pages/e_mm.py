from playwright.async_api import Page, expect
from pages import Document
from config import Config


class Emm(Document):
    def __init__(self, page: Page):
        super().__init__(page)
        self.document_no: str = ""
        self.document_time = page.locator("#DocumentTime")
        self.notes = page.locator("#Notes")
        self.drafts_button = page.get_by_role("button", name="Taslaklara git!")

    async def click_document_time(self):
        await self.document_time.click()

    async def fill_notes(self, note: str):
        await self.notes.fill(note)

    async def click_drafts_button(self):
        await self.drafts_button.click()

    async def return_document_number(self, customer_full_name) -> str:
        await expect(self.page.locator("tbody")).to_contain_text(customer_full_name)

        self.document_no = await self.page.evaluate(
            """ async () => {
            response = document.querySelector("#StagingEMMTable > tbody > tr > td:nth-child(3)").innerText;
            return response; 
            }
        """
        )
        if self.document_no:
            print(f"E-mm number: {self.document_no}")
        else:
            print("E-mm number not found")

        return self.document_no

    async def create(self) -> str:
        await self.navigate_to(self.e_document, self.e_mm)
        await self.click_search_recipient()
        await self.fill_title_tckn_input_field(Config.E_MM_CUSTOMER)
        await self.click_recipient(recipient=Config.E_MM_CUSTOMER)
        await self.click_today_button()
        await self.click_document_time()
        await self.click_next_button()
        await self.click_search_product()
        await self.fill_product(product=Config.PRODUCT)
        await self.click_product_item(product=Config.PRODUCT)
        await self.click_next_button()
        await self.fill_notes(note=Config.TAX_EXEMPTION_REASON)
        await self.click_finish_button()
        await self.click_yes_save_button()

        await self.page.wait_for_selector(
            "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
        )
        await expect(self.page.get_by_text("başarıyla")).to_be_visible()

        await self.click_drafts_button()

        self.document_no = await self.return_document_number(
            Config.E_MM_CUSTOMER_FULL_NAME
        )
        return self.document_no

    async def send(self, document_no): ...

    async def download(self, document_no): ...

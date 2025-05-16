from playwright.async_api import Page, expect
from pages import Document
from env import Config


class EInvoice(Document):
    def __init__(self, page: Page):
        super().__init__(page)
        self.document_no: str = ""
        self.e_invoice_operations: str = "e-Fatura İşlemleri"
        self.draft_e_invoice: str = "Taslak e-Faturalar"
        self.sent_e_invoice: str = "Giden e-Fatura"

        self.create_new_document_button = page.get_by_role(
            "button", name="Yeni Fatura Oluştur!"
        )

    async def select_e_invoice_customer(self):
        await self.e_archive_button.click()

    async def select_invoice_type(self, option: str = "1"):
        await self.invoice_type.select_option(option)

    async def click_create_new_document_button(self):
        await self.create_new_document_button.click()

    async def return_document_number(self) -> str:
        await self.page.wait_for_selector(
            "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
        )
        await expect(self.page.get_by_text("başarıyla")).to_be_visible()

        full_text = await self.save_message.text_content()
        if full_text:
            self.document_no: str = full_text.split(":")[-1].strip()
            print(f"Invoice Number: {self.document_no}")
        else:
            print("Invoice number not found")

        await expect(self.page.get_by_role("paragraph")).to_contain_text(
            f"Fatura başarıyla kaydedilmiştir. Fatura No. : {self.document_no}"
        )
        return self.document_no

    async def create(self) -> str:
        await self.navigate_to(self.e_document, self.e_invoice_e_archive)
        await self.click_search_recipient()
        await self.select_e_invoice_customer()
        await self.fill_title_tckn_input_field(recipient=Config.E_INVOICE_CUSTOMER)
        await self.click_recipient(recipient=Config.E_INVOICE_CUSTOMER)
        await self.select_scenario()
        await self.select_invoice_type()
        await self.click_next_button()
        await self.click_today_button()
        await self.click_same_day_button()
        await self.click_next_button()
        await self.click_search_product()
        await self.fill_product(product=Config.PRODUCT)
        await self.click_product_item(product=Config.PRODUCT)
        await self.click_next_button()
        await self.click_next_button()
        await self.click_next_button()
        await self.fill_tax_exemption_reason(Config.TAX_EXEMPTION_REASON)
        await self.click_finish_button()
        await self.click_yes_save_button()
        self.document_no = await self.return_document_number()
        await self.click_create_new_document_button()
        return self.document_no

    async def send(self, document_no):
        await self.navigate_to(self.e_invoice_operations, self.draft_e_invoice)
        await self.close_hint_notification()

        await expect(self.page.locator("tbody")).to_contain_text(document_no)

        print(document_no)

    async def download(self, document_no):
        await self.navigate_to(self.e_invoice_operations, self.sent_e_invoice)
        print(document_no)

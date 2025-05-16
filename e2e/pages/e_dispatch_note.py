from playwright.async_api import Page, expect
from pages import Document
from env import Config


class EDispatchNote(Document):
    def __init__(self, page: Page):
        super().__init__(page)
        self.document_no: str = ""
        self.dispatch_time = page.locator("#DespatchTime")
        self.actual_dispatch_date = page.locator("#ActualDespatchDate")
        self.actual_dispatch_time = page.locator("#ActualDespatchTime")
        self.carrier_info = page.locator("#CarrierInfo")
        self.driver_name = page.locator("#DriverName")
        self.driver_last_name = page.locator("#DriverLastName")
        self.driver_tckn = page.locator("#Tckn")
        self.number_plate = page.locator("#Plaque")
        self.notes = page.locator("#Notes")
        self.create_new_document_button = page.get_by_role(
            "button", name="Yeni İrsaliye Oluştur!"
        )

    async def select_dispatch_note_customer(self):
        await self.e_dispatch_note_button.click()

    async def select_dispatch_type(self, option: str = "1"):
        await self.dispatch_type.select_option(option)

    async def click_dispatch_time(self):
        await self.dispatch_time.click()

    async def click_actual_dispatch_date(self):
        await self.actual_dispatch_date.click()

    async def click_actual_dispatch_time(self):
        await self.actual_dispatch_time.click()

    async def uncheck_carrier_info(self):
        await self.carrier_info.uncheck()

    async def fill_driver_name(self, name: str):
        await self.driver_name.fill(name)

    async def fill_driver_last_name(self, last_name: str):
        await self.driver_last_name.fill(last_name)

    async def fill_driver_tckn(self, tckn):
        await self.driver_tckn.fill(tckn)

    async def fill_number_plate(self, number_plate):
        await self.number_plate.fill(number_plate)

    async def fill_notes(self, note: str):
        await self.notes.fill(note)

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
            print(f"Dispatch Number: {self.document_no}")
        else:
            print("Dispatch number not found")

        await expect(self.page.get_by_role("paragraph")).to_contain_text(
            f"İrsaliye başarıyla kaydedilmiştir. İrsaliye No. : {self.document_no}"
        )
        return self.document_no

    async def create(self) -> str:
        await self.navigate_to(self.e_document, self.e_dispatch_note)
        await self.click_search_recipient()
        await self.select_dispatch_note_customer()
        await self.fill_title_tckn_input_field(
            recipient=Config.E_DISPATCH_NOTE_CUSTOMER
        )
        await self.click_recipient(recipient=Config.E_DISPATCH_NOTE_CUSTOMER)
        await self.select_scenario()
        await self.select_dispatch_type()
        await self.click_next_button()
        await self.click_today_button()
        await self.click_dispatch_time()
        await self.click_actual_dispatch_date()
        await self.click_actual_dispatch_time()
        await self.click_next_button()
        await self.uncheck_carrier_info()
        await self.fill_driver_name(name=Config.DRIVER_FIRST_NAME)
        await self.fill_driver_last_name(last_name=Config.DRIVER_LAST_NAME)
        await self.fill_driver_tckn(tckn=Config.DRIVER_TCKN)
        await self.fill_number_plate(number_plate=Config.NUMBER_PLATE)
        await self.click_next_button()
        await self.click_search_product()
        await self.fill_product(product=Config.PRODUCT)
        await self.click_product_item(product=Config.PRODUCT)
        await self.click_next_button()
        await self.click_next_button()
        await self.click_next_button()
        await self.fill_notes(note=Config.TAX_EXEMPTION_REASON)
        await self.click_finish_button()
        await self.click_yes_save_button()
        self.document_no = await self.return_document_number()
        await self.click_create_new_document_button()
        return self.document_no

    async def send(self, document_no): ...

    async def download(self, document_no): ...

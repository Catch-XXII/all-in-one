from playwright.async_api import Page
from env import Config


class Base:
    def __init__(self, page: Page, timeout: int = 10_000):
        self.page = page
        self.timeout = timeout
        self.cookie_message = page.get_by_role("button", name="dismiss cookie message")
        self.second_notification = page.locator("#Bilgilendirme2")
        self.first_notification = page.locator("#Bilgilendirme")
        self.hint = page.locator(".enjoyhint_close_btn")

        # Common Elements
        self.search_recipient = page.locator("#SearchRecipient")
        self.e_archive_button = page.get_by_text("E-Arşiv", exact=True)
        self.e_invoice_button = page.get_by_text("E-Fatura", exact=True)
        self.title_vkn_tckn_input = page.get_by_label("Ünvanı/Adı Soyadı - Vkn/Tckn")
        self.scenario_id = page.locator("#SenaryoId")
        self.invoice_type = page.locator("#FaturaTipi")
        self.next_button = page.get_by_role("menuitem", name="Sonraki")
        self.today_button = page.locator("#today")
        self.same_day_button = page.locator("#day")

    async def go_to(self, path: str = ""):
        url = Config.BASE_URL.rstrip("/") + "/" + path.lstrip("/")
        await self.page.goto(url)

    async def close_first_notification(self):
        await self.first_notification.get_by_label("Close").click()

    async def close_second_notification(self):
        await self.second_notification.get_by_label("Close").click()

    async def close_hint_notification(self):
        await self.hint.click()

    async def close_cookie_message(self):
        await self.cookie_message.click()

    async def fill_title_tckn_input_field(self, recipient: str):
        await self.title_vkn_tckn_input.fill(recipient)

    async def click_today_button(self):
        await self.today_button.click()

    async def click_same_day_button(self):
        await self.same_day_button.click()

    async def click_menu(self, item):
        await self.page.evaluate(
            f"""
               (function() {{
                   const container = document.querySelector('ul.left-menu-list.left-menu-list-root.list-unstyled');
                   if (!container) {{
                       console.warn('Menu container not found');
                       return;
                   }}
                   const links = container.querySelectorAll('a.left-menu-link');
                   for (const link of links) {{
                       if (link.textContent.trim().toLowerCase() === '{item.lower()}') {{
                           link.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                           link.click();
                           console.log('Clicked on:', link);
                           return;
                       }}
                   }}
                   console.warn('Link with text "{item}" not found');
               }})();
               """
        )


class Document(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.e_document = "e-Belge Oluştur"
        self.e_invoice_e_archive = "e-Fatura/e-Arşiv Oluştur"
        self.e_dispatch_note = "e-İrsaliye İşlemleri"


class EInvoice(Document):
    def __init__(self, page: Page):
        super().__init__(page)
        self.document_no: str = ""
        self.e_invoice_operations: str = "e-Fatura İşlemleri"
        self.draft_e_invoice: str = "Taslak e-Faturalar"
        self.sent_e_invoice: str = "Giden e-Fatura"

    async def navigate_to(self, first: str, second: str):
        await self.click_menu(first)
        await self.click_menu(second)

    async def click_search_recipient(self):
        await self.search_recipient.click()

    async def select_e_invoice_customer(self):
        await self.e_archive_button.click()

    async def select_scenario(self, option: str = "1"):
        await self.scenario_id.select_option(option)

    async def select_invoice_type(self, option: str = "1"):
        await self.invoice_type.select_option(option)

    async def click_next_button(self):
        await self.next_button.click()

    async def click_recipient(self, recipient: str):
        await self.page.get_by_text(recipient).click()

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

        return self.document_no

    async def send(self, document_no):
        await self.navigate_to(self.e_invoice_operations, self.draft_e_invoice)
        print(document_no)

    async def download(self, document_no):
        await self.navigate_to(self.e_invoice_operations, self.sent_e_invoice)
        print(document_no)


class EArchive(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create(self) -> str: ...

    async def send(self, document_no): ...

    async def download(self, document_no): ...


class EDispatchNote(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create(self) -> str: ...

    async def send(self, document_no): ...

    async def download(self, document_no): ...


class Emm(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create(self) -> str: ...

    async def send(self, document_no): ...

    async def download(self, document_no): ...


class ESmm(Document):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create(self) -> str: ...

    async def send(self, document_no): ...

    async def download(self, document_no): ...

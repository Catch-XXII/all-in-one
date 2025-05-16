from playwright.async_api import Page
from env import Config


class Base:
    def __init__(self, page: Page, timeout: int = 10_000):
        self.page = page
        self.timeout = timeout
        self.cookie_message = page.get_by_role("button", name="dismiss cookie message")
        self.second_notification = page.locator("#Bilgilendirme2").get_by_label("Close")
        self.first_notification = page.locator("#Bilgilendirme").get_by_label("Close")
        self.hint = page.locator(".enjoyhint_close_btn")

        # Common Elements
        self.search_recipient = page.locator("#SearchRecipient")
        self.e_invoice_button = page.locator("label[for='rbtRecipientType_eInvoice']")
        self.e_archive_button = page.locator("label[for='rbtRecipientType_eArchive']")
        self.e_dispatch_note_button = page.locator(
            "label[for='rbtRecipientType_eDespatchNoPayer']"
        )
        self.title_vkn_tckn_input = page.get_by_label("Ünvanı/Adı Soyadı - Vkn/Tckn")
        self.scenario_id = page.locator("#SenaryoId")
        self.invoice_type = page.locator("#FaturaTipi")
        self.dispatch_type = page.locator("#IrsaliyeTipi")
        self.next_button = page.get_by_role("menuitem", name="Sonraki")
        self.today_button = page.locator("#today")
        self.same_day_button = page.locator("#day")
        self.search_product = page.locator("#SearchProduct")
        self.select_product = page.get_by_label("Ürün adı - Kaynak kodu ile")
        self.tax_exemption_reason = page.locator("#TaxExemptionReason")
        self.finish_button = page.get_by_role("menuitem", name="Bitir")
        self.yes_save_button = page.get_by_role("button", name="Evet Kaydedelim !")
        self.save_message = page.locator("p.lead.text-muted")
        self.filter = page.get_by_role("tab", name="Filtre Ekle Firma : isnet")
        self.filter_document_no = page.locator("#FaturaNo")

    async def go_to(self, path: str = ""):
        url = Config.BASE_URL.rstrip("/") + "/" + path.lstrip("/")
        await self.page.goto(url)

    async def close_first_notification(self):
        await self.first_notification.click()

    async def close_second_notification(self):
        await self.second_notification.click()

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

    async def click_finish_button(self):
        await self.finish_button.click()

    async def click_yes_save_button(self):
        await self.yes_save_button.click()

    async def select_scenario(self, option: str = "1"):
        await self.scenario_id.select_option(option)

    async def fill_tax_exemption_reason(self, reason):
        await self.tax_exemption_reason.fill(reason)

    async def click_product_item(self, product):
        await self.page.get_by_text(product).nth(4).click()

    async def click_search_recipient(self):
        await self.search_recipient.click()

    async def click_search_product(self):
        await self.search_product.click()

    async def click_next_button(self):
        await self.next_button.click()

    async def click_recipient(self, recipient: str):
        await self.page.get_by_text(recipient).click()

    async def click_filter(self):
        await self.filter.click()

    async def fill_product(self, product):
        await self.select_product.fill(product)

    async def fill_filter_document_no(self, document_no):
        await self.filter_document_no.fill(document_no)

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

# from playwright.async_api import Page, expect
# from pages import Document
# class Base:
#     def __init__(self, page: Page, timeout: int = 10_000):
#         self.page = page
#         self.timeout = timeout
#         self.cookie_message = page.get_by_role("button", name="dismiss cookie message")
#         self.second_notification = page.locator("#Bilgilendirme2").get_by_label("Close")
#         self.first_notification = page.locator("#Bilgilendirme").get_by_label("Close")
#         self.hint = page.locator(".enjoyhint_close_btn")
#
#         # Common Elements
#         self.search_recipient = page.locator("#SearchRecipient")
#         self.e_invoice_button = page.locator("label[for='rbtRecipientType_eInvoice']")
#         self.e_archive_button = page.locator("label[for='rbtRecipientType_eArchive']")
#         self.e_dispatch_note_button = page.locator(
#             "label[for='rbtRecipientType_eDespatchNoPayer']"
#         )
#         self.title_vkn_tckn_input = page.get_by_label("Ünvanı/Adı Soyadı - Vkn/Tckn")
#         self.scenario_id = page.locator("#SenaryoId")
#         self.invoice_type = page.locator("#FaturaTipi")
#         self.dispatch_type = page.locator("#IrsaliyeTipi")
#         self.next_button = page.get_by_role("menuitem", name="Sonraki")
#         self.today_button = page.locator("#today")
#         self.same_day_button = page.locator("#day")
#         self.search_product = page.locator("#SearchProduct")
#         self.select_product = page.get_by_label("Ürün adı - Kaynak kodu ile")
#         self.tax_exemption_reason = page.locator("#TaxExemptionReason")
#         self.finish_button = page.get_by_role("menuitem", name="Bitir")
#         self.yes_save_button = page.get_by_role("button", name="Evet Kaydedelim !")
#         self.save_message = page.locator("p.lead.text-muted")
#         self.filter = page.get_by_role("tab", name="Filtre Ekle Firma : isnet")
#         self.filter_document_no = page.locator("#FaturaNo")
#
#     async def go_to(self, path: str = ""):
#         url = Config.BASE_URL.rstrip("/") + "/" + path.lstrip("/")
#         await self.page.goto(url)
#
#     async def close_first_notification(self):
#         await self.first_notification.click()
#
#     async def close_second_notification(self):
#         await self.second_notification.click()
#
#     async def close_hint_notification(self):
#         await self.hint.click()
#
#     async def close_cookie_message(self):
#         await self.cookie_message.click()
#
#     async def fill_title_tckn_input_field(self, recipient: str):
#         await self.title_vkn_tckn_input.fill(recipient)
#
#     async def click_today_button(self):
#         await self.today_button.click()
#
#     async def click_same_day_button(self):
#         await self.same_day_button.click()
#
#     async def click_finish_button(self):
#         await self.finish_button.click()
#
#     async def click_yes_save_button(self):
#         await self.yes_save_button.click()
#
#     async def select_scenario(self, option: str = "1"):
#         await self.scenario_id.select_option(option)
#
#     async def fill_tax_exemption_reason(self, reason):
#         await self.tax_exemption_reason.fill(reason)
#
#     async def click_product_item(self, product):
#         await self.page.get_by_text(product).nth(4).click()
#
#     async def click_search_recipient(self):
#         await self.search_recipient.click()
#
#     async def click_search_product(self):
#         await self.search_product.click()
#
#     async def click_next_button(self):
#         await self.next_button.click()
#
#     async def click_recipient(self, recipient: str):
#         await self.page.get_by_text(recipient).click()
#
#     async def click_filter(self):
#         await self.filter.click()
#
#     async def fill_product(self, product):
#         await self.select_product.fill(product)
#
#     async def fill_filter_document_no(self, document_no):
#         await self.filter_document_no.fill(document_no)
#
#     async def click_menu(self, item):
#         await self.page.evaluate(
#             f"""
#                (function() {{
#                    const container = document.querySelector('ul.left-menu-list.left-menu-list-root.list-unstyled');
#                    if (!container) {{
#                        console.warn('Menu container not found');
#                        return;
#                    }}
#                    const links = container.querySelectorAll('a.left-menu-link');
#                    for (const link of links) {{
#                        if (link.textContent.trim().toLowerCase() === '{item.lower()}') {{
#                            link.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
#                            link.click();
#                            console.log('Clicked on:', link);
#                            return;
#                        }}
#                    }}
#                    console.warn('Link with text "{item}" not found');
#                }})();
#                """
#         )
#
#
# class Document(Base):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.e_document = "e-Belge Oluştur"
#         self.e_invoice_e_archive = "e-Fatura/e-Arşiv Oluştur"
#         self.e_dispatch_note = "e-İrsaliye Oluştur"
#         self.e_mm = "e-MM Oluştur"
#         self.e_smm = "e-SMM Oluştur"
#
#     async def navigate_to(self, first: str, second: str):
#         await self.click_menu(first)
#         await self.click_menu(second)
#
#
# class EInvoice(Document):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.document_no: str = ""
#         self.e_invoice_operations: str = "e-Fatura İşlemleri"
#         self.draft_e_invoice: str = "Taslak e-Faturalar"
#         self.sent_e_invoice: str = "Giden e-Fatura"
#
#         self.create_new_document_button = page.get_by_role(
#             "button", name="Yeni Fatura Oluştur!"
#         )
#
#     async def select_e_invoice_customer(self):
#         await self.e_archive_button.click()
#
#     async def select_invoice_type(self, option: str = "1"):
#         await self.invoice_type.select_option(option)
#
#     async def click_create_new_document_button(self):
#         await self.create_new_document_button.click()
#
#     async def return_document_number(self) -> str:
#         await self.page.wait_for_selector(
#             "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
#         )
#         await expect(self.page.get_by_text("başarıyla")).to_be_visible()
#
#         full_text = await self.save_message.text_content()
#         if full_text:
#             self.document_no: str = full_text.split(":")[-1].strip()
#             print(f"Invoice Number: {self.document_no}")
#         else:
#             print("Invoice number not found")
#
#         await expect(self.page.get_by_role("paragraph")).to_contain_text(
#             f"Fatura başarıyla kaydedilmiştir. Fatura No. : {self.document_no}"
#         )
#         return self.document_no
#
#     async def create(self) -> str:
#         await self.navigate_to(self.e_document, self.e_invoice_e_archive)
#         await self.click_search_recipient()
#         await self.select_e_invoice_customer()
#         await self.fill_title_tckn_input_field(recipient=Config.E_INVOICE_CUSTOMER)
#         await self.click_recipient(recipient=Config.E_INVOICE_CUSTOMER)
#         await self.select_scenario()
#         await self.select_invoice_type()
#         await self.click_next_button()
#         await self.click_today_button()
#         await self.click_same_day_button()
#         await self.click_next_button()
#         await self.click_search_product()
#         await self.fill_product(product=Config.PRODUCT)
#         await self.click_product_item(product=Config.PRODUCT)
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.fill_tax_exemption_reason(Config.TAX_EXEMPTION_REASON)
#         await self.click_finish_button()
#         await self.click_yes_save_button()
#         self.document_no = await self.return_document_number()
#         await self.click_create_new_document_button()
#         return self.document_no
#
#     async def send(self, document_no):
#         await self.navigate_to(self.e_invoice_operations, self.draft_e_invoice)
#         await self.close_hint_notification()
#
#         await expect(self.page.locator("tbody")).to_contain_text(document_no)
#
#         print(document_no)
#
#     async def download(self, document_no):
#         await self.navigate_to(self.e_invoice_operations, self.sent_e_invoice)
#         print(document_no)
#
#
# class EArchive(Document):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.document_no: str = ""
#         self.create_new_document_button = page.get_by_role(
#             "button", name="Yeni Fatura Oluştur!"
#         )
#
#     async def select_e_archive_customer(self):
#         await self.e_invoice_button.click()
#
#     async def select_invoice_type(self, option: str = "1"):
#         await self.invoice_type.select_option(option)
#
#     async def click_create_new_document_button(self):
#         await self.create_new_document_button.click()
#
#     async def return_document_number(self) -> str:
#         await self.page.wait_for_selector(
#             "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
#         )
#         await expect(self.page.get_by_text("başarıyla")).to_be_visible()
#
#         full_text = await self.save_message.text_content()
#         if full_text:
#             self.document_no: str = full_text.split(":")[-1].strip()
#             print(f"Archive Number: {self.document_no}")
#         else:
#             print("Archive number not found")
#
#         await expect(self.page.get_by_role("paragraph")).to_contain_text(
#             f"Fatura başarıyla kaydedilmiştir. Fatura No. : {self.document_no}"
#         )
#         return self.document_no
#
#     async def create(self) -> str:
#         await self.navigate_to(self.e_document, self.e_invoice_e_archive)
#         await self.click_search_recipient()
#         await self.select_e_archive_customer()
#         await self.fill_title_tckn_input_field(recipient=Config.E_ARCHIVE_CUSTOMER)
#         await self.click_recipient(recipient=Config.E_ARCHIVE_CUSTOMER)
#         await self.select_invoice_type()
#         await self.click_next_button()
#         await self.click_today_button()
#         await self.click_same_day_button()
#         await self.click_next_button()
#         await self.click_search_product()
#         await self.fill_product(product=Config.PRODUCT)
#         await self.click_product_item(product=Config.PRODUCT)
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.fill_tax_exemption_reason(reason=Config.TAX_EXEMPTION_REASON)
#         await self.click_finish_button()
#         await self.click_yes_save_button()
#         self.document_no = await self.return_document_number()
#         await self.click_create_new_document_button()
#         return self.document_no
#
#     async def send(self, document_no): ...
#
#     async def download(self, document_no): ...
#
#
# class EDispatchNote(Document):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.document_no: str = ""
#         self.dispatch_time = page.locator("#DespatchTime")
#         self.actual_dispatch_date = page.locator("#ActualDespatchDate")
#         self.actual_dispatch_time = page.locator("#ActualDespatchTime")
#         self.carrier_info = page.locator("#CarrierInfo")
#         self.driver_name = page.locator("#DriverName")
#         self.driver_last_name = page.locator("#DriverLastName")
#         self.driver_tckn = page.locator("#Tckn")
#         self.number_plate = page.locator("#Plaque")
#         self.notes = page.locator("#Notes")
#         self.create_new_document_button = page.get_by_role(
#             "button", name="Yeni İrsaliye Oluştur!"
#         )
#
#     async def select_dispatch_note_customer(self):
#         await self.e_dispatch_note_button.click()
#
#     async def select_dispatch_type(self, option: str = "1"):
#         await self.dispatch_type.select_option(option)
#
#     async def click_dispatch_time(self):
#         await self.dispatch_time.click()
#
#     async def click_actual_dispatch_date(self):
#         await self.actual_dispatch_date.click()
#
#     async def click_actual_dispatch_time(self):
#         await self.actual_dispatch_time.click()
#
#     async def uncheck_carrier_info(self):
#         await self.carrier_info.uncheck()
#
#     async def fill_driver_name(self, name: str):
#         await self.driver_name.fill(name)
#
#     async def fill_driver_last_name(self, last_name: str):
#         await self.driver_last_name.fill(last_name)
#
#     async def fill_driver_tckn(self, tckn):
#         await self.driver_tckn.fill(tckn)
#
#     async def fill_number_plate(self, number_plate):
#         await self.number_plate.fill(number_plate)
#
#     async def fill_notes(self, note: str):
#         await self.notes.fill(note)
#
#     async def click_create_new_document_button(self):
#         await self.create_new_document_button.click()
#
#     async def return_document_number(self) -> str:
#         await self.page.wait_for_selector(
#             "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
#         )
#         await expect(self.page.get_by_text("başarıyla")).to_be_visible()
#
#         full_text = await self.save_message.text_content()
#         if full_text:
#             self.document_no: str = full_text.split(":")[-1].strip()
#             print(f"Dispatch Number: {self.document_no}")
#         else:
#             print("Dispatch number not found")
#
#         await expect(self.page.get_by_role("paragraph")).to_contain_text(
#             f"İrsaliye başarıyla kaydedilmiştir. İrsaliye No. : {self.document_no}"
#         )
#         return self.document_no
#
#     async def create(self) -> str:
#         await self.navigate_to(self.e_document, self.e_dispatch_note)
#         await self.click_search_recipient()
#         await self.select_dispatch_note_customer()
#         await self.fill_title_tckn_input_field(
#             recipient=Config.E_DISPATCH_NOTE_CUSTOMER
#         )
#         await self.click_recipient(recipient=Config.E_DISPATCH_NOTE_CUSTOMER)
#         await self.select_scenario()
#         await self.select_dispatch_type()
#         await self.click_next_button()
#         await self.click_today_button()
#         await self.click_dispatch_time()
#         await self.click_actual_dispatch_date()
#         await self.click_actual_dispatch_time()
#         await self.click_next_button()
#         await self.uncheck_carrier_info()
#         await self.fill_driver_name(name=Config.DRIVER_FIRST_NAME)
#         await self.fill_driver_last_name(last_name=Config.DRIVER_LAST_NAME)
#         await self.fill_driver_tckn(tckn=Config.DRIVER_TCKN)
#         await self.fill_number_plate(number_plate=Config.NUMBER_PLATE)
#         await self.click_next_button()
#         await self.click_search_product()
#         await self.fill_product(product=Config.PRODUCT)
#         await self.click_product_item(product=Config.PRODUCT)
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.fill_notes(note=Config.TAX_EXEMPTION_REASON)
#         await self.click_finish_button()
#         await self.click_yes_save_button()
#         self.document_no = await self.return_document_number()
#         await self.click_create_new_document_button()
#         return self.document_no
#
#     async def send(self, document_no): ...
#
#     async def download(self, document_no): ...
#
#
# class Emm(Document):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.document_no: str = ""
#         self.document_time = page.locator("#DocumentTime")
#         self.notes = page.locator("#Notes")
#         self.drafts_button = page.get_by_role("button", name="Taslaklara git!")
#
#     async def click_document_time(self):
#         await self.document_time.click()
#
#     async def fill_notes(self, note: str):
#         await self.notes.fill(note)
#
#     async def click_drafts_button(self):
#         await self.drafts_button.click()
#
#     async def return_document_number(self, customer_full_name) -> str:
#         await expect(self.page.locator("tbody")).to_contain_text(customer_full_name)
#
#         self.document_no = await self.page.evaluate(
#             """ async () => {
#             response = document.querySelector("#StagingEMMTable > tbody > tr > td:nth-child(3)").innerText;
#             return response;
#             }
#         """
#         )
#         if self.document_no:
#             print(f"E-mm number: {self.document_no}")
#         else:
#             print("E-mm number not found")
#
#         return self.document_no
#
#     async def create(self) -> str:
#         await self.navigate_to(self.e_document, self.e_mm)
#         await self.click_search_recipient()
#         await self.fill_title_tckn_input_field(Config.E_MM_CUSTOMER)
#         await self.click_recipient(recipient=Config.E_MM_CUSTOMER)
#         await self.click_today_button()
#         await self.click_document_time()
#         await self.click_next_button()
#         await self.click_search_product()
#         await self.fill_product(product=Config.PRODUCT)
#         await self.click_product_item(product=Config.PRODUCT)
#         await self.click_next_button()
#         await self.fill_notes(note=Config.TAX_EXEMPTION_REASON)
#         await self.click_finish_button()
#         await self.click_yes_save_button()
#
#         await self.page.wait_for_selector(
#             "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
#         )
#         await expect(self.page.get_by_text("başarıyla")).to_be_visible()
#
#         await self.click_drafts_button()
#
#         self.document_no = await self.return_document_number(
#             Config.E_MM_CUSTOMER_FULL_NAME
#         )
#         return self.document_no
#
#     async def send(self, document_no): ...
#
#     async def download(self, document_no): ...
#
#
# class ESmm(Document):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.document_no: str = ""
#         self.document_time = page.locator("#DocumentTime")
#         self.notes = page.locator("#Notes")
#         self.create_new_document_button = page.get_by_role(
#             "button", name="Yeni Doküman Oluştur!"
#         )
#
#     async def select_e_invoice_customer(self):
#         await self.e_archive_button.click()
#
#     async def click_document_time(self):
#         await self.document_time.click()
#
#     async def fill_notes(self, note: str):
#         await self.notes.fill(note)
#
#     async def click_create_new_document(self):
#         await self.create_new_document_button.click()
#
#     async def return_document_number(self) -> str:
#         await self.page.wait_for_selector(
#             "div.sweet-alert.showSweetAlert.visible", timeout=self.timeout
#         )
#         await expect(self.page.get_by_text("başarıyla")).to_be_visible()
#
#         full_text = await self.save_message.text_content()
#         if full_text:
#             self.document_no: str = full_text.split(":")[-1].strip()
#             print(f"Document Number: {self.document_no}")
#         else:
#             print("Document number not found")
#
#         await expect(self.page.get_by_role("paragraph")).to_contain_text(
#             f"Doküman başarıyla kaydedilmiştir.Döküman no : {self.document_no}"
#         )
#         return self.document_no
#
#     async def create(self) -> str:
#         await self.navigate_to(self.e_document, self.e_smm)
#         await self.click_search_recipient()
#         await self.select_e_invoice_customer()
#         await self.fill_title_tckn_input_field(
#             recipient=Config.E_SMM_E_INVOICE_CUSTOMER
#         )
#         await self.click_recipient(recipient=Config.E_SMM_E_INVOICE_CUSTOMER)
#         await self.click_today_button()
#         await self.click_document_time()
#         await self.click_next_button()
#         await self.click_search_product()
#         await self.fill_product(product=Config.PRODUCT)
#         await self.click_product_item(product=Config.PRODUCT)
#         await self.click_next_button()
#         await self.click_next_button()
#         await self.fill_notes(note=Config.TAX_EXEMPTION_REASON)
#         await self.click_finish_button()
#         await self.click_yes_save_button()
#         self.document_no = await self.return_document_number()
#         await self.click_create_new_document()
#         return self.document_no
#
#     async def send(self, document_no): ...
#
#     async def download(self, document_no): ...

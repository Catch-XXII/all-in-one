from fastapi import APIRouter
from playwright.async_api import async_playwright

from app.db.schemas.analyze_schema import AnalyzeRequestSchema
from app.utils.parser_utils import HTMLStructureAnalyzer

router = APIRouter()


@router.post("/analyze")
async def analyze(body: AnalyzeRequestSchema):
    url = str(body.url).strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto(url, timeout=15000)
            await page.wait_for_load_state("domcontentloaded")
        except Exception as e:
            await browser.close()
            return {"detail": f"Failed to load page: {str(e)}"}

        html_content = await page.content()
        structure_parser = HTMLStructureAnalyzer(html_content)
        structure_info = structure_parser.get_document_structure()
        tag_counts = structure_parser.get_tag_counts()

        elements = await page.query_selector_all(
            "body input, body button, body textarea, body select, "
            "body a, body form, body img, body h1, body p"
        )
        result = []

        for el in elements:
            tag = await el.evaluate("e => e.tagName.toLowerCase()")
            class_attr = await el.get_attribute("class") or ""
            id_attr = await el.get_attribute("id")
            name_attr = await el.get_attribute("name")
            placeholder_attr = await el.get_attribute("placeholder")
            type_attr = await el.get_attribute("type")
            text_content = (await el.inner_text()) or ""

            if "footer" in class_attr.lower():
                continue

            if tag == "a" and not text_content.strip():
                continue

            if tag not in {
                "input",
                "button",
                "textarea",
                "select",
                "a",
                "form",
                "img",
                "h1",
                "p",
            }:
                continue

            if not (id_attr or name_attr or placeholder_attr or text_content.strip()):
                continue

            # Try to find label by matching 'for' attribute
            label_text = None
            element_id_or_name = id_attr or name_attr
            if element_id_or_name:
                label_el = await page.query_selector(
                    f'label[for="{element_id_or_name}"]'
                )
                if label_el:
                    label_text = (await label_el.inner_text()) or None

            if not label_text:
                parent = await el.evaluate_handle("e => e.parentElement")
                if parent:
                    label_el = await parent.query_selector("label")
                    if label_el:
                        label_text = (await label_el.inner_text()) or None

            result.append(
                {
                    "tag": tag,
                    "type": type_attr,
                    "id": id_attr,
                    "name": name_attr,
                    "placeholder": placeholder_attr,
                    "class": class_attr,
                    "text": text_content.strip(),
                    "label": label_text.strip() if label_text else None,
                }
            )

        await browser.close()
        return {
            "structure": structure_info,
            "tag_counts": tag_counts,
            "elements": result,
        }

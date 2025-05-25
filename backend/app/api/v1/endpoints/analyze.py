from fastapi import APIRouter
from httpx import AsyncClient, RequestError
from selectolax.parser import HTMLParser

from app.db.schemas.analyze_schema import AnalyzeRequestSchema

router = APIRouter()


def guess_element_type(node):
    tag = node.tag or ""
    class_attr = node.attributes.get("class")
    class_attr = class_attr.lower() if class_attr else ""

    if tag == "h1" or "title" in class_attr or "headline" in class_attr:
        return "headline"
    if tag == "button" or "btn" in class_attr:
        return "button"
    if tag == "a" and "href" in node.attributes:
        return "link"
    if tag == "img":
        return "image"
    if tag == "form":
        return "form"
    if tag == "p" and len(node.text(strip=True)) > 40:
        return "paragraph"

    return "other"


@router.post("/analyze")
async def analyze(body: AnalyzeRequestSchema):
    url = str(body.url).strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,image/webp,*/*;q=0.8"
        ),
    }

    try:
        async with AsyncClient(timeout=10, follow_redirects=True) as client:
            response = await client.get(url, headers=headers)
    except RequestError as e:
        return {"detail": f"Failed to fetch URL: {str(e)}"}

    tree = HTMLParser(response.text)
    elements = []

    for node in tree.css("*"):
        if not node.tag:
            continue

        elements.append(
            {
                "type": guess_element_type(node),
                "tag": node.tag,
                "text": node.text(strip=True),
                "id": node.attributes.get("id"),
                "class": node.attributes.get("class"),
            }
        )

    return elements

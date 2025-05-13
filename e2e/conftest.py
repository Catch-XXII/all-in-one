from typing import Any, AsyncGenerator
import pytest_asyncio
from pages import LoginPage
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    async_playwright,
)


# Global playwright fixture
@pytest_asyncio.fixture(scope="function")
async def playwright_instance() -> AsyncGenerator[Playwright, Any]:
    async with async_playwright() as p:
        yield p


# Browser fixture
@pytest_asyncio.fixture(scope="function")
async def browser(playwright_instance: Playwright) -> AsyncGenerator[Browser, Any]:
    print("Launching browser...")
    browser = await playwright_instance.chromium.launch(headless=False, slow_mo=500)
    print("Browser launched.")
    yield browser
    await browser.close()


# Context fixture
@pytest_asyncio.fixture(scope="function")
async def context(browser: Browser) -> AsyncGenerator[BrowserContext, Any]:
    print("Creating context...")
    context = await browser.new_context(viewport={"width": 1881, "height": 935})
    print("Context created...")
    yield context
    await context.close()


# Page fixture
@pytest_asyncio.fixture(scope="function")
async def page(context: BrowserContext) -> AsyncGenerator[Page, Any]:
    print("Creating page...")
    page = await context.new_page()
    print("Page created...")
    yield page


# User fixture (login + logout)
@pytest_asyncio.fixture(scope="function")
async def user(page: Page) -> AsyncGenerator[Page, Any]:
    print("Creating Login page...")
    login_page = LoginPage(page)
    await login_page.do_login()
    print("User logged in...")
    yield page
    await login_page.do_logout()
    print("User logged out...")


# Show collected test cases before execution
def pytest_collection_finish(session):
    print("\n[Collected Test Cases]")
    for item in session.items:
        print(f"- {item.nodeid}")

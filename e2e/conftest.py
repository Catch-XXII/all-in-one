from typing import Any, AsyncGenerator
from pages import LoginPage
import pytest_asyncio
import os
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    async_playwright,
)


def pytest_configure(config):
    if os.environ.get("CI"):
        config.option.reruns = 3


# Global playwright fixture
@pytest_asyncio.fixture(scope="function")
async def playwright_instance():
    async with async_playwright() as p:
        yield p


# Browser fixture
@pytest_asyncio.fixture(scope="function")
async def browser(playwright_instance: Playwright) -> AsyncGenerator[Browser, Any]:
    print()
    print("=" * 100)
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


@pytest_asyncio.fixture
async def user(page: Page) -> AsyncGenerator[Page, Any]:
    print("Creating Login page...")
    login_page = LoginPage(page)
    await login_page.do_login()
    print("User logged in...")
    yield page
    await login_page.do_logout()
    print("")
    print("User logged out...")
    print("=" * 100)


def pytest_collection_finish(session):
    print("\n[Collected Test Cases]")
    for item in session.items:
        print(f"- {item.nodeid}")

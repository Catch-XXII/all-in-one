from pages import (
    Inbox,
    Credit,
    Reports,
    FastInvoice,
)
import pytest


@pytest.mark.aio
class TestAllInOne:
    @pytest.mark.asyncio
    async def test_bulk_download_from_inbox(self, user):
        inbox = Inbox(user)
        await inbox.download()

    @pytest.mark.asyncio
    async def test_purchase_credit(self, user):
        credit = Credit(user)
        await credit.purchase()

    @pytest.mark.asyncio
    async def test_reports(self, user):
        reports = Reports(user)
        await reports.check()

    @pytest.mark.asyncio
    async def test_create_fast_invoice(self, user):
        fast = FastInvoice(user)
        await fast.create()

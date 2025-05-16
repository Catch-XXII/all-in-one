from utils import save_document
from pages import (
    EInvoice,
    EArchive,
    EDispatchNote,
    Emm,
    ESmm,
)
import pytest


@pytest.mark.create
class TestCreate:
    @pytest.mark.order(1)
    @pytest.mark.asyncio
    async def test_create_e_invoice(self, user):
        e_invoice = EInvoice(user)
        invoice_number = await e_invoice.create()
        save_document("invoice", invoice_number)

    @pytest.mark.order(2)
    @pytest.mark.asyncio
    async def test_create_e_archive(self, user):
        e_archive = EArchive(user)
        archive_number = await e_archive.create()
        save_document("archive", archive_number)

    @pytest.mark.order(3)
    @pytest.mark.asyncio
    async def test_create_e_dispatch(self, user):
        e_dispatch = EDispatchNote(user)
        dispatch_number = await e_dispatch.create()
        save_document("dispatch", dispatch_number)

    @pytest.mark.order(4)
    @pytest.mark.asyncio
    async def test_create_e_mm(self, user):
        e_mm = Emm(user)
        e_mm_number = await e_mm.create()
        save_document("e_mm", e_mm_number)

    @pytest.mark.order(5)
    @pytest.mark.asyncio
    async def test_create_e_smm(self, user):
        e_smm = ESmm(user)
        e_smm_number = await e_smm.create()
        save_document("e_smm", e_smm_number)

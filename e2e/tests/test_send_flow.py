from pages import (
    EDispatchNote,
    EInvoice,
    EArchive,
    ESmm,
    Emm,
)
import pytest
from utils import load_document


@pytest.mark.send
class TestSend:
    @pytest.mark.asyncio
    async def test_send_e_invoice(self, user):
        invoice_number = load_document("invoice")
        assert invoice_number is not None, "Invoice number not found"

        e_invoice = EInvoice(user)
        await e_invoice.send(invoice_number)
        print(f"Sent invoice: {invoice_number}")

    @pytest.mark.asyncio
    async def test_send_e_archive(self, user):
        archive_number = load_document("archive")
        assert archive_number is not None, "Archive number not found"

        e_archive = EArchive(user)
        await e_archive.send(archive_number)
        print(f"Sent Archive: {archive_number}")

    @pytest.mark.asyncio
    async def test_send_e_dispatch(self, user):
        dispatch_number = load_document("dispatch")
        assert dispatch_number is not None, "Dispatch number not found"

        e_dispatch = EDispatchNote(user)
        await e_dispatch.send(dispatch_number)
        print(f"Sent Dispatch: {dispatch_number}")

    @pytest.mark.asyncio
    async def test_send_e_mm(self, user):
        e_mm_number = load_document("e_mm")
        assert e_mm_number is not None, "E-mm number not found"

        e_mm = Emm(user)
        await e_mm.send(e_mm_number)
        print(f"Sent E-mm: {e_mm_number}")

    @pytest.mark.asyncio
    async def test_send_e_smm(self, user):
        e_smm_number = load_document("e_smm")
        assert e_smm_number is not None, "E-smm number not found"

        e_smm = ESmm(user)
        await e_smm.send(e_smm_number)
        print(f"Sent E-smm: {e_smm_number}")

from utils import load_document
from pages import (
    EInvoice,
    EArchive,
    EDispatchNote,
    Emm,
    ESmm,
)
import pytest


@pytest.mark.download
class TestDownload:
    @pytest.mark.asyncio
    async def test_download_e_invoice(self, user):
        invoice_number = load_document("invoice")
        assert invoice_number is not None, "Invoice number not found"

        e_invoice = EInvoice(user)
        await e_invoice.download(invoice_number)
        print(f"Download invoice: {invoice_number}")

    @pytest.mark.asyncio
    async def test_download_e_archive(self, user):
        archive_number = load_document("archive")
        assert archive_number is not None, "Archive number not found"

        e_archive = EArchive(user)
        await e_archive.download(archive_number)
        print(f"Download archive: {archive_number}")

    @pytest.mark.asyncio
    async def test_download_e_dispatch(self, user):
        dispatch_number = load_document("dispatch")
        assert dispatch_number is not None, "Dispatch number not found"

        e_dispatch = EDispatchNote(user)
        await e_dispatch.download(dispatch_number)
        print(f"Download dispatch: {dispatch_number}")

    @pytest.mark.asyncio
    async def test_download_e_mm(self, user):
        e_mm_number = load_document("e_mm")
        assert e_mm_number is not None, "E-mm number not found"

        e_mm = Emm(user)
        await e_mm.download(e_mm_number)
        print(f"Download e-mm: {e_mm_number}")

    @pytest.mark.asyncio
    async def test_download_e_smm(self, user):
        e_smm_number = load_document("e_smm")
        assert e_smm_number is not None, "E-smm number not found"

        e_smm = ESmm(user)
        await e_smm.download(e_smm_number)
        print(f"Download e-smm: {e_smm_number}")

from pages import EInvoice, EArchive, EDispatchNote, Emm, ESmm
import pytest


invoice_number = ""
archive_number = ""
dispatch_number = ""
e_mm_number = ""
e_smm_number = ""


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_e_invoice(user):
    e_invoice = EInvoice(user)
    global invoice_number
    invoice_number = await e_invoice.create()


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_create_e_archive(user):
    e_archive = EArchive(user)
    global archive_number
    archive_number = await e_archive.create()


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_create_e_dispatch(user):
    e_dispatch = EDispatchNote(user)
    global dispatch_number
    dispatch_number = await e_dispatch.create()


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_create_e_mm(user):
    e_mm = Emm(user)
    global e_mm_number
    e_mm_number = await e_mm.create()


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_create_e_smm(user):
    e_smm = ESmm(user)
    global e_smm_number
    e_smm_number = await e_smm.create()


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_send_e_invoice(user):
    e_invoice = EInvoice(user)
    await e_invoice.send(invoice_number)


@pytest.mark.asyncio
@pytest.mark.order(7)
async def test_send_e_archive(user):
    e_archive = EArchive(user)
    await e_archive.send(archive_number)


@pytest.mark.asyncio
@pytest.mark.order(8)
async def test_send_e_dispatch(user):
    e_dispatch = EDispatchNote(user)
    await e_dispatch.send(dispatch_number)


@pytest.mark.asyncio
@pytest.mark.order(9)
async def test_send_e_mm(user):
    e_mm = Emm(user)
    await e_mm.send(e_mm_number)


@pytest.mark.asyncio
@pytest.mark.order(10)
async def test_send_e_smm(user):
    e_smm = ESmm(user)
    await e_smm.send(e_smm_number)


@pytest.mark.asyncio
@pytest.mark.order(11)
async def test_download_e_invoice(user):
    e_invoice = EInvoice(user)
    await e_invoice.download(invoice_number)


@pytest.mark.asyncio
@pytest.mark.order(12)
async def test_download_e_archive(user):
    e_archive = EArchive(user)
    await e_archive.download(archive_number)


@pytest.mark.asyncio
@pytest.mark.order(13)
async def test_download_e_dispatch(user):
    e_dispatch = EDispatchNote(user)
    await e_dispatch.download(dispatch_number)


@pytest.mark.asyncio
@pytest.mark.order(14)
async def test_download_e_mm(user):
    e_mm = Emm(user)
    await e_mm.download(e_mm_number)


@pytest.mark.asyncio
@pytest.mark.order(15)
async def test_download_e_smm(user):
    e_smm = ESmm(user)
    await e_smm.download(e_smm_number)

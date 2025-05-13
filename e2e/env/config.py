"""Configuration loader for environment variables using dotenv.

This module reads key environment settings from a .env file and makes them
available via the Config class as class-level constants.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Holds application-wide configuration values loaded from environment variables.

    Alla values are loaded once at runtime using 'os.getenv()' and exposed as class
    attributes. The .env file must be present in the project root and is loaded
    automatically via 'python-dotenv'.
    """

    TAX_EXEMPTION_REASON = os.getenv("TAX_EXEMPTION_REASON")
    BASE_URL = os.getenv("BASE_URL")
    PASSWORD = os.getenv("PASSWORD")
    COMPANY = os.getenv("COMPANY")
    PRODUCT = os.getenv("PRODUCT")
    TCKN = os.getenv("TCKN")

    # EInvoicePage
    E_INVOICE_CUSTOMER = os.getenv("E_INVOICE_CUSTOMER")

    # EArchivePage
    E_ARCHIVE_CUSTOMER = os.getenv("E_ARCHIVE_CUSTOMER")

    # EDispatchNote
    E_DISPATCH_NOTE_CUSTOMER = os.getenv("E_DISPATCH_NOTE_CUSTOMER")
    DRIVER_FIRST_NAME = os.getenv("DRIVER_FIRST_NAME")
    DRIVER_LAST_NAME = os.getenv("DRIVER_LAST_NAME")
    DRIVER_TCKN = os.getenv("DRIVER_TCKN")
    NUMBER_PLATE = os.getenv("NUMBER_PLATE")

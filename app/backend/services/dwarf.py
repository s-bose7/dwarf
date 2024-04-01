# app/backend/services/dwarf.py

from typing import Dict
from app.database.db import DataBase


class Dwarf:

    db = DataBase()
    i32t_identifier: int = 0
    default_domain: str = f"http://localhost:5000/" # http://dwarf.co

    @staticmethod
    def encode(long_url: str) -> str:
        short_url = Dwarf.db.retrieve_url(long_url=long_url)
        if short_url is None:
            # Generate a new short URL
            Dwarf.i32t_identifier += 1
            short_url = Dwarf.default_domain + str(Dwarf.i32t_identifier)

            # Store the mapping in the database
            Dwarf.db.insert_url(long_url, short_url)

        return short_url

    @staticmethod
    def decode(identifier: str) -> str:
        short_url = Dwarf.default_domain + identifier
        long_url = Dwarf.db.retrieve_url(short_url=short_url)
        return long_url if long_url else ""

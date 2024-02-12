
from typing import Dict

class Dwarf:

    default_domain: str = f"http://localhost:5000/" # http://dwarf.co
    i32t_identifier: int = 0
    encode_map: Dict[str, str] = {}
    decode_map: Dict[str, str] = {}

    def __init__(self) -> None:
        pass

    def __encode(long_url: str)->str:
        if long_url not in Dwarf.encode_map:
            Dwarf.i32t_identifier += 1
            short_url = Dwarf.default_domain + str(Dwarf.i32t_identifier)
            Dwarf.encode_map[long_url] = short_url
            Dwarf.decode_map[short_url] = long_url

        return Dwarf.encode_map.get(long_url)

    @staticmethod
    def decode(indentifier: str)->str:
        short_url = Dwarf.default_domain + indentifier
        if short_url not in Dwarf.decode_map:
            return ""
        return Dwarf.decode_map.get(short_url)


    @staticmethod
    def shorten(url: str)->str:
        short_url = Dwarf.__encode(url)
        return short_url
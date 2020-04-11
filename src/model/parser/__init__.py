import pytz

from datetime import datetime
from src.model.parser.pusat import ParserPusat
from src.model.parser.aceh import ParserAceh
from src.model.parser.bali import ParserBali
from src.model.parser.banten import ParserBanten
from src.model.parser.ntb import ParserNTB
from src.model.parser.sulsel import ParserSulsel


WAKTU_JALAN = datetime.now().astimezone(pytz.timezone("Asia/Jakarta"))
WAKTU_JALAN_STR = WAKTU_JALAN.strftime("%Y-%m-%d %H:%M:%S")


parser_pusat = ParserPusat()

# key from province in https://inacovid19.maps.arcgis.com/apps/opsdashboard/index.html#/4411f5e9c69d4ca4be31ac805a0267be
parsers_daerah = {
    "Aceh": ParserAceh(render="html"),
    "Bali": ParserBali(render="html"),
    "Banten": ParserBanten(render="html"),
    "Nusa Tenggara Barat": ParserNTB(render="html"),
    "Sulawesi Selatan": ParserSulsel(render="html"),
}

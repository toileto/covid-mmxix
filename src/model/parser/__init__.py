import pytz

from datetime import datetime
from src.model.parser.pusat import ParserPusat

from src.model.parser.aceh import ParserAceh
from src.model.parser.riau import ParserRiau

from src.model.parser.bali import ParserBali
from src.model.parser.banten import ParserBanten
from src.model.parser.jabar import ParserJaBar
from src.model.parser.jateng import ParserJaTeng
from src.model.parser.jatim import ParserJaTim

from src.model.parser.kalbar import ParserKalBar
from src.model.parser.kalsel import ParserKalSel

from src.model.parser.ntb import ParserNTB
from src.model.parser.ntt import ParserNTT

from src.model.parser.sulbar import ParserSulBar
from src.model.parser.sulsel import ParserSulSel
from src.model.parser.sultra import ParserSulTra
from src.model.parser.sulut import ParserSulUt


WAKTU_JALAN = datetime.now().astimezone(pytz.timezone("Asia/Jakarta"))
WAKTU_JALAN_STR = WAKTU_JALAN.strftime("%Y-%m-%d %H:%M:%S")


parser_pusat = ParserPusat()

# key from province in https://inacovid19.maps.arcgis.com/apps/opsdashboard/index.html#/4411f5e9c69d4ca4be31ac805a0267be
parsers_daerah = {
    "Aceh": ParserAceh(render="html"),
    "Bali": ParserBali(render="html"),
    "Banten": ParserBanten(render="html"),
    "Jawa Barat": ParserJaBar(render="html"),
    "Jawa Tengah": ParserJaTeng(render="html"),
    "Jawa Timur": ParserJaTim(render="html"),
    "Kalimantan Barat": ParserKalBar(render="html"),
    "Kalimantan Selatan": ParserKalSel(render="html"),
    "Nusa Tenggara Barat": ParserNTB(render="html"),
    "Nusa Tenggara Timur": ParserNTT(render="html"),
    "Riau": ParserRiau(render="html"),
    "Sulawesi Barat": ParserSulBar(render="html"),
    "Sulawesi Selatan": ParserSulSel(render="html"),
    "Sulawesi Tenggara": ParserSulTra(render="html"),
    "Sulawesi Utara": ParserSulUt(render="html"),
}

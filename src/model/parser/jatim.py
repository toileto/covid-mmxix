from src.model.parser.base import ParserBase

class ParserJaTim(ParserBase):
    WEB_URL = "https://infocovid19.jatimprov.go.id"
    DATA_URL = "http://covid19dev.jatimprov.go.id/xweb/draxi"

    def __init__(self, render=None):
        super(ParserJaTim, self).__init__(render)

    def parse(self, source):
        body = source.find("div", {"class": "jumlah-status"})
        data = body.find("div").text.strip().split()

        positive = body.find("label").text.strip().split()[0].strip()
        recover = data[1].strip()
        dead = data[7].strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

from src.model.parser.base import ParserBase

class ParserBali(ParserBase):
    WEB_URL = "https://infocorona.baliprov.go.id"
    DATA_URL = "https://pendataan.baliprov.go.id"

    def __init__(self, render=None):
        super(ParserBali, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "col-md-3"})
        positive = body[0].find("h3").text.replace(" Org", "")
        recover = body[2].find("h3").text.replace(" Org", "")
        dead = body[3].find("h3").text.replace(" Org", "")

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

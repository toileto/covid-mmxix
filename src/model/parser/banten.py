from src.model.parser.base import ParserBase

class ParserBanten(ParserBase):
    WEB_URL = "https://infocorona.bantenprov.go.id"
    DATA_URL = "https://infocorona.bantenprov.go.id"

    def __init__(self, render=None):
        super(ParserBanten, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "col-lg-3"})
        data = body[2].p.text.strip().split("\n")
        value = [d.strip().split()[0] for d in data]

        positive = value[0]
        recover = value[2]
        dead = value[3]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

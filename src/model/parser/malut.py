from src.model.parser.base import ParserBase

class ParserMalUt(ParserBase):
    WEB_URL = "http://corona.malutprov.go.id"
    DATA_URL = "http://corona.malutprov.go.id"

    def __init__(self, render=None):
        super(ParserMalUt, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "card-body"})
        data = body[-1].text.strip().split()

        positive = data[0].strip()
        recover = data[5].strip()
        dead = data[7].strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

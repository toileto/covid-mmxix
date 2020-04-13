from src.model.parser.base import ParserBase

class ParserKalSel(ParserBase):
    WEB_URL = "https://corona.kalselprov.go.id"
    DATA_URL = "https://corona.kalselprov.go.id"

    def __init__(self, render=None):
        super(ParserKalSel, self).__init__(render)

    def parse(self, source):
        body = source.find_all("span", {"class": "h1 font-weight-bolder mb-0 text-white"})
        data = [x.text.strip() for x in body]

        positive = data[8]
        recover = data[11]
        dead = data[10]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

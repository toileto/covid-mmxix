from src.model.parser.base import ParserBase

class ParserNTB(ParserBase):
    WEB_URL = "https://corona.ntbprov.go.id"
    DATA_URL = "https://corona.ntbprov.go.id"

    def __init__(self, render=None):
        super(ParserNTB, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "col-md-4"})
        data =  body[2].find_all("span")

        value = [d.text.split()[0] for d in data]

        positive = value[1]
        recover = value[2]
        dead = value[3]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

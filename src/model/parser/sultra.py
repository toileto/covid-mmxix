from src.model.parser.base import ParserBase

class ParserSulTra(ParserBase):
    WEB_URL = "https://dinkes.sultraprov.go.id"
    DATA_URL = "https://dinkes.sultraprov.go.id"

    def __init__(self, render=None):
        super(ParserSulTra, self).__init__(render)

    def parse(self, source):
        body = source.find_all("span", {"class": "info-angka red"})
        data = [b.text.strip() for b in body]

        positive = data[1]
        recover = data[0]
        dead = data[2]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

from src.model.parser.base import ParserBase

class ParserRiau(ParserBase):
    WEB_URL = "https://corona.riau.go.id"
    DATA_URL = "https://covid19.riau.go.id/pantauan"

    def __init__(self, render=None):
        super(ParserRiau, self).__init__(render)

    def parse(self, source):
        body = source.find_all("h5", {"class": "card-title"})
        data = [b.text.strip() for b in body]

        positive = data[7]
        recover = data[9]
        dead = data[10]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

from src.model.parser.base import ParserBase

class ParserJambi(ParserBase):
    WEB_URL = "http://corona.jambiprov.go.id"
    DATA_URL = "http://corona.jambiprov.go.id"

    def __init__(self, render=None):
        super(ParserJambi, self).__init__(render)

    def parse(self, source):
        body = source.find_all(
            "span", {"class": "wp-block-getwid-counter__number"})
        data = [b.text.strip() for b in body]

        positive = data[0]
        recover = data[2]
        dead = data[4]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

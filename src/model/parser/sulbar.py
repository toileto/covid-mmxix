from src.model.parser.base import ParserBase

class ParserSulBar(ParserBase):
    WEB_URL = "https://covid19.sulbarprov.go.id"
    DATA_URL = "https://covid19.sulbarprov.go.id"

    def __init__(self, render=None):
        super(ParserSulBar, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "neuron-counter"})
        data = [b.text.strip() for b in body]

        positive = data[0]
        recover = data[3]
        dead = data[4]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

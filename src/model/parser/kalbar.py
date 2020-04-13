from src.model.parser.base import ParserBase

class ParserKalBar(ParserBase):
    WEB_URL = "https://dinkes.kalbarprov.go.id/covid-19"
    DATA_URL = "https://dinkes.kalbarprov.go.id/covid-19"

    def __init__(self, render=None):
        super(ParserKalBar, self).__init__(render)

    def parse(self, source):
        body = source.find_all("h1", {"class": "elementor-heading-title"})
        data = [x.text.strip() for x in body]

        positive = data[0]
        recover = data[1]
        dead = data[2]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

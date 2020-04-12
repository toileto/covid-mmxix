from src.model.parser.base import ParserBase

class ParserAceh(ParserBase):
    WEB_URL = "https://covid19.acehprov.go.id"
    DATA_URL = "https://covid19.acehprov.go.id"

    def __init__(self, render=None):
        super(ParserAceh, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "col-md-3"})
        data = body[2]

        positive = data.find(id="positif").text.strip()
        recover = data.find(id="sembuh").text.strip()
        dead = data.find(id="p_meninggal").text.strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

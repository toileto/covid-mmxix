from src.model.parser.base import ParserBase

class ParserAceh(ParserBase):
    WEB_URL = "https://covid19.acehprov.go.id"
    DATA_URL = "https://covid19.acehprov.go.id"

    def __init__(self, render=None):
        super(ParserAceh, self).__init__(render)

    def parse(self, source):
        positive = source.find(id="positif").text.strip()
        recover = source.find(id="sembuh").text.strip()
        dead = source.find(id="p_meninggal").text.strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

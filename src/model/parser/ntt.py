from src.model.parser.base import ParserBase

class ParserNTT(ParserBase):
    WEB_URL = "https://covid19.nttprov.go.id"
    DATA_URL = "https://covid19.nttprov.go.id"

    def __init__(self, render=None):
        super(ParserNTT, self).__init__(render)

    def parse(self, source):
        data = source.find(
            "section",
            {"class": "flex flex-col lg:flex-row lg:flex-no-wrap"}
        ).find(
            text="Positif"
        ).parent.parent.parent.text.strip().split()

        positive = data[0]
        recover = data[2]
        dead = data[4]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

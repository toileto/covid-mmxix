from src.model.parser.base import ParserBase

class ParserJaBar(ParserBase):
    WEB_URL = "https://pikobar.jabarprov.go.id"
    DATA_URL = "https://pikobar.jabarprov.go.id"

    def __init__(self, render=None):
        super(ParserJaBar, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "flex justify-between items-baseline text-2xl"})
        data = [x.text.split()[-1].strip() for x in body]

        positive = data[0].strip()
        recover = data[1].strip()
        dead = data[2].strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

from src.model.parser.base import ParserBase

class ParserNTB(ParserBase):
    WEB_URL = "https://corona.ntbprov.go.id"
    DATA_URL = "https://corona.ntbprov.go.id"

    def __init__(self, render=None):
        super(ParserNTB, self).__init__(render)

    def parse(self, source):
        body = source.find_all("h2", {"class": "price"})
        data = body[2].text.split()[-1].strip()
        positive = data.strip()

        body = source.find_all("div", {"class": "col-md-4"})
        data =  body[2].find_all("span")
        value = [d.text.strip().split()[0] for d in data]
        recover = value[2].strip()
        dead = value[3].strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

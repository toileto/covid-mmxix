from src.model.parser.base import ParserBase

class ParserJaTeng(ParserBase):
    WEB_URL = "https://corona.jatengprov.go.id"
    DATA_URL = "https://corona.jatengprov.go.id"

    def __init__(self, render=None):
        super(ParserJaTeng, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "col-lg-3 col-md-6 col-6 mb-3"})
        data = [x.find(
            "div", {"class":"font-counter"}).text.strip().split()[0] for x in body]

        positive = data[0].strip()
        recover = data[2].strip()
        dead = data[3].strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

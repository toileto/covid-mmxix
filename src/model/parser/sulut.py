from src.model.parser.base import ParserBase

class ParserSulUt(ParserBase):
    WEB_URL = "https://corona.sulutprov.go.id"
    DATA_URL = "https://corona.sulutprov.go.id"

    def __init__(self, render=None):
        super(ParserSulUt, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "info-angka red"})
        data = [b.text.strip() for b in body]

        positive = source.find_all(
            "div", {"class": "price-center"}
        )[-1].text.strip().split()[0].strip()
        recover = source.find(
            "i", {"class": "fa-check"}).parent.b.text.strip()
        dead = source.find(
            "i", {"class": "fa-cross-death"}).parent.b.text.strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

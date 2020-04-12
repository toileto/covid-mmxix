from src.model.parser.base import ParserBase

class ParserSulSel(ParserBase):
    WEB_URL = "https://covid19.sulselprov.go.id"
    DATA_URL = "https://covid19.sulselprov.go.id"

    def __init__(self, render=None):
        super(ParserSulSel, self).__init__(render)

    def parse(self, source):
        body = source.find_all("div", {"class": "col-lg-4"})
        data =  body[5].find_all("span")

        value = [d.text.split()[0] for d in data]

        positive = value[0]
        recover = value[3]
        dead = value[5]

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

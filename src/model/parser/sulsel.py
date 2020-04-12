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

        positive = value[0].strip()
        recover = value[3].strip()
        dead = value[5].strip()

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }

from src.model.renderer import render_html

class ParserPusat(object):
    WEB_URL = "https://www.covid19.go.id/"
    DATA_URL = "https://inacovid19.maps.arcgis.com/apps/opsdashboard/index.html#/4411f5e9c69d4ca4be31ac805a0267be"

    def __init__(self):
        self.render_data = render_html(self.DATA_URL)

    def parse_province_data(self):
        body = self.render_data.find("h3").parent.parent.parent
        prov_data = body.find_all("div", {"class": "external-html"})

        result = []
        cols = ["positif", "sembuh", "meninggal"]
        for pd in prov_data:
            r = {}
            temp = pd.find_all("p")

            r["provinsi"] = temp[0].text
            for i in range(1,4):
                t = temp[i].text
                t = t[t.find("\xa0"):].replace(",", "")
                r[cols[i-1]] = int(t)

            result.append(r)

        return result

    def get_province_data(self):
        result = {}
        data = self.parse_province_data()
        data.sort(key=lambda x: x["provinsi"])
        for d in data:
            province = d["provinsi"]
            del d["provinsi"]
            result[province] = {"pusat": d}

        return result

    def get_overview(self):
        data = [
            self.render_data.find(text="Terkonfirmasi"),
            self.render_data.find(text="Sembuh"),
            self.render_data.find(text="Meninggal"),
        ]

        for i, d in enumerate(data):
            data[i] = d.parent.parent.parent.parent.parent.parent.contents[3].text.strip().replace("," , "")

        return {
            "positif": int(data[0]),
            "sembuh": int(data[1]),
            "meninggal": int(data[2]),
        }

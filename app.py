from src.model.parser import parser_pusat, parsers_daerah

cols = ["positif", "sembuh", "meninggal"]

all_data = parser_pusat.get_province_data()

for k in all_data.keys():
    prov_parser = parsers_daerah.get(k)
    if prov_parser:
        try:
            data = prov_parser.get_data_html()
            diff = {}
            for c in cols:
                diff[c] = data[c] - all_data[k]["pusat"][c]
            all_data[k].update({
                "daerah": data,
                "selisih": diff,
                "sumber": prov_parser.WEB_URL
            })

        except:
            all_data[k].update({"error": True})

for k, v in all_data.items():
    print(k, v)

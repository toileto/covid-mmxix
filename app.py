import json
from src.model.parser import parser_pusat, parsers_daerah, WAKTU_JALAN_STR
from src.model.visualizer import visualize_province_table

cols = ["positif", "sembuh", "meninggal"]

# check each province
data_semua_provinsi = parser_pusat.get_province_data()
for k in data_semua_provinsi.keys():
    prov_parser = parsers_daerah.get(k)
    if prov_parser:
        try:
            data = prov_parser.get_data_html()
            diff = {}
            for c in cols:
                diff[c] = data[c] - data_semua_provinsi[k]["pusat"][c]
            data_semua_provinsi[k].update({
                "daerah": data,
                "selisih": diff,
                "sumber": prov_parser.WEB_URL
            })
        except:
            data_semua_provinsi[k].update({"error": True})

# data formatting
tabel_data_provinsi = visualize_province_table(data_semua_provinsi)
summary_data = {
    "waktu_jalan": WAKTU_JALAN_STR,
    "data_semua_provinsi": data_semua_provinsi,
}

# write to file
namafile_ts = WAKTU_JALAN_STR.replace(' ', 'T')

with open(f"data/historical/markdown/README_{namafile_ts}.md", "w") as f:
    f.write(f"#### Update: {WAKTU_JALAN_STR} WIB\n")
    f.write(f"## Tabel Selisih Pusat vs Daerah\n")
    f.write(f"Sumber Pusat: {parser_pusat.DATA_URL}\n")
    f.write(tabel_data_provinsi)

with open(f"data/historical/json/{namafile_ts}.json", "w") as f:
    json.dump(summary_data, f)

def visualize_province_table(data):
    tbody = ""
    total_positive = 0
    total_recover = 0
    total_dead = 0

    for k, v in data.items():
        # sum national stats
        total_positive += v["pusat"]["positif"]
        total_recover += v["pusat"]["sembuh"]
        total_dead += v["pusat"]["meninggal"]

        # format `selisih`
        diff = v.get("selisih")
        if diff:
            for dk in diff.keys():
                if diff[dk] > 0:
                    diff[dk] = f"+{diff[dk]}"
                else:
                    diff[dk] = f"{diff[dk]}"

        tds = ""
        tds += f'<td class="province">{k}</td>'
        tds += f'<td class="national-positive">{v["pusat"]["positif"]}</td>'
        tds += f'<td class="national-recover">{v["pusat"]["sembuh"]}</td>'
        tds += f'<td class="national-deadd">{v["pusat"]["meninggal"]}</td>'
        if v.get("daerah"):
            tds += f'<td class="regional-positive">{v["daerah"]["positif"]} <span class="diff-positive">({diff["positif"]})</span></td>'
            tds += f'<td class="regional-recover">{v["daerah"]["sembuh"]} <span class="diff-recover">({diff["sembuh"]})</span></td>'
            tds += f'<td class="regional-dead">{v["daerah"]["meninggal"]} <span class="diff-dead">({diff["meninggal"]})</span></td>'
            tds += f'<td class="regional-source"><a href="{v["sumber"]}">{v["sumber"]}</a></td>'
        elif v.get("error"):
            tds += f'<td class="regional-error" colspan=3 style="text-align:center">ERROR</td>'
            tds += f'<td class="regional-source"><a href="{v["sumber"]}">{v["sumber"]}</a></td>'
        else:
            tds += '<td class="regional-unknown" colspan=4></td>'
        tbody += f'        <tr>{tds}</tr>\n'


    return f"""<table border="1">
    <thead>
        <tr>
            <th rowspan=2 style="text-align:center">Provinsi</th>
            <th colspan=3 style="text-align:center">Pusat</th>
            <th colspan=4 style="text-align:center">Daerah</th>
        </tr>
        <tr>
            <th>Positif</th>
            <th>Sembuh</th>
            <th>Meninggal</th>
            <th>Positif</th>
            <th>Sembuh</th>
            <th>Meninggal</th>
            <th>Sumber</th>
        </tr>
    </thead>
    <tbody>\n{tbody}    </tbody>
    <tfoot>
        <tr>
            <td><b>TOTAL</b></td>
            <td>{total_positive}</td>
            <td>{total_recover}</td>
            <td>{total_dead}</td>
            <td colspan=4></td>
        </tr>
    </tfoot>
</table>"""

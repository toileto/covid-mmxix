# ina-covid-mmxix
Dashboard untuk menampilkan tingkat keseragaman data statistik kasus COVID-19 di Indonesia antara pusat & daerah. \
[Klik tautan ini untuk informasi lebih lanjut](INFO.md)

<br>

#### Update: 2020-04-23 22:00 WIB
## Selisih Pusat vs Daerah
Sumber Pusat: https://inacovid19.maps.arcgis.com/apps/opsdashboard/index.html#/4411f5e9c69d4ca4be31ac805a0267be
<table>
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
    <tbody>
        <tr><td class="province">Aceh</td><td class="national-positive">7</td><td class="national-recover">4</td><td class="national-dead">1</td><td class="regional-positive">7 <span class="diff-positive">(0)</span></td><td class="regional-recover">4 <span class="diff-recover">(0)</span></td><td class="regional-dead">1 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://covid19.acehprov.go.id">https://covid19.acehprov.go.id</a></td></tr>
        <tr><td class="province">Bali</td><td class="national-positive">167</td><td class="national-recover">55</td><td class="national-dead">4</td><td class="regional-positive">167 <span class="diff-positive">(0)</span></td><td class="regional-recover">55 <span class="diff-recover">(0)</span></td><td class="regional-dead">4 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://infocorona.baliprov.go.id">https://infocorona.baliprov.go.id</a></td></tr>
        <tr><td class="province">Banten</td><td class="national-positive">337</td><td class="national-recover">29</td><td class="national-dead">35</td><td class="regional-positive">288 <span class="diff-positive">(-49)</span></td><td class="regional-recover">50 <span class="diff-recover">(+21)</span></td><td class="regional-dead">43 <span class="diff-dead">(+8)</span></td><td class="regional-source"><a href="https://infocorona.bantenprov.go.id">https://infocorona.bantenprov.go.id</a></td></tr>
        <tr><td class="province">Bengkulu</td><td class="national-positive">8</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">DKI Jakarta</td><td class="national-positive">3517</td><td class="national-recover">326</td><td class="national-dead">301</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Daerah Istimewa Yogyakarta</td><td class="national-positive">76</td><td class="national-recover">32</td><td class="national-dead">7</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Gorontalo</td><td class="national-positive">7</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Jambi</td><td class="national-positive">14</td><td class="national-recover">1</td><td class="national-dead">0</td><td class="regional-positive">13 <span class="diff-positive">(-1)</span></td><td class="regional-recover">1 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="http://corona.jambiprov.go.id">http://corona.jambiprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Barat</td><td class="national-positive">784</td><td class="national-recover">87</td><td class="national-dead">74</td><td class="regional-positive">784 <span class="diff-positive">(0)</span></td><td class="regional-recover">87 <span class="diff-recover">(0)</span></td><td class="regional-dead">74 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://pikobar.jabarprov.go.id">https://pikobar.jabarprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Tengah</td><td class="national-positive">538</td><td class="national-recover">54</td><td class="national-dead">53</td><td class="regional-positive">493 <span class="diff-positive">(-45)</span></td><td class="regional-recover">62 <span class="diff-recover">(+8)</span></td><td class="regional-dead">60 <span class="diff-dead">(+7)</span></td><td class="regional-source"><a href="https://corona.jatengprov.go.id">https://corona.jatengprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Timur</td><td class="national-positive">664</td><td class="national-recover">112</td><td class="national-dead">60</td><td class="regional-positive">662 <span class="diff-positive">(-2)</span></td><td class="regional-recover">127 <span class="diff-recover">(+15)</span></td><td class="regional-dead">66 <span class="diff-dead">(+6)</span></td><td class="regional-source"><a href="https://infocovid19.jatimprov.go.id">https://infocovid19.jatimprov.go.id</a></td></tr>
        <tr><td class="province">Kalimantan Barat</td><td class="national-positive">50</td><td class="national-recover">7</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Selatan</td><td class="national-positive">114</td><td class="national-recover">9</td><td class="national-dead">6</td><td class="regional-positive">113 <span class="diff-positive">(-1)</span></td><td class="regional-recover">10 <span class="diff-recover">(+1)</span></td><td class="regional-dead">7 <span class="diff-dead">(+1)</span></td><td class="regional-source"><a href="https://corona.kalselprov.go.id">https://corona.kalselprov.go.id</a></td></tr>
        <tr><td class="province">Kalimantan Tengah</td><td class="national-positive">83</td><td class="national-recover">9</td><td class="national-dead">4</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Timur</td><td class="national-positive">74</td><td class="national-recover">11</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Utara</td><td class="national-positive">77</td><td class="national-recover">2</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kepulauan Bangka Belitung</td><td class="national-positive">8</td><td class="national-recover">2</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kepulauan Riau</td><td class="national-positive">83</td><td class="national-recover">8</td><td class="national-dead">8</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Lampung</td><td class="national-positive">38</td><td class="national-recover">10</td><td class="national-dead">5</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Maluku</td><td class="national-positive">17</td><td class="national-recover">10</td><td class="national-dead">0</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Maluku Utara</td><td class="national-positive">14</td><td class="national-recover">2</td><td class="national-dead">0</td><td class="regional-positive">14 <span class="diff-positive">(0)</span></td><td class="regional-recover">2 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="http://corona.malutprov.go.id">http://corona.malutprov.go.id</a></td></tr>
        <tr><td class="province">Nusa Tenggara Barat</td><td class="national-positive">115</td><td class="national-recover">13</td><td class="national-dead">4</td><td class="regional-positive">153 <span class="diff-positive">(+38)</span></td><td class="regional-recover">15 <span class="diff-recover">(+2)</span></td><td class="regional-dead">4 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.ntbprov.go.id">https://corona.ntbprov.go.id</a></td></tr>
        <tr><td class="province">Nusa Tenggara Timur</td><td class="national-positive">1</td><td class="national-recover">0</td><td class="national-dead">0</td><td class="regional-error" colspan=3 style="text-align:center">ERROR</td><td class="regional-source"><a href="https://covid19.nttprov.go.id">https://covid19.nttprov.go.id</a></td></tr>
        <tr><td class="province">Papua</td><td class="national-positive">130</td><td class="national-recover">32</td><td class="national-dead">6</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Papua Barat</td><td class="national-positive">13</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Riau</td><td class="national-positive">36</td><td class="national-recover">9</td><td class="national-dead">4</td><td class="regional-positive">36 <span class="diff-positive">(0)</span></td><td class="regional-recover">9 <span class="diff-recover">(0)</span></td><td class="regional-dead">4 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.riau.go.id">https://corona.riau.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Barat</td><td class="national-positive">8</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-positive">8 <span class="diff-positive">(0)</span></td><td class="regional-recover">1 <span class="diff-recover">(0)</span></td><td class="regional-dead">1 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://covid19.sulbarprov.go.id">https://covid19.sulbarprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Selatan</td><td class="national-positive">397</td><td class="national-recover">80</td><td class="national-dead">34</td><td class="regional-error" colspan=3 style="text-align:center">ERROR</td><td class="regional-source"><a href="https://covid19.sulselprov.go.id">https://covid19.sulselprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Tengah</td><td class="national-positive">29</td><td class="national-recover">3</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sulawesi Tenggara</td><td class="national-positive">37</td><td class="national-recover">4</td><td class="national-dead">2</td><td class="regional-positive">4 <span class="diff-positive">(-33)</span></td><td class="regional-recover">1 <span class="diff-recover">(-3)</span></td><td class="regional-dead">0 <span class="diff-dead">(-2)</span></td><td class="regional-source"><a href="https://dinkes.sultraprov.go.id">https://dinkes.sultraprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Utara</td><td class="national-positive">31</td><td class="national-recover">5</td><td class="national-dead">3</td><td class="regional-positive">32 <span class="diff-positive">(+1)</span></td><td class="regional-recover">6 <span class="diff-recover">(+1)</span></td><td class="regional-dead">3 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.sulutprov.go.id">https://corona.sulutprov.go.id</a></td></tr>
        <tr><td class="province">Sumatera Barat</td><td class="national-positive">86</td><td class="national-recover">16</td><td class="national-dead">9</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sumatera Selatan</td><td class="national-positive">93</td><td class="national-recover">5</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sumatera Utara</td><td class="national-positive">95</td><td class="national-recover">21</td><td class="national-dead">11</td><td class="regional-unknown" colspan=4></td></tr>
    </tbody>
    <tfoot>
        <tr>
            <td><b>TOTAL</b></td>
            <td><b>7748</b></td>
            <td><b>960</b></td>
            <td><b>647</b></td>
            <td colspan=4></td>
        </tr>
    </tfoot>
</table>
<br>

### Overview Pusat
| Positif | Sembuh | Meninggal |
|--|--|--|
| 7775 | 960 | 647 |
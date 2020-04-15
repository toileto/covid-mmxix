# ina-covid-mmxix
Dashboard untuk menampilkan tingkat keseragaman data statistik kasus COVID-19 di Indonesia antara pusat & daerah. \
[Klik tautan ini untuk informasi lebih lanjut](INFO.md)

<br>

#### Update: 2020-04-15 19:00 WIB
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
        <tr><td class="province">Aceh</td><td class="national-positive">5</td><td class="national-recover">4</td><td class="national-dead">1</td><td class="regional-positive">5 <span class="diff-positive">(0)</span></td><td class="regional-recover">4 <span class="diff-recover">(0)</span></td><td class="regional-dead">1 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://covid19.acehprov.go.id">https://covid19.acehprov.go.id</a></td></tr>
        <tr><td class="province">Bali</td><td class="national-positive">98</td><td class="national-recover">23</td><td class="national-dead">2</td><td class="regional-positive">98 <span class="diff-positive">(0)</span></td><td class="regional-recover">23 <span class="diff-recover">(0)</span></td><td class="regional-dead">2 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://infocorona.baliprov.go.id">https://infocorona.baliprov.go.id</a></td></tr>
        <tr><td class="province">Banten</td><td class="national-positive">281</td><td class="national-recover">7</td><td class="national-dead">25</td><td class="regional-positive">216 <span class="diff-positive">(-65)</span></td><td class="regional-recover">27 <span class="diff-recover">(+20)</span></td><td class="regional-dead">36 <span class="diff-dead">(+11)</span></td><td class="regional-source"><a href="https://infocorona.bantenprov.go.id">https://infocorona.bantenprov.go.id</a></td></tr>
        <tr><td class="province">Bengkulu</td><td class="national-positive">4</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">DKI Jakarta</td><td class="national-positive">2474</td><td class="national-recover">164</td><td class="national-dead">242</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Daerah Istimewa Yogyakarta</td><td class="national-positive">62</td><td class="national-recover">18</td><td class="national-dead">7</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Gorontalo</td><td class="national-positive">1</td><td class="national-recover">0</td><td class="national-dead">0</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Jambi</td><td class="national-positive">6</td><td class="national-recover">0</td><td class="national-dead">0</td><td class="regional-positive">6 <span class="diff-positive">(0)</span></td><td class="regional-recover">0 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="http://corona.jambiprov.go.id">http://corona.jambiprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Barat</td><td class="national-positive">559</td><td class="national-recover">23</td><td class="national-dead">52</td><td class="regional-positive">540 <span class="diff-positive">(-19)</span></td><td class="regional-recover">23 <span class="diff-recover">(0)</span></td><td class="regional-dead">52 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://pikobar.jabarprov.go.id">https://pikobar.jabarprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Tengah</td><td class="national-positive">292</td><td class="national-recover">19</td><td class="national-dead">27</td><td class="regional-positive">233 <span class="diff-positive">(-59)</span></td><td class="regional-recover">33 <span class="diff-recover">(+14)</span></td><td class="regional-dead">38 <span class="diff-dead">(+11)</span></td><td class="regional-source"><a href="https://corona.jatengprov.go.id">https://corona.jatengprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Timur</td><td class="national-positive">499</td><td class="national-recover">81</td><td class="national-dead">45</td><td class="regional-positive">499 <span class="diff-positive">(0)</span></td><td class="regional-recover">86 <span class="diff-recover">(+5)</span></td><td class="regional-dead">46 <span class="diff-dead">(+1)</span></td><td class="regional-source"><a href="https://infocovid19.jatimprov.go.id">https://infocovid19.jatimprov.go.id</a></td></tr>
        <tr><td class="province">Kalimantan Barat</td><td class="national-positive">13</td><td class="national-recover">5</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Selatan</td><td class="national-positive">49</td><td class="national-recover">3</td><td class="national-dead">6</td><td class="regional-positive">49 <span class="diff-positive">(0)</span></td><td class="regional-recover">5 <span class="diff-recover">(+2)</span></td><td class="regional-dead">7 <span class="diff-dead">(+1)</span></td><td class="regional-source"><a href="https://corona.kalselprov.go.id">https://corona.kalselprov.go.id</a></td></tr>
        <tr><td class="province">Kalimantan Tengah</td><td class="national-positive">33</td><td class="national-recover">8</td><td class="national-dead">2</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Timur</td><td class="national-positive">35</td><td class="national-recover">6</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Utara</td><td class="national-positive">20</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kepulauan Bangka Belitung</td><td class="national-positive">5</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kepulauan Riau</td><td class="national-positive">32</td><td class="national-recover">2</td><td class="national-dead">5</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Lampung</td><td class="national-positive">20</td><td class="national-recover">1</td><td class="national-dead">5</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Maluku</td><td class="national-positive">14</td><td class="national-recover">1</td><td class="national-dead">0</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Maluku Utara</td><td class="national-positive">4</td><td class="national-recover">2</td><td class="national-dead">0</td><td class="regional-positive">4 <span class="diff-positive">(0)</span></td><td class="regional-recover">2 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="http://corona.malutprov.go.id">http://corona.malutprov.go.id</a></td></tr>
        <tr><td class="province">Nusa Tenggara Barat</td><td class="national-positive">37</td><td class="national-recover">2</td><td class="national-dead">2</td><td class="regional-positive">41 <span class="diff-positive">(+4)</span></td><td class="regional-recover">5 <span class="diff-recover">(+3)</span></td><td class="regional-dead">2 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.ntbprov.go.id">https://corona.ntbprov.go.id</a></td></tr>
        <tr><td class="province">Nusa Tenggara Timur</td><td class="national-positive">1</td><td class="national-recover">0</td><td class="national-dead">0</td><td class="regional-positive">0 <span class="diff-positive">(-1)</span></td><td class="regional-recover">0 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://covid19.nttprov.go.id">https://covid19.nttprov.go.id</a></td></tr>
        <tr><td class="province">Papua</td><td class="national-positive">75</td><td class="national-recover">5</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Papua Barat</td><td class="national-positive">2</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Riau</td><td class="national-positive">20</td><td class="national-recover">1</td><td class="national-dead">0</td><td class="regional-positive">20 <span class="diff-positive">(0)</span></td><td class="regional-recover">2 <span class="diff-recover">(+1)</span></td><td class="regional-dead">2 <span class="diff-dead">(+2)</span></td><td class="regional-source"><a href="https://corona.riau.go.id">https://corona.riau.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Barat</td><td class="national-positive">7</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-positive">7 <span class="diff-positive">(0)</span></td><td class="regional-recover">1 <span class="diff-recover">(0)</span></td><td class="regional-dead">1 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://covid19.sulbarprov.go.id">https://covid19.sulbarprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Selatan</td><td class="national-positive">242</td><td class="national-recover">42</td><td class="national-dead">15</td><td class="regional-positive">240 <span class="diff-positive">(-2)</span></td><td class="regional-recover">42 <span class="diff-recover">(0)</span></td><td class="regional-dead">22 <span class="diff-dead">(+7)</span></td><td class="regional-source"><a href="https://covid19.sulselprov.go.id">https://covid19.sulselprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Tengah</td><td class="national-positive">22</td><td class="national-recover">2</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sulawesi Tenggara</td><td class="national-positive">24</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-positive">4 <span class="diff-positive">(-20)</span></td><td class="regional-recover">1 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(-1)</span></td><td class="regional-source"><a href="https://dinkes.sultraprov.go.id">https://dinkes.sultraprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Utara</td><td class="national-positive">18</td><td class="national-recover">2</td><td class="national-dead">2</td><td class="regional-positive">18 <span class="diff-positive">(0)</span></td><td class="regional-recover">4 <span class="diff-recover">(+2)</span></td><td class="regional-dead">2 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.sulutprov.go.id">https://corona.sulutprov.go.id</a></td></tr>
        <tr><td class="province">Sumatera Barat</td><td class="national-positive">55</td><td class="national-recover">8</td><td class="national-dead">4</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sumatera Selatan</td><td class="national-positive">22</td><td class="national-recover">4</td><td class="national-dead">2</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sumatera Utara</td><td class="national-positive">78</td><td class="national-recover">10</td><td class="national-dead">9</td><td class="regional-unknown" colspan=4></td></tr>
    </tbody>
    <tfoot>
        <tr>
            <td><b>TOTAL</b></td>
            <td><b>5109</b></td>
            <td><b>446</b></td>
            <td><b>469</b></td>
            <td colspan=4></td>
        </tr>
    </tfoot>
</table>
<br>

### Overview Pusat
| Positif | Sembuh | Meninggal |
|--|--|--|
| 5136 | 446 | 469 |
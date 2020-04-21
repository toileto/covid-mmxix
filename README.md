# ina-covid-mmxix
Dashboard untuk menampilkan tingkat keseragaman data statistik kasus COVID-19 di Indonesia antara pusat & daerah. \
[Klik tautan ini untuk informasi lebih lanjut](INFO.md)

<br>

#### Update: 2020-04-21 22:00 WIB
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
        <tr><td class="province">Bali</td><td class="national-positive">150</td><td class="national-recover">42</td><td class="national-dead">3</td><td class="regional-positive">150 <span class="diff-positive">(0)</span></td><td class="regional-recover">42 <span class="diff-recover">(0)</span></td><td class="regional-dead">3 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://infocorona.baliprov.go.id">https://infocorona.baliprov.go.id</a></td></tr>
        <tr><td class="province">Banten</td><td class="national-positive">341</td><td class="national-recover">17</td><td class="national-dead">35</td><td class="regional-positive">275 <span class="diff-positive">(-66)</span></td><td class="regional-recover">40 <span class="diff-recover">(+23)</span></td><td class="regional-dead">43 <span class="diff-dead">(+8)</span></td><td class="regional-source"><a href="https://infocorona.bantenprov.go.id">https://infocorona.bantenprov.go.id</a></td></tr>
        <tr><td class="province">Bengkulu</td><td class="national-positive">8</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">DKI Jakarta</td><td class="national-positive">3260</td><td class="national-recover">286</td><td class="national-dead">298</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Daerah Istimewa Yogyakarta</td><td class="national-positive">72</td><td class="national-recover">30</td><td class="national-dead">7</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Gorontalo</td><td class="national-positive">7</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Jambi</td><td class="national-positive">13</td><td class="national-recover">1</td><td class="national-dead">0</td><td class="regional-error" colspan=3 style="text-align:center">ERROR</td><td class="regional-source"><a href="http://corona.jambiprov.go.id">http://corona.jambiprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Barat</td><td class="national-positive">756</td><td class="national-recover">75</td><td class="national-dead">68</td><td class="regional-positive">756 <span class="diff-positive">(0)</span></td><td class="regional-recover">75 <span class="diff-recover">(0)</span></td><td class="regional-dead">68 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://pikobar.jabarprov.go.id">https://pikobar.jabarprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Tengah</td><td class="national-positive">449</td><td class="national-recover">51</td><td class="national-dead">44</td><td class="regional-positive">400 <span class="diff-positive">(-49)</span></td><td class="regional-recover">52 <span class="diff-recover">(+1)</span></td><td class="regional-dead">52 <span class="diff-dead">(+8)</span></td><td class="regional-source"><a href="https://corona.jatengprov.go.id">https://corona.jatengprov.go.id</a></td></tr>
        <tr><td class="province">Jawa Timur</td><td class="national-positive">603</td><td class="national-recover">100</td><td class="national-dead">56</td><td class="regional-positive">603 <span class="diff-positive">(0)</span></td><td class="regional-recover">101 <span class="diff-recover">(+1)</span></td><td class="regional-dead">58 <span class="diff-dead">(+2)</span></td><td class="regional-source"><a href="https://infocovid19.jatimprov.go.id">https://infocovid19.jatimprov.go.id</a></td></tr>
        <tr><td class="province">Kalimantan Barat</td><td class="national-positive">27</td><td class="national-recover">7</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Selatan</td><td class="national-positive">98</td><td class="national-recover">9</td><td class="national-dead">6</td><td class="regional-positive">99 <span class="diff-positive">(+1)</span></td><td class="regional-recover">10 <span class="diff-recover">(+1)</span></td><td class="regional-dead">7 <span class="diff-dead">(+1)</span></td><td class="regional-source"><a href="https://corona.kalselprov.go.id">https://corona.kalselprov.go.id</a></td></tr>
        <tr><td class="province">Kalimantan Tengah</td><td class="national-positive">67</td><td class="national-recover">9</td><td class="national-dead">4</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Timur</td><td class="national-positive">68</td><td class="national-recover">11</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kalimantan Utara</td><td class="national-positive">77</td><td class="national-recover">2</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kepulauan Bangka Belitung</td><td class="national-positive">8</td><td class="national-recover">2</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Kepulauan Riau</td><td class="national-positive">81</td><td class="national-recover">8</td><td class="national-dead">8</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Lampung</td><td class="national-positive">27</td><td class="national-recover">10</td><td class="national-dead">5</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Maluku</td><td class="national-positive">17</td><td class="national-recover">10</td><td class="national-dead">0</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Maluku Utara</td><td class="national-positive">4</td><td class="national-recover">2</td><td class="national-dead">0</td><td class="regional-positive">4 <span class="diff-positive">(0)</span></td><td class="regional-recover">2 <span class="diff-recover">(0)</span></td><td class="regional-dead">0 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="http://corona.malutprov.go.id">http://corona.malutprov.go.id</a></td></tr>
        <tr><td class="province">Nusa Tenggara Barat</td><td class="national-positive">93</td><td class="national-recover">11</td><td class="national-dead">4</td><td class="regional-positive">108 <span class="diff-positive">(+15)</span></td><td class="regional-recover">11 <span class="diff-recover">(0)</span></td><td class="regional-dead">4 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.ntbprov.go.id">https://corona.ntbprov.go.id</a></td></tr>
        <tr><td class="province">Nusa Tenggara Timur</td><td class="national-positive">1</td><td class="national-recover">0</td><td class="national-dead">0</td><td class="regional-error" colspan=3 style="text-align:center">ERROR</td><td class="regional-source"><a href="https://covid19.nttprov.go.id">https://covid19.nttprov.go.id</a></td></tr>
        <tr><td class="province">Papua</td><td class="national-positive">118</td><td class="national-recover">28</td><td class="national-dead">6</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Papua Barat</td><td class="national-positive">7</td><td class="national-recover">0</td><td class="national-dead">1</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Riau</td><td class="national-positive">35</td><td class="national-recover">9</td><td class="national-dead">4</td><td class="regional-positive">35 <span class="diff-positive">(0)</span></td><td class="regional-recover">9 <span class="diff-recover">(0)</span></td><td class="regional-dead">4 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.riau.go.id">https://corona.riau.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Barat</td><td class="national-positive">7</td><td class="national-recover">1</td><td class="national-dead">1</td><td class="regional-positive">7 <span class="diff-positive">(0)</span></td><td class="regional-recover">1 <span class="diff-recover">(0)</span></td><td class="regional-dead">1 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://covid19.sulbarprov.go.id">https://covid19.sulbarprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Selatan</td><td class="national-positive">374</td><td class="national-recover">73</td><td class="national-dead">30</td><td class="regional-error" colspan=3 style="text-align:center">ERROR</td><td class="regional-source"><a href="https://covid19.sulselprov.go.id">https://covid19.sulselprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Tengah</td><td class="national-positive">27</td><td class="national-recover">3</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sulawesi Tenggara</td><td class="national-positive">37</td><td class="national-recover">4</td><td class="national-dead">2</td><td class="regional-positive">4 <span class="diff-positive">(-33)</span></td><td class="regional-recover">1 <span class="diff-recover">(-3)</span></td><td class="regional-dead">0 <span class="diff-dead">(-2)</span></td><td class="regional-source"><a href="https://dinkes.sultraprov.go.id">https://dinkes.sultraprov.go.id</a></td></tr>
        <tr><td class="province">Sulawesi Utara</td><td class="national-positive">20</td><td class="national-recover">5</td><td class="national-dead">3</td><td class="regional-positive">20 <span class="diff-positive">(0)</span></td><td class="regional-recover">5 <span class="diff-recover">(0)</span></td><td class="regional-dead">3 <span class="diff-dead">(0)</span></td><td class="regional-source"><a href="https://corona.sulutprov.go.id">https://corona.sulutprov.go.id</a></td></tr>
        <tr><td class="province">Sumatera Barat</td><td class="national-positive">76</td><td class="national-recover">13</td><td class="national-dead">7</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sumatera Selatan</td><td class="national-positive">89</td><td class="national-recover">5</td><td class="national-dead">3</td><td class="regional-unknown" colspan=4></td></tr>
        <tr><td class="province">Sumatera Utara</td><td class="national-positive">84</td><td class="national-recover">13</td><td class="national-dead">9</td><td class="regional-unknown" colspan=4></td></tr>
    </tbody>
    <tfoot>
        <tr>
            <td><b>TOTAL</b></td>
            <td><b>7108</b></td>
            <td><b>842</b></td>
            <td><b>616</b></td>
            <td colspan=4></td>
        </tr>
    </tfoot>
</table>
<br>

### Overview Pusat
| Positif | Sembuh | Meninggal |
|--|--|--|
| 7135 | 842 | 616 |
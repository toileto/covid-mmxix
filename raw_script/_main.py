from datetime import datetime
from dateutil import tz
from lxml import html
import json
import requests
import pandas as pd

JKT = tz.gettz('Asia/Jakarta')

# Pusat
def scrape_pusat():
    url = (
        'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/'
        'COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?f=json&where='
        '(Kasus_Posi%20%3C%3E%200)%20AND%20(Provinsi%20%3C%3E%20%27Indonesia'
        '%27)&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFi'
        'elds=*&orderByFields=Kasus_Posi%20desc&resultOffset=0&resultRecordC'
        'ount=34&cacheHint=true'
    )

    # Start fetching data
    fetched = requests.get(url)
    data = fetched.json()

    all_data = list()

    for i in data['features']:
      _data = i['attributes']
      del _data['FID']
      all_data.append(_data)

    df_pusat = pd.DataFrame.from_records(all_data)
    df_pusat = df_pusat.rename(
        columns={
            "Kode_Provi":"id",
            "Provinsi":"provinsi",
            "Kasus_Posi":"positif",
            "Kasus_Semb":"sembuh",
            "Kasus_Meni":"meninggal"
        }
    ).sort_values(by='provinsi')

    df_pusat['id'] = df_pusat['id'].astype('int')
    df_pusat['sumber'] = 'pusat'
    df_pusat['retrieved'] = datetime.now(tz=JKT)

    return df_pusat

# DI Aceh
def scrape_aceh():
    url = 'https://covid.bravo.siat.web.id/json/covid'

    # Start fetching data
    fetched = requests.get(url)
    data = fetched.json()
    df_aceh = pd.DataFrame(data)
    df_aceh = df_aceh[
      ['labPositif', 'positifSembuh', 'positifMeninggal', 'positifRawat']
    ]
    df_aceh = df_aceh.rename(
        columns = {
            'labPositif':'positif',
            'positifSembuh':'sembuh',
            'positifMeninggal':'meninggal',
            'positifRawat': 'dirawat'
        }
    ).apply(lambda x : x.astype(int))

    df_aceh['provinsi'] = 'Aceh'

    df_aceh = (
        df_aceh
        .groupby(by='provinsi', as_index=False)
        ['positif', 'sembuh', 'meninggal']
        .sum()
    )

    df_aceh['sumber'] = 'daerah'
    df_aceh['retrieved'] = datetime.now(tz=JKT)

    return df_aceh

# Banten
def scrape_banten():
    page = requests.get(
        'https://infocorona.bantenprov.go.id/kasus-terkonfirmasi'
    )
    tree = html.fromstring(page.content)

    xpath_positif = (
        '/html/body/div/div/section[2]/div/div[1]/div/div/'
        'table/tbody/tr[9]/td[4]/b'
    )
    xpath_meninggal = (
        '/html/body/div/div/section[2]/div/div[1]/div/div/'
        'table/tbody/tr[9]/td[3]/b'
    )
    xpath_sembuh = (
        '/html/body/div/div/section[2]/div/div[1]/'
        'div/div/table/tbody/tr[9]/td[1]/b'
    )

    positif = int(tree.xpath(xpath_positif)[0].text_content())
    meninggal = int(tree.xpath(xpath_meninggal)[0].text_content())
    sembuh = int(tree.xpath(xpath_sembuh)[0].text_content())

    banten = [{
        'provinsi':'Banten',
        'positif':positif,
        'meninggal':meninggal,
        'sembuh':sembuh,
        'sumber':'daerah',
        'retrieved': datetime.now(tz=JKT)
    }]

    df_banten = pd.DataFrame.from_records(banten)

    return df_banten


# Sumsel
def scrape_sumsel():
    url = (
        'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/'
        'services/Statistik_Perkembangan_COVID19_Indonesia/FeatureServer/'
        '0/query?f=json&where=Tanggal%3Ctimestamp%20%272020-04-11%2017:00:'
        '00%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&ou'
        'tFields=*&orderByFields=Tanggal%20asc&resultOffset=0&resultRecord'
        'Count=2000&cacheHint=true'
    )

    # Start fetching data
    fetched = requests.get(url)
    data = fetched.json()

    all_data = list()

    for i in data['features']:
      _data = i['attributes']
      new_data = dict()
      for key, value in _data.items():
        if key in ('Tanggal', 'Pembaruan_Terakhir') and\
          value is not None:
          value = datetime.fromtimestamp(value / 1000)
        new_data[key.lower()] = value
      all_data.append(new_data)

    df_sumsel = pd.DataFrame.from_records(all_data)
    df_sumsel = df_sumsel[
        ['hari_ke', 'tanggal', 'jumlah_kasus_kumulatif',
         'jumlah_pasien_sembuh', 'jumlah_pasien_meninggal']
    ]
    df_susmel = df_sumsel.rename(
        columns = {
            'jumlah_kasus_kumulatif':'positif',
            'jumlah_pasien_sembuh': 'sembuh',
            'jumlah_pasien_meninggal':'meninggal'
        }
    )
    df_sumsel['sumber'] = 'daerah'
    df_sumsel['retrieved'] = datetime.now(tz=JKT)

    return df_sumsel
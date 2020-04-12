# ina-covid-mmxix
Dashboard untuk menampilkan tingkat keseragaman data statistik kasus COVID-19 di Indonesia antara pusat & daerah.

## Motivasi
1. Menyajikan data (yang diusahakan) paling baru, untuk dapat dibandingkan dengan mudah antara versi pusat & daerah
2. Menampilkan perbedaan data yang diharapkan dapat dikoreksi kemudian \
    (contoh: *overall* kasus positif berbeda dengan total kasus positif per Provinsi)
3. Membuat aplikasi yang dapat dijalankan sendiri untuk mengetahui data paling terkini
4. Menampilkan data rujukan untuk masing-masing Provinsi
5. Selingan karena bosan selama masa PPSB ^^a

## Cara pemakaian
Kami mengusahakan untuk memperbarui data secara reguler di [Halaman Utama](https://github.com/toileto/ina-covid-mmxix#ina-covid-mmxix). \
Namun jika dirasa data yang kami tampilkan masih kurang *update*, Anda dapat melakukannya secara mandiri dengan cara:

#### A. Prasyarat
1. Pastikan program `python3` sudah ter*install* di komputer Anda ([tutorial](https://realpython.com/installing-python/))
    ```
    # jalankan command di bawah untuk memastikan

    python3 --version
    ```
2. Dan ada `Google Chrome` ter*install* juga ([rujukan](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en-GB))

#### B. Cara menjalankan
1. *Install* terlebih dahulu *library* yang diperlukan
    ```
    pip3 install -r requirements.txt
    ```
2. Jalankan program utama
    ```
    python3 app.py
    ```
3. Tunggu beberapa saat
4. Setelah program selesai buka `README.md` untuk melihat hasil terbaru \
    Untuk hasil yang lebih baik Anda bisa menyalin isinya ke *[online markdown viewer](https://lmgtfy.com/?q=online+markdown+viewer)*

#### C. Lain-lain
- Dashboard historis dapat diakses di [data/historical/markdown](data/historical/markdown)
- Untuk mempermudah pemrosesan data, kami juga menyiapkan format JSON yang dapat diakses di [data/historical/json](data/historical/json)

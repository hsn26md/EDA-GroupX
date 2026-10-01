import pandas as pd

# Define the full data dictionary for the bedtime screen time & sleep debt dataset
data_dict = [
    {
        'nama_kolom': 'user_id',
        'deskripsi': 'Kode pengenal unik untuk setiap individu responden dalam survei.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '-',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Pengenal langsung',
        'tindakan_penanganan': 'Hapus / Hash'
    },
    {
        'nama_kolom': 'age',
        'deskripsi': 'Usia responden dalam satuan tahun saat survei dilaksanakan.',
        'tipe_data': 'int64',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Tahun',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Generalisasi (diubah ke kelompok umur)'
    },
    {
        'nama_kolom': 'gender',
        'deskripsi': 'Identitas jenis kelamin yang dilaporkan secara mandiri oleh responden.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '-',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'occupation_type',
        'deskripsi': 'Kategori bidang pekerjaan atau status profesi utama responden.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '-',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Pertahankan / Generalisasi jika k < 5'
    },
    {
        'nama_kolom': 'chronotype',
        'deskripsi': 'Karakteristik pola biologis ritme sirkadian/tidur alami responden (misal: Night Owl, Morning Lark, Intermediate).',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '-',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'bedtime_phone_minutes',
        'deskripsi': 'Rata-rata durasi penggunaan ponsel di tempat tidur sebelum tidur dalam satuan menit.',
        'tipe_data': 'int64',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Menit',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'primary_bedtime_app',
        'deskripsi': 'Aplikasi ponsel utama yang paling sering diakses responden tepat sebelum tidur.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '-',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'screen_brightness',
        'deskripsi': 'Tingkat persentase kecerahan layar ponsel yang digunakan sebelum tidur.',
        'tipe_data': 'float64',
        'skala_pengukuran': 'Rasio',
        'satuan': '%',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'daily_screen_time_hours',
        'deskripsi': 'Total estimasi waktu tatap layar (screen time) harian responden dalam satuan jam.',
        'tipe_data': 'float64',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Jam',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'total_sleep_hours',
        'deskripsi': 'Total durasi waktu tidur efektif yang didapatkan responden per malam dalam satuan jam.',
        'tipe_data': 'float64',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Jam',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    },
    {
        'nama_kolom': 'sleep_debt_category',
        'deskripsi': 'Klasifikasi tingkat keparahan akumulasi utang tidur (sleep debt) yang dialami responden.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Ordinal',
        'satuan': '-',
        'nilai_kosong': 0,
        'sumber': 'Formulir Survei Kaggle',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan'
    }
]

df_kamus = pd.DataFrame(data_dict)

# Save as CSV
csv_filename = "data_dictionary.csv"
df_kamus.to_csv(csv_filename, index=False)

# Save as Markdown
md_filename = "data_dictionary.md"
with open(md_filename, "w", encoding="utf-8") as f:
    f.write("# Kamus Data — Bedtime Screen Time & Sleep Debt Dataset\n\n")
    f.write(df_kamus.to_markdown(index=False))

print(f"Created {csv_filename} and {md_filename}")
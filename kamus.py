import pandas as pd
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
    }
]
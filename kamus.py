import pandas as pd

data_dict = [
    {
        'nama_kolom': 'user_id',
        'deskripsi': 'Kode pengenal unik/pseudonim untuk setiap individu responden dalam survei.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '—',
        'contoh_nilai': 'USR-00001',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Pertahankan / Hash',
        'catatan': 'Primary key (8.500 entri unik).'
    },
    {
        'nama_kolom': 'age',
        'deskripsi': 'Usia responden dalam satuan tahun saat survei dilaksanakan.',
        'tipe_data': 'int',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Tahun',
        'contoh_nilai': '29',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Generalisasi',
        'catatan': 'Disarankan dikelompokkan ke dalam rentang umur.'
    },
]
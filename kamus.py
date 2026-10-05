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
    {
        'nama_kolom': 'gender',
        'deskripsi': 'Identitas jenis kelamin yang dilaporkan secara mandiri oleh responden.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '—',
        'contoh_nilai': 'Female',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Terdiri dari 3 kategori: Female, Male, Non-Binary.'
    },
    {
        'nama_kolom': 'occupation_type',
        'deskripsi': 'Kategori bidang pekerjaan atau status profesi utama responden.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '—',
        'contoh_nilai': 'Healthcare / Shift Worker',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Quasi-identifier',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': '5 kategori profesi utama.'
    },
    {
        'nama_kolom': 'chronotype',
        'deskripsi': 'Karakteristik pola biologis ritme sirkadian/tidur alami responden.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '—',
        'contoh_nilai': 'Intermediate',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Data fisiologis (Morning Lark, Intermediate, Night Owl).'
    },
    {
        'nama_kolom': 'bedtime_phone_minutes',
        'deskripsi': 'Durasi penggunaan ponsel sebelum tidur dalam satuan menit.',
        'tipe_data': 'int',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Menit',
        'contoh_nilai': '179',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Nilai berkisar 1–180 menit.'
    },
    {
        'nama_kolom': 'primary_bedtime_app',
        'deskripsi': 'Aplikasi ponsel utama yang paling sering dibuka responden sebelum tidur.',
        'tipe_data': 'string',
        'skala_pengukuran': 'Nominal',
        'satuan': '—',
        'contoh_nilai': 'Instagram / Reddit',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': '6 opsi kategori aplikasi.'
    },
    {
        'nama_kolom': 'screen_brightness_pct',
        'deskripsi': 'Tingkat kecerahan layar ponsel yang digunakan sebelum tidur dalam persentase.',
        'tipe_data': 'int',
        'skala_pengukuran': 'Rasio',
        'satuan': '%',
        'contoh_nilai': '54',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Nilai berkisar 10%–100%.'
    },
    {
        'nama_kolom': 'blue_light_filter_active',
        'deskripsi': 'Indikator aktif atau tidaknya fitur filter sinar biru pada perangkat.',
        'tipe_data': 'bool',
        'skala_pengukuran': 'Nominal',
        'satuan': '—',
        'contoh_nilai': '1',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Variabel biner (0 = Tidak Aktif, 1 = Aktif).'
    },
    {
        'nama_kolom': 'caffeine_post_5pm_mg',
        'deskripsi': 'Jumlah konsumsi kafein oleh responden setelah pukul 17:00 dalam miligram.',
        'tipe_data': 'int',
        'skala_pengukuran': 'Rasio',
        'satuan': 'mg',
        'contoh_nilai': '92',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Nilai berkisar 0–250 mg.'
    },
    {
        'nama_kolom': 'physical_activity_min',
        'deskripsi': 'Durasi aktivitas fisik atau olahraga harian responden dalam satuan menit.',
        'tipe_data': 'int',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Menit',
        'contoh_nilai': '21',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Nilai berkisar 0–112 menit.'
    },
    {
        'nama_kolom': 'sleep_latency_min',
        'deskripsi': 'Durasi waktu yang dibutuhkan responden untuk mulai tertidur dalam menit.',
        'tipe_data': 'float',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Menit',
        'contoh_nilai': '84.4',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Sleep onset latency (6.0–123.3 menit).'
    },
    {
        'nama_kolom': 'total_sleep_hours',
        'deskripsi': 'Total durasi tidur efektif responden per malam dalam satuan jam.',
        'tipe_data': 'float',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Jam',
        'contoh_nilai': '3.2',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Total durasi tidur (3.2–9.8 jam).'
    },
    {
        'nama_kolom': 'deep_sleep_pct',
        'deskripsi': 'Proporsi tahap tidur nyenyak (deep sleep) dari total durasi tidur dalam persentase.',
        'tipe_data': 'float',
        'skala_pengukuran': 'Rasio',
        'satuan': '%',
        'contoh_nilai': '23.5',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Fase tidur N3 (8.1%–28.0%).'
    },
    {
        'nama_kolom': 'rem_sleep_pct',
        'deskripsi': 'Proporsi tahap tidur bermimpi (REM sleep) dari total durasi tidur dalam persentase.',
        'tipe_data': 'float',
        'skala_pengukuran': 'Rasio',
        'satuan': '%',
        'contoh_nilai': '22.2',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Fase tidur REM (9.6%–27.0%).'
    },
]
    {
        'nama_kolom': 'morning_alarm_snoozes',
        'deskripsi': 'Frekuensi responden menekan tombol tunda (snooze) alaram pagi.',
        'tipe_data': 'int',
        'skala_pengukuran': 'Rasio',
        'satuan': 'Kali',
        'contoh_nilai': '7',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Bukan data pribadi',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Jumlah tunda alaram (0–7 kali).'
    },
    {
        'nama_kolom': 'next_day_fatigue_score',
        'deskripsi': 'Skor tingkat kelelahan yang dirasakan responden pada keesokan harinya.',
        'tipe_data': 'float',
        'skala_pengukuran': 'Ordinal',
        'satuan': 'Skor (1–10)',
        'contoh_nilai': '10.0',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': 'Skor persepsi kelelahan (1.0–10.0).'
    },
    {
        'nama_kolom': 'sleep_debt_category',
        'deskripsi': 'Klasifikasi tingkat keparahan akumulasi utang tidur (sleep debt).',
        'tipe_data': 'string',
        'skala_pengukuran': 'Ordinal',
        'satuan': '—',
        'contoh_nilai': 'Severe Sleep Debt',
        'nilai_kosong': 'Tidak ada (0%)',
        'sumber': 'bedtime_screentime_sleep_debt.csv',
        'kategori_data_pribadi': 'Data spesifik',
        'tindakan_penanganan': 'Pertahankan',
        'catatan': '4 kategori tingkat keparahan utang tidur.'
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

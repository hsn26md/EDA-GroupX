# Cleaning Log

Dataset: bedtime_screen_sleep_debt.csv  
Baris mentah: 8600 -> baris bersih: 8500  

| # | Langkah | Baris terdampak | Alasan |
|---|---|---|---|
| 1 | Ekstrak angka & placeholder -> NaN | 107.0 | Regex ambil angka dari teks bersatuan; N/A, -, NaN dijadikan missing |
| 2 | Buang spasi awal dan akhir kolom teks | 500.0 | Spasi tersembunyi memecah groupby dan melambungkan nunique |
| 3 | Seragamkan gender | 9.0 | Spasi/huruf/pemisah oleh kode; singkatan diputuskan manual di PETA_MANUAL |
| 4 | Seragamkan occupation_type | 10.0 | Spasi/huruf/pemisah oleh kode; singkatan diputuskan manual di PETA_MANUAL |
| 5 | Seragamkan chronotype | 5.0 | Spasi/huruf/pemisah oleh kode; singkatan diputuskan manual di PETA_MANUAL |
| 6 | Seragamkan primary_bedtime_app | 12.0 | Spasi/huruf/pemisah oleh kode; singkatan diputuskan manual di PETA_MANUAL |
| 7 | Seragamkan sleep_debt_category | 4.0 | Huruf dan spasi oleh kode; 4 salah ketik diputuskan manual lalu dicatat di peta |
| 8 | Seragamkan blue_light_filter_active | 6.0 | Yes/No/True/False/1/0 dipetakan ke 1/0 |
| 9 | Hapus duplikat persis | 100.0 | Seluruh kolom identik; satu baris disimpan |
| 10 | Buang baris tanpa user_id | 0.0 | Kunci utama kosong tidak dapat ditelusuri kembali ke sumber |
| 11 | Nilai di luar batas domain -> NaN | 30.0 | Aturan domain per kolom, bukan IQR |
| 12 | Imputasi occupation_type | 170.0 | Diisi label 'Unknown' |
| 13 | Imputasi chronotype | 127.0 | Diisi label 'Unknown' |
| 14 | Imputasi age | 8.0 | Median global |
| 15 | Imputasi screen_brightness_pct | 176.0 | Median global |
| 16 | Imputasi caffeine_post_5pm_mg | 174.0 | Median global |
| 17 | Imputasi total_sleep_hours | 8.0 | Median per sleep_debt_category |
| 18 | Imputasi sleep_latency_min | 259.0 | Median per sleep_debt_category |
| 19 | Imputasi deep_sleep_pct | 255.0 | Median per sleep_debt_category |
| 20 | Imputasi rem_sleep_pct | 60.0 | Median per sleep_debt_category |
| 21 | Konversi bedtime_phone_minutes ke numerik (buang satuan 'min') | 51.0 | Kolom bertipe teks karena sebagian nilai berformat '<angka> min'; diekstrak angkanya dengan regex dan diubah ke float agar bisa dihitung |
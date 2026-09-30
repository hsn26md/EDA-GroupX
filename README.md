# Proyek EDA: Analisis Kebiasaan Penggunaan Ponsel Sebelum Tidur & Sleep Debt

Proyek ini disusun untuk memenuhi tugas **Milestone M1** Mata Kuliah *Exploratory Data Analysis* (EDA).

## 👥 Anggota Kelompok
1. Ahmad Hussein Mufahir - Repository & Infrastructure Lead
2. Fikri El - Lead Data Analyst
3. Aliifah Husnul Khotimah - Data Architect
4. Zacky Alvansyah - Data Privacy & Security Engineer

---

## 📌 Provenansi Data (Data Provenance)
* **Nama Sumber**: Sleep Debt and Screen Time Dataset (oleh Samar Talwar)
* **Tautan / Instansi**: [Kaggle Dataset Link](https://www.kaggle.com/datasets/samartalwar/sleep-debt-and-screen-time-late-night-phone-habits)
* **Tanggal Pengambilan**: 30 September 2026
* **Lisensi / Izin**: CC0: Public Domain (Open Data)
* **Kalimat Sitasi**: *Talwar, S. (2024). Sleep Debt and Screen Time Dataset. Kaggle.*

---

## ❓ Pertanyaan Analisis
**Pertanyaan Payung:**
> Bagaimana kebiasaan penggunaan ponsel sebelum tidur (*bedtime phone habits*) berkaitan dengan durasi tidur dan tingkat *sleep debt* pengguna?

**Pertanyaan Turunan:**
1. Bagaimana perbedaan rata-rata `bedtime_phone_minutes` pada setiap kelompok `sleep_debt_category`? (Kolom: `bedtime_phone_minutes`, `sleep_debt_category`)
2. Kelompok `occupation_type` mana yang memiliki rata-rata `bedtime_phone_minutes` tertinggi dan `total_sleep_hours` terendah? (Kolom: `occupation_type`, `bedtime_phone_minutes`, `total_sleep_hours`)
3. Kategori `primary_bedtime_app` apa yang paling berkaitan dengan tingginya `bedtime_phone_minutes` sebelum tidur? (Kolom: `primary_bedtime_app`, `bedtime_phone_minutes`)

# Students’ Performance Dataset

Dataset ini berisi data mahasiswa dari sebuah institusi pendidikan tinggi yang mencakup informasi saat pendaftaran serta performa akademik pada semester pertama dan kedua. Dataset digunakan untuk membangun model klasifikasi guna memprediksi **dropout**, **enrolled**, atau **graduate** pada akhir masa studi normal.

---

## Gambaran Umum

* **Sumber**: UCI Machine Learning Repository
* **Tugas**: Multiclass classification (3 kelas)
* **Target**: `Status` / `Target`
* **Tidak ada missing values**
* Data mencakup:

  * Jalur akademik sebelumnya
  * Faktor demografis
  * Faktor sosial-ekonomi
  * Performa akademik semester 1 & 2
  * Indikator ekonomi makro

---

## Penjelasan Variabel

### 1. Informasi Demografis & Latar Belakang

| Variabel            | Tipe    | Deskripsi Singkat             |
| ------------------- | ------- | ----------------------------- |
| `Marital_status`    | Integer | Status pernikahan mahasiswa   |
| `Gender`            | Integer | 1 = male, 0 = female          |
| `Age_at_enrollment` | Integer | Usia saat masuk               |
| `Nacionality`       | Integer | Kode kewarganegaraan          |
| `International`     | Integer | Mahasiswa internasional (1/0) |

---

### 2. Jalur Masuk & Pendidikan Sebelumnya

| Variabel                       | Tipe       | Deskripsi                           |
| ------------------------------ | ---------- | ----------------------------------- |
| `Application_mode`             | Integer    | Jalur pendaftaran                   |
| `Application_order`            | Integer    | Urutan pilihan program (0–9)        |
| `Course`                       | Integer    | Kode program studi                  |
| `Daytime_evening_attendance`   | Integer    | 1 = siang, 0 = malam                |
| `Previous_qualification`       | Integer    | Pendidikan terakhir                 |
| `Previous_qualification_grade` | Continuous | Nilai pendidikan sebelumnya (0–200) |
| `Admission_grade`              | Continuous | Nilai saat masuk (0–200)            |

---

### 3. Latar Belakang Keluarga

| Variabel                | Tipe    | Deskripsi       |
| ----------------------- | ------- | --------------- |
| `Mothers_qualification` | Integer | Pendidikan ibu  |
| `Fathers_qualification` | Integer | Pendidikan ayah |
| `Mothers_occupation`    | Integer | Pekerjaan ibu   |
| `Fathers_occupation`    | Integer | Pekerjaan ayah  |

---

### 4. Faktor Sosial & Keuangan

| Variabel                    | Tipe    | Deskripsi          |
| --------------------------- | ------- | ------------------ |
| `Displaced`                 | Integer | Mahasiswa perantau |
| `Educational_special_needs` | Integer | Kebutuhan khusus   |
| `Debtor`                    | Integer | Memiliki tunggakan |
| `Tuition_fees_up_to_date`   | Integer | Pembayaran lancar  |
| `Scholarship_holder`        | Integer | Penerima beasiswa  |

---

### 5. Performa Akademik – Semester 1

| Variabel                                       | Deskripsi              |
| ---------------------------------------------- | ---------------------- |
| `Curricular_units_1st_sem_credited`            | SKS dikreditkan        |
| `Curricular_units_1st_sem_enrolled`            | SKS diambil            |
| `Curricular_units_1st_sem_evaluations`         | Jumlah evaluasi        |
| `Curricular_units_1st_sem_approved`            | SKS lulus              |
| `Curricular_units_1st_sem_grade`               | Rata-rata nilai (0–20) |
| `Curricular_units_1st_sem_without_evaluations` | Tanpa evaluasi         |

---

### 6. Performa Akademik – Semester 2

| Variabel                                       | Deskripsi              |
| ---------------------------------------------- | ---------------------- |
| `Curricular_units_2nd_sem_credited`            | SKS dikreditkan        |
| `Curricular_units_2nd_sem_enrolled`            | SKS diambil            |
| `Curricular_units_2nd_sem_evaluations`         | Jumlah evaluasi        |
| `Curricular_units_2nd_sem_approved`            | SKS lulus              |
| `Curricular_units_2nd_sem_grade`               | Rata-rata nilai (0–20) |
| `Curricular_units_2nd_sem_without_evaluations` | Tanpa evaluasi         |

---

### 7. Indikator Ekonomi Makro

| Variabel            | Tipe       | Deskripsi                |
| ------------------- | ---------- | ------------------------ |
| `Unemployment_rate` | Continuous | Tingkat pengangguran (%) |
| `Inflation_rate`    | Continuous | Tingkat inflasi (%)      |
| `GDP`               | Continuous | Produk Domestik Bruto    |

---

### 8. Target Variable

| Variabel            | Tipe        | Kelas                             |
| ------------------- | ----------- | --------------------------------- |
| `Status` / `Target` | Categorical | `Dropout`, `Enrolled`, `Graduate` |

---

## Struktur Problem

* **Jenis problem**: Multiclass classification
* **Tujuan utama**:

  * Identifikasi risiko dropout lebih awal
  * Analisis faktor penentu keberhasilan akademik
  * Membantu pengambilan kebijakan akademik

---

## Referensi

Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021).
*Predict students' dropout and academic success.*
UCI Machine Learning Repository.
[https://doi.org/10.24432/C5MC89](https://doi.org/10.24432/C5MC89)

---

Jika diperlukan, saya bisa bantu:

* Membuat versi README untuk GitHub (format markdown production-ready)
* Menyederhanakan untuk laporan
* Menambahkan section EDA atau data dictionary yang lebih formal
* Membuat versi dokumentasi teknis untuk tim data science

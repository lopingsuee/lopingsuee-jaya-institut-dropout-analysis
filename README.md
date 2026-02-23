# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

# Jaya Institut — Student Dropout Early Warning System

---

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang menghadapi tantangan tingginya angka mahasiswa dropout. Tingginya angka dropout berdampak pada reputasi institusi, stabilitas finansial, dan kualitas akademik.

Proyek ini bertujuan membangun:

* Sistem Early Warning berbasis Machine Learning
* Dashboard monitoring berbasis Metabase
* Prototype prediksi risiko dropout menggunakan Streamlit

---

## Permasalahan Bisnis

1. Tingginya angka dropout mahasiswa.
2. Tidak adanya sistem deteksi dini berbasis data.
3. Sulitnya mengidentifikasi faktor penyebab dropout.
4. Kurangnya monitoring performa akademik dan finansial mahasiswa.

---

## Cakupan Proyek

1. Exploratory Data Analysis (EDA)
2. Identifikasi faktor risiko dropout
3. Data preprocessing dan feature engineering
4. Pembangunan model machine learning
5. Evaluasi model
6. Pengembangan prototype Streamlit
7. Pembuatan business dashboard Metabase
8. Rekomendasi strategis berbasis data

---

# Persiapan

## 1. Clone Repository

```
git clone <repository-url>
cd <repository-folder>
```

---

## 2. Membuat dan Mengaktifkan Virtual Environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### MacOS / Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Dataset

Sumber data:

[https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Dataset memiliki:

* 4.424 baris
* 37 kolom
* Tidak ada missing value

Target awal:

* Dropout
* Graduate
* Enrolled

Target ditransformasikan menjadi biner:

* 1 = Dropout
* 0 = Non-Dropout

---

# Business Dashboard (Metabase)

Dashboard dibuat untuk membantu manajemen memahami:

* Distribusi status mahasiswa
* Dropout rate per program studi
* Pengaruh faktor finansial
* Performa semester 1
* Hubungan scholarship dan dropout
* Monitoring kelulusan mata kuliah

---

## Cara Menjalankan Metabase

Pastikan file berikut tersedia di root directory:

```
metabase.db.mv.db
```

### Menjalankan Metabase dengan Docker

```
docker run -d -p 3000:3000 --name metabase \
-v $(pwd)/metabase.db.mv.db:/metabase.db.mv.db \
metabase/metabase
```

Jika database sudah ada di container, export dengan:

```
docker cp metabase:/metabase.db/metabase.db.mv.db ./
```

---

## Mengakses Dashboard

1. Buka browser
2. Akses:

```
http://localhost:3000
```

---

## Kredensial Akun Metabase

email: [root@mail.com](mailto:root@mail.com)
password: root123

---

Jika dashboard telah dipublish publik (opsional), tautan dapat ditambahkan di sini.

---

# Menjalankan Sistem Machine Learning

Model yang digunakan:

Logistic Regression dengan `class_weight="balanced"`

Performa model:

* ROC-AUC: ± 0.89
* Recall Dropout: ± 0.80
* Accuracy: ± 0.84

Fokus evaluasi pada recall kelas Dropout karena false negative lebih berisiko dalam konteks bisnis.

---

## Menjalankan Prototype Secara Lokal

Pastikan model tersedia:

```
model/model_fix.joblib
```

Jalankan:

```
streamlit run app.py
```

Aplikasi akan berjalan di:

```
http://localhost:8501
```

---

## Prototype Online

[https://lopingsuee-jaya-institut-dropout-analysis-xgf36hcgcjcmkerd9ody.streamlit.app/](https://lopingsuee-jaya-institut-dropout-analysis-xgf36hcgcjcmkerd9ody.streamlit.app/)

Prototype menerima input:

* Data demografi
* Data admission
* Status finansial
* Performa semester 1
* Data makro ekonomi

Output:

* Probabilitas dropout
* Prediksi High Risk / Low Risk
* Threshold yang dapat disesuaikan

---

# Conclusion

1. Faktor finansial adalah indikator paling kuat risiko dropout.
2. Performa semester pertama merupakan prediktor akademik paling signifikan.
3. Mahasiswa dengan approval rate rendah memiliki risiko tinggi.
4. Logistic Regression memberikan performa stabil dengan ROC-AUC mendekati 0.9.

Sistem ini layak digunakan sebagai alat early warning berbasis data.

---

# Rekomendasi Action Items

* Implementasi monitoring otomatis mahasiswa baru
* Intervensi akademik pada semester pertama
* Program bantuan finansial untuk mahasiswa debtor
* Mentoring khusus mahasiswa berisiko
* Integrasi sistem ke sistem akademik internal
* Evaluasi model secara berkala setiap semester


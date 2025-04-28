# 🌟 Happiness Score Prediction API

Sebuah mini-proyek berbasis **FastAPI** yang dapat memprediksi **Happiness Score** berdasarkan input fitur tertentu.

## 📁 Struktur File

```
├── app.py               # Endpoint API utama
├── XGBoost_Model.pkl    # File model Machine Learning yang telah dilatih
```

## 🚀 Fitur API

- Prediksi skor kebahagiaan berdasarkan 7 fitur utama
- Menerima input melalui metode POST
- Hasil prediksi berupa skor kebahagiaan dalam bentuk angka desimal
- Ringan, cepat, dan siap diintegrasikan ke aplikasi lain

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/username/happiness-score-api.git
cd happiness-score-api
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
uvicorn app:app --reload
```

### 5. Akses Swagger UI

Buka browser ke:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "GDP_per_capita": 1.2,
  "Social_support": 0.8,
  "Healthy_life_expectancy": 0.9,
  "Freedom_to_make_life_choices": 0.7,
  "Generosity": 0.3,
  "Perceptions_of_corruption": 0.2,
  "GDP_per_Score": 1.1
}
```

## ✅ Contoh Output

```json
{
  "predicted_score": 7.543
}
```

> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.

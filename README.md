

<div align="center">

# 🚚 EmptyLegs

### AI-Powered Empty-Leg Logistics Optimization

**Reducing deadhead miles · Cutting CO₂ · Using existing infrastructure**

<br/>

[![Status](https://img.shields.io/badge/status-prototype-success)]()
[![Tech](https://img.shields.io/badge/AI-ML%20%7C%20Geospatial-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

</div>

---

## 🌍 Why EmptyLegs?

> **30% of trucks drive empty.**
> EmptyLegs turns those wasted miles into **low-cost, low-carbon logistics capacity**.

Instead of adding new vehicles, EmptyLegs unlocks unused capacity already on the road by intelligently matching **empty truck routes** with **nearby shipment requests**.

---

## ✨ What Makes It Different

| Feature               | EmptyLegs |
| --------------------- | --------- |
| Uses existing trucks  | ✅         |
| Real route geometry   | ✅         |
| ML-based ranking      | ✅         |
| Address-based input   | ✅         |
| CO₂ impact tracking   | ✅         |
| No new infrastructure | ✅         |

---

## 🧠 How It Works (High Level)

```
Driver Route
    ↓
Shipment Request
    ↓
Route & Detour Analysis
    ↓
Capacity + Time Validation
    ↓
ML-Based Scoring
    ↓
Ranked Matches
    ↓
Accept → CO₂ Saved
```

---

## 📐 System Architecture

```
┌──────────────────┐
│  React Frontend  │
│  (Vite + Leaflet)│
└────────┬─────────┘
         │ REST
┌────────▼─────────┐
│  FastAPI Backend │
│  - Matching Logic│
│  - Metrics       │
└────────┬─────────┘
         │
┌────────▼─────────┐
│ ML Engine        │
│ (PyTorch)        │
│ Route Embeddings │
└──────────────────┘

Maps: OpenStreetMap  
ML Target: Google Vertex AI
```

---

## ⚙️ Tech Stack

### Frontend

* React (Vite)
* Leaflet + OpenStreetMap
* Axios

### Backend

* FastAPI
* SQLite + SQLAlchemy
* PyTorch (ML scoring engine)

### Google Technologies Used

* **Google Vertex AI** – ML training & deployment target
* **Google Maps Platform** – initial routing & geospatial reference
* **Google Cloud Run** – backend deployment target
* **Google Firebase** – authentication & realtime updates (planned)
* **Google BigQuery** – emissions & logistics analytics (planned)

> Prototype uses OpenStreetMap for free geocoding but is architected for Google Maps.

---

## 🚀 Key Features

* 📍 **Address-based input** (no coordinates required)
* 🧠 **ML-assisted match scoring**
* ⚖️ **Weight & capacity validation**
* ♻️ **Live CO₂ savings metrics**
* ⚡ **Real-time match acceptance**
* 🔒 **Single-accept, route-locking logic**

---

## 🔌 API Snapshot

**Register Driver**

```http
POST /drivers/register
```

**Create Shipment**

```http
POST /shipments/create
```

**Fetch Matches**

```http
GET /matches
```

**Accept Match**

```http
POST /matches/{match_id}/accept
```

**Metrics**

```http
GET /metrics
```

---

## 🧪 Run Locally

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

📍 `http://localhost:8000/docs`

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

📍 `http://localhost:5173`

---

## 📊 Sustainability Impact

* Fewer empty miles
* Lower fuel consumption
* Reduced CO₂ per shipment
* Better fleet utilization

**Impact is calculated and displayed in real time.**

---

## 🏆 Why This Should Win In This Hackathon

* Real problem, measurable impact
* Uses AI meaningfully (not decorative)
* Works end-to-end
* Scales without new infrastructure
* Clean separation of concerns
* Cloud-ready architecture

---

## 📌 Status

✅ Functional prototype
✅ End-to-end flow
✅ Demo-ready
🔜 Cloud deployment & tuning

---

## 📄 License

MIT

---



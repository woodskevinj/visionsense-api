---
# 🖼️ Vision Sense API

End-to-end deep learning project for image classification — built and deployed using
PyTorch and FastAPI.

This project demonstrates the full applied ML lifecycle from data exploration and
transfer learning to model serving and containerized deployment on AWS.
---

## 🧩 Project Overview

Deploy a containerized API that accepts an image file (`POST /predict`), runs it through a pre-trained deep learning model, and returns the predicted label and confidence score.

---

## ⚙️ Tech Stack

| Component            | Purpose                                  |
| -------------------- | ---------------------------------------- |
| **Framework**        | FastAPI                                  |
| **Model**            | TorchVision ResNet-50 (ImageNet weights) |
| **Image Handling**   | Pillow                                   |
| **Serving**          | Uvicorn                                  |
| **Containerization** | Docker (multi-stage build)               |
| **Optional**         | AWS ECS / App Runner deployment later    |

---

## 📂 Project Structure

```css
visionsense-api/
├── app.py
├── src/
│   ├── __init__.py
│   └── classifier.py
├── requirements.txt
├── README.md
├── Dockerfile
├── .dockerignore
└── .gitignore

```

---

## 🚀 Getting Started

````bash
# 1️⃣ Clone the repository
```bash
git clone https://github.com/woodskevinj/visionsense-api.git
cd visionsense-api
````

# 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

# 3️⃣ Run the FastAPI app

```bash
uvicorn api.app:app --reload
```

# 4️⃣ Test the /predict endpoint

````

Send an image file for inference:

```bash
curl -X POST -F "file=@test.jpg" http://127.0.0.1:8000/predict
````

Expected JSON response:

```json
{
  "top1_prediction": { "label": "cat", "confidence": 0.8723 },
  "top3_predictions": [
    { "label": "cat", "confidence": 0.8723 },
    { "label": "dog", "confidence": 0.0671 },
    { "label": "deer", "confidence": 0.0339 }
  ]
}
```

---

## 🧠 Learning Focus

This project highlights core concepts required of an Applied ML Engineer:

- 🧩 Convolutional Neural Networks (CNNs) — for visual pattern extraction

- 🔁 Transfer Learning — adapting pretrained ResNet18 to CIFAR-10

- 📈 Model Evaluation — training/validation loss tracking

- ⚙️ Model Serving — running inference via FastAPI

- 🐳 Containerization — reproducible, portable environments for deployment

- ☁️ AWS Integration (Optional) — deploying via ECS with Docker and ECR

---

## 🌐 API Endpoints

| Endpoint | Method | Description                                                              |
| -------- | ------ | ------------------------------------------------------------------------ |
| /predict | POST   | Upload an image for classification (returns top-1 and top-3 predictions) |
| /logs    | GET    | Retrieve recent prediction logs (?limit=10)                              |
| /health  | GET    | Quick system health and model readiness check                            |
| /info    | GET    | View model metadata (architecture, parameters, size, etc.)               |
| /        | GET    | Welcome message and API overview                                         |

---

## 🐳 Docker Usage

Build Docker Image

```bash
docker build -t visionsense-api .
```

Run Container

```bash
docker run -p 8000:8000 visionsense-api
```

- Verify it’s running:

```bash
docker ps
```

```nginx
CONTAINER ID   IMAGE              COMMAND                  STATUS         PORTS                    NAMES
xxxxxx         visionsense-api   "uvicorn app:app --h…"   Up 5 seconds   0.0.0.0:8000->8000/tcp   visionsense

```

### 🌐 Test the API

```arduino
http://127.0.0.1:8000/health
http://127.0.0.1:8000/logs
```

You should see:

```json
{
  "status": "healthy",
  "model_loaded": true,
  "device": "cpu",
  "message": "API and model are ready for inference."
}
```

---

## 🧱 Docker Ignore Setup

.dockerignore ensures that unnecessary local files (data, logs, checkpoints, etc.) are excluded from Docker builds for a small and efficient image.

Example included in repo:

```bash
data/
logs/
notebooks/.ipynb_checkpoints/
venv/
.git/
```

---

## 📊 Current Progress

| Phase                                | Description                               | Status  |
| ------------------------------------ | ----------------------------------------- | ------- |
| **Data Exploration & Preprocessing** | CIFAR-10 dataset setup and visualization  | 🔜 Next |
| **Model Training (ResNet18)**        | Fine-tuning pretrained CNNon CIFAR-10     | 🔜 Next |
| **API Development**                  | FastAPI app + model inference integration | 🔜 Next |
| **Logging & Health Monitoring**      | Logs, /health, /info endpoints added      | 🔜 Next |
| **Containerization (Docker)**        | Docker build + run configuration          | 🔜 Next |
| **Cloud Deployment (AWS ECS)**       | Push image to ECR and deploy              | 🔜 Next |

---

## 📅 Roadmap

- [ ] Complete EDA and preprocessing

- [ ] Train and save fine-tuned ResNet18 model

- [ ] Integrate inference into FastAPI /predict route

- [ ] Add logging, /logs, /health, and /info endpoints

- [ ] Containerize with Docker

- [ ] Deploy to AWS ECS

---

## ☁️ Deployment Status

- ✅ Dockerized successfully using a multi-stage build (~1 GB final image)
- ⚙️ AWS ECR upload attempted — image too large for current bandwidth limits
- 🧩 Next iteration: optimize dependency footprint (use `torch-cpu`, lighter base image)
- 🚀 ECS deployment workflow will follow in the next phase

---

## 💡 Developer Note

- TBD

---

👨‍💻 Author

- Kevin Woods
- Applied ML Engineer | AWS Certified AI Practitioner | AWS Machine Learning Certified Engineer – Associate
- 🔗 GitHub: woodskevinj

---
# 🖼️ Vision Sense API

End-to-end deep learning project for image classification — built and deployed using
PyTorch and FastAPI.

This project demonstrates the full applied ML lifecycle from data exploration and
transfer learning to model serving and containerized deployment on AWS.
---

## 🧩 Project Overview

VisionSense API provides a containerized image-classification microservice.
It accepts an image file (`POST /predict`), runs it through a pretrained ResNet-18 (ImageNet weights), and returns the top-5 predicted labels and confidence scores.

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
  "success": true,
  "results": [
    { "label": "golden retriever", "confidence": 0.9853 },
    { "label": "Labrador retriever", "confidence": 0.0094 },
    { "label": "cocker spaniel", "confidence": 0.0021 },
    { "label": "kuvasz", "confidence": 0.0013 },
    { "label": "flat-coated retriever", "confidence": 0.0011 }
  ]
}
```

---

## 🧠 Learning Focus

This project highlights core concepts required of an Applied ML Engineer:

- 🧩 Convolutional Neural Networks (CNNs) — visual feature extraction

- 🔁 Transfer Learning — using pretrained ImageNet models

- ⚙️ Model Serving — building a real-time inference API

- 🐳 Containerization — reproducible, portable environments

- ☁️ AWS Integration (optional) — ECS/ECR deployment workflow

---

## 🌐 API Endpoints

| Endpoint | Method | Description                                                              |
| -------- | ------ | ------------------------------------------------------------------------ |
| /predict | POST   | Upload an image for classification (returns top-1 and top-3 predictions) |
| /logs    | GET    | Retrieve recent prediction logs (?limit=10)                              |
| /health  | GET    | Quick system health and model readiness check                            |
| /info    | GET    | View model metadata (architecture, parameters, size, etc.)               |
| /        | GET    | Welcome message and API overview                                         |

Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc

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

Verify

```bash
docker ps
```

- Example

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
__pycache__/
```

---

## 📊 Current Progress

| Phase                           | Description                                             | Status       |
| ------------------------------- | ------------------------------------------------------- | ------------ |
| **Base Model Setup**            | ResNet-18 pretrained ImageNet model loaded successfully | ✅ Completed |
| **FastAPI Inference API**       | `/predict` endpoint serving live predictions            | ✅ Completed |
| **Logging & Health Monitoring** | Logs, /health, /info endpoints added                    | 🔜 Next      |
| **Docker Containerization**     | Local container build and test                          | 🔜 Next      |
| **Fine-Tuning Pipeline**        | Adapt ResNet-18 for CIFAR-10 / custom dataset           | 🔜 Next      |
| **AWS Deployment**              | Push image to ECR and deploy on ECS                     | 🔜 Upcoming  |

---

## 🔁 Transfer Learning (Fine-Tuning)

The next milestone introduces **fine-tuning**, where we adapt the pretrained ResNet-18 to a smaller custom dataset (e.g., **CIFAR-10**).

This involves:

1. Replacing the final classification layer (fc) with a new one for custom labels.

2. Training on the new dataset while keeping earlier convolutional layers frozen or partially trainable.

3. Saving and serving the fine-tuned model through this same API.

---

## 📅 Roadmap

- [x] Implement pretrained ResNet-18 inference API

- [ ] Containerize with Docker

- [ ] Fine-tune on CIFAR-10

- [ ] Save and load fine-tuned model for inference

- [ ] Add logging, /logs, /health, and /info endpoints

- [ ] Deploy to AWS ECS

---

## ☁️ Deployment Status

- ✅ Docker image builds successfully (~1 GB)

- 🧩 ECR/ECS deployment planned

- ⚙️ Next optimization: use torch-cpu and lighter base image for faster upload

---

## 💡 Developer Note

- TBD

---

👨‍💻 Author

- Kevin Woods
- Applied ML Engineer | AWS Certified AI Practitioner | AWS Machine Learning Certified Engineer – Associate
- 🔗 GitHub: woodskevinj

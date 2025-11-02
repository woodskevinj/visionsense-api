from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from src.classifier import VisionClassifier
import shutil
import tempfile
import os

app = FastAPI(
    title="VisionSense API",
    description="Image classification API using a pretrained ResNet model",
    version="1.0.0",
)

# Initialize classifier once at startup
classifier = VisionClassifier()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Receives an image file and returns top-5 predicted labels + confidences.
    """

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_path = temp_file.name

        # ✅ Now returns top-5 list instead of single dict
        results = classifier.predict(temp_path, top_k=5)
        os.remove(temp_path)

        return JSONResponse(content={"success": True, "result": results})
    
    except Exception as e:
        return JSONResponse(
            content={"success": False, "error": str(e)}, status_code=500
        )
    
@app.get("/")
def root():
    return {"message": "Welcome to VisionSense API!  Use POST /predict to classify images."}


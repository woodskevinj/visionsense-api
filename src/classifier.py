import torch
from torchvision.models import resnet18, ResNet18_Weights
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json
import os

class VisionClassifier:
    def __init__(self, labels_path: str = None, device: str = None):
        """
        Initialize classifier with modern weights and label mapping.
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        # ✅ Use the modern TorchVision weights interface
        self.weights = ResNet18_Weights.DEFAULT
        self.model = resnet18(weights=self.weights)
        self.model.eval()
        self.model.to(self.device)

        # Load labels (prefer local, fallback to default)
        if labels_path and os.path.exists(labels_path):
            with open(labels_path, "r") as f:
                self.labels = json.load(f)

        else:
            # Use labels that come bundled with the weights metadata
            self.labels = self.weights.meta["categories"]

        # ✅ Built-in transform pipeline from weights (exact preprocessing)
        self.transform = self.weights.transforms()

    def predict(self, image_path: str, top_k: int = 5):
        """
        Run image classification and return top prediction
        """
        image = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

        # Get top-K predictions
        top_probs, top_classes = torch.topk(probabilities, top_k)
        results = [
            {
                "label": self.labels[idx.item()],
                "confidence": round(prob.item(), 4)
            }
            for prob, idx in zip(top_probs, top_classes)
        ]
        return results
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json
import os

class VisionClassifier:
    def __init__(self, labels_path: str = None, device: str = None):
        """
        Initialize classifier with pretrained model and label mapping.
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = models.resnet18(pretrained=True)
        self.model.eval()
        self.model.to(self.device)

        # Load ImageNet Class labels
        if labels_path and os.path.exists(labels_path):
            with open(labels_path, "r") as f:
                self.labels = json.load(f)

        else:
            # default labels (from torchvision)
            labels_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
            import urllib.request
            response = urllib.request.urlopen(labels_url)
            self.labels = [line.strip() for line in response.readlines()]

        # Define transform pipeline
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def predict(self, image_path: str):
        """
        Run image classification and return top prediction
        """
        image = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

        # Get top prediction
        top_prob, top_class = torch.max(probabilities, dim=0)
        predicted_label = self.labels[top_class.item()]
        return {
            "label": predicted_label,
            "confidence": round(top_prob.item(), 4)
        }
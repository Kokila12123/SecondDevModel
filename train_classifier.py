import os
from ultralytics import YOLO

def train_road_classifier():
    data_dir = "C:/Users/yashw/.gemini/antigravity/scratch/trash_detection/road_data_split"
    
    # Verify data split exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Split directory {data_dir} does not exist. Run prepare_data.py first.")
        
    print("Loading pre-trained YOLOv8-nano classification model...")
    # Using yolov8n-cls.pt (nano classifier)
    model = YOLO("yolov8n-cls.pt")
    
    print("Starting training of road classifier...")
    # Train the model on the GPU
    results = model.train(
        data=data_dir,
        epochs=30,          # 30 epochs is enough for fine-tuning on 100 images
        imgsz=224,          # standard YOLO image classification size
        batch=16,           # small batch size to fit memory and handle small data
        device=0,           # use GPU (GeForce RTX 4060)
        project="road_trash_project",
        name="road_classifier",
        plots=True
    )
    print("Road classifier training completed successfully!")
    print(f"Results saved in: {results.save_dir}")

if __name__ == "__main__":
    train_road_classifier()

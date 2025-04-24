from ultralytics import YOLO

def train():

    model = YOLO('pothole_yolov8.pt')

    model.train(
        data=r'C:\Users\dixon\Desktop\ITS365\waldo-dataset-a\waldo-dataset-a\data.yaml',
        epochs=50,
        imgsz=640
    )

    results = model.val()

    model.save('pothole3yolov8.pt')

if __name__ == "__main__":
    train()
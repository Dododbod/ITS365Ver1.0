from ultralytics import YOLO
import os

def run_inference():
    # Load your trained model
    model = YOLO(r'pothole_yolov8.pt')

    # Path to test images
    test_images_path = r'C:\Users\dixon\Desktop\ITS365\waldo-dataset-b\test\images'

    # Run inference
    results = model(test_images_path)

    # Loop through results and show/save them
    for i, result in enumerate(results[3:13]):
        result.show()  # visualize result
        result.save(filename=f'result_{i}.jpg')  # optional: save output to file
        print(f"Image {i+1}: Detected {len(result.boxes)} object(s)")

if __name__ == "__main__":
    run_inference()

import os
import zipfile
from pathlib import Path
import cv2
import torch
from matplotlib import pyplot as plt
from ultralytics import YOLO
from IPython.display import Image, display

# 1️⃣ Confusion Matrix: Load and Display
confusion_matrix_path = r'runs\detect\val\confusion_matrix.png'  # Update this if needed

if os.path.exists(confusion_matrix_path):
    display(Image(filename=confusion_matrix_path))
else:
    print("Confusion matrix image not found!")

# 2️⃣ Precision-Recall-F1 Curve: Load and Display
pr_curve_path = r'runs\detect\val\pr_curve.png'  # Update this if needed

if os.path.exists(pr_curve_path):
    display(Image(filename=pr_curve_path))
else:
    print("Precision-Recall curve image not found!")

# 3️⃣ GitHub Dataset Download - Windows Compatible (no !wget)
import urllib.request

DEV_NAME = "Dododbod"      # Replace this
REPO_NAME = "ITS365MLProject"          # Replace this

url = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-test.zip'
output_file = 'waldo-dataset-test.zip'

try:
    urllib.request.urlretrieve(url, output_file)
    print("✅ Download complete.")
except Exception as e:
    print(f"❌ Error downloading: {e}")

# 4️⃣ Unzip the dataset
zip_path = 'waldo-dataset-test.zip'
extract_path = 'test_data'

if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("✅ Dataset extracted.")
else:
    print("❌ Zip file not found!")

# 5️⃣ Load your trained YOLO model
model = YOLO(r'runs\train\waldo_run\weights\best.pt')  # Update path if needed

# 6️⃣ Path to test images
test_images_dir = Path(extract_path) / 'images'  # assuming structure /images inside the zip

# 7️⃣ Initialize counter
total_waldo_faces = 0

# 8️⃣ Loop through the test images
for img_path in test_images_dir.glob('*.jpg'):
    print(f"\nProcessing {img_path.name}... 🕵️‍♂️")

    # Read and convert the image
    img = cv2.imread(str(img_path))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Run inference
    results = model(img_rgb)
    pred = results[0]
    boxes = pred.boxes.xywh
    class_ids = pred.boxes.cls
    names = model.names  # use model.names instead of pred.names

    # Detect 'waldorotation' or 'wendarotation'
    waldo_faces = []
    for i, box in enumerate(boxes):
        label_idx = int(class_ids[i].item())
        label_name = names[label_idx]
        if label_name in ['waldorotation', 'wendarotation']:
            waldo_faces.append(box)

    # Count
    waldo_count = len(waldo_faces)
    total_waldo_faces += waldo_count

    # Draw bounding boxes
    for box in waldo_faces:
        x, y, w, h = box
        x1, y1, x2, y2 = int(x - w/2), int(y - h/2), int(x + w/2), int(y + h/2)
        cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show image with results
    plt.figure(figsize=(8, 8))
    plt.imshow(img_rgb)
    plt.title(f"{img_path.name} - Found {waldo_count} Waldo Face{'s' if waldo_count != 1 else ''} 😎")
    plt.axis('off')
    plt.show()

# 9️⃣ Summary
print(f"\n🎉🎉🎉 Total Waldo Faces Found: {total_waldo_faces} 😎")
print("🏆 The winner will be the student who finds the most Waldo faces!")
import os
import torch
import shutil
import zipfile
import zipfile
import matplotlib.pyplot as plt
import cv2
import requests
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import locale
locale.getpreferredencoding = lambda: "UTF-8"
from ultralytics import YOLO

print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
# Check if CUDA (GPU support) is available for PyTorch and print the result (True/False).
print(torch.cuda.is_available())
# Print the number of CUDA-compatible devices (GPUs) available on the system.
print(torch.cuda.device_count())

# Print the name of the first CUDA-compatible device (GPU) available (index 0).
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
else:
    print("No CUDA device available.")
# Importing the PyTorch library, which provides tools for machine learning and deep learning.
# Write your code here
# Importing the YOLO (You Only Look Once) model from the 'ultralytics' package for object detection tasks.
# Write your code here
# # # Optional Dataset (Type: A)

# # Define the global variables for the developer name and repository name
# DEV_NAME = 'kaopanboonyuen'
# REPO_NAME = 'where-is-waldo'

# # Use f-string to create the dynamic URL for the dataset
# url = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-a.zip'

# # Download the zip file using wget
# # !wget https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-a.zip -O waldo-dataset-a.zip
# !wget {url} -O waldo-dataset-a.zip

# # Unzip the downloaded file
# # !unzip /content/waldo-dataset-a.zip >> logs.log
# !unzip /content/waldo-dataset-a.zip >> logs.log

url = 'https://github.com/kaopanboonyuen/where-is-waldo/raw/main/dataset/waldo-dataset-a.zip'
r = requests.get(url)

with open("waldo-dataset-a.zip", "wb") as f:
    f.write(r.content)
    
with zipfile.ZipFile("waldo-dataset-a.zip", "r") as zip_ref:
    zip_ref.extractall("waldo-dataset-a")
    
# Define the global variables for the repository name
DEV_NAME = 'kaopanboonyuen'  # Replace with your developer name
REPO_NAME = 'where-is-waldo'  # Replace with your repository name

# Use f-string to create the dynamic URLs
url_part1 = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-b.zip.part1'
url_part2 = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-b.zip.part2'
url_part3 = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-b.zip.part3'
url_part4 = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-b.zip.part4'
url_part5 = f'https://github.com/{DEV_NAME}/{REPO_NAME}/raw/main/dataset/waldo-dataset-b.zip.part5'

# Function to download a part and save it to the file system
def download_part(url, filename):
    print(f"Downloading {filename}...")
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"Downloaded {filename} successfully.")

# Download each part
download_part(url_part1, "waldo-dataset-b.zip.part1")
download_part(url_part2, "waldo-dataset-b.zip.part2")
download_part(url_part3, "waldo-dataset-b.zip.part3")
download_part(url_part4, "waldo-dataset-b.zip.part4")
download_part(url_part5, "waldo-dataset-b.zip.part5")

print("All parts downloaded successfully!")

def reassemble_zip(parts, output_file):
    with open(output_file, 'wb') as output_zip:
        for part in parts:
            with open(part, 'rb') as part_file:
                output_zip.write(part_file.read())
    print(f"Reassembled to {output_file}.")

parts = ['waldo-dataset-b.zip.part1', 'waldo-dataset-b.zip.part2',
         'waldo-dataset-b.zip.part3', 'waldo-dataset-b.zip.part4', 'waldo-dataset-b.zip.part5']  # List of split parts
output_file = 'waldo-dataset-b.zip' 


with zipfile.ZipFile('waldo-dataset-b.zip', 'r') as zip_ref:
    zip_ref.extractall('waldo-dataset-b')  # Choose the extraction path
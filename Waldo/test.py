import os
import shutil

# Use raw strings (r"...") or double backslashes for Windows paths
base_dir = r'C:\Users\dixon\Desktop\ITS365\waldo-dataset-a'  # Change this to where you want the dataset

# Create directories
os.makedirs(os.path.join(base_dir, 'train', 'images'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'train', 'labels'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'valid', 'images'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'valid', 'labels'), exist_ok=True)

# Source directory where you unzipped waldo-dataset-b
source_dir = r'C:\Users\dixon\Desktop\ITS365\waldo-dataset-b'  # Change this too

# Move folders
shutil.move(os.path.join(source_dir, 'train', 'images'), os.path.join(base_dir, 'train', 'images'))
shutil.move(os.path.join(source_dir, 'train', 'labels'), os.path.join(base_dir, 'train', 'labels'))
shutil.move(os.path.join(source_dir, 'valid', 'images'), os.path.join(base_dir, 'valid', 'images'))
shutil.move(os.path.join(source_dir, 'valid', 'labels'), os.path.join(base_dir, 'valid', 'labels'))
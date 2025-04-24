import random
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_random_label_overlay(train_images_dir, train_labels_dir, num_images=4):
    """
    Function to show random images with their labels overlaid in a grid (1 row, 4 columns).

    :param train_images_dir: Path to the directory containing the images
    :param train_labels_dir: Path to the directory containing the labels
    :param num_images: Number of random images to show in the grid (default is 4)
    """
    fig, axs = plt.subplots(1, num_images, figsize=(15, 5))

    for i in range(num_images):
        # Randomly select an image and its corresponding label
        image_file = random.choice(os.listdir(train_images_dir))
        label_file = image_file.replace('.jpg', '.txt')  # Assuming the labels are .txt files with the same name as the image

        # Load the image
        image = cv2.imread(os.path.join(train_images_dir, image_file))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Load the label file
        label_path = os.path.join(train_labels_dir, label_file)
        with open(label_path, 'r') as file:
            labels = file.readlines()

        # Loop through each label and draw the bounding box on the image
        for label in labels:
            parts = label.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])

            # Convert normalized coordinates to pixel values
            img_height, img_width, _ = image.shape
            x_center = int(x_center * img_width)
            y_center = int(y_center * img_height)
            width = int(width * img_width)
            height = int(height * img_height)

            # Calculate the top-left and bottom-right corners of the bounding box
            x1 = x_center - width // 2
            y1 = y_center - height // 2
            x2 = x_center + width // 2
            y2 = y_center + height // 2

            # Draw the bounding box on the image
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Red color for bounding box

        # Display the image with bounding boxes overlaid
        axs[i].imshow(image)
        axs[i].axis('off')  # Turn off axis

    plt.tight_layout()
    plt.show()
    
train_images_dir = r'C:\Users\dixon\Desktop\ITS365\waldo-dataset-a\train\images\images'
train_labels_dir = r'C:\Users\dixon\Desktop\ITS365\waldo-dataset-a\train\labels\labels'

show_random_label_overlay(train_images_dir, train_labels_dir, num_images=4)
# This code was developed by Messaad Salim
# University of Msila
# For contact, LinkedIn: https://www.linkedin.com/in/salimmessaad
import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_image_with_histogram(image_path):
    # Read the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Histogram Equalization
    equalized_img = cv2.equalizeHist(img)

    # Display original and enhanced images using matplotlib
    plt.figure(figsize=(10,5))
    
    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Enhanced image
    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title("Enhanced Image")
    plt.axis('off')

    plt.show()

    # Save the enhanced image
    output_path = 'enhanced_image.png'
    cv2.imwrite(output_path, equalized_img)
    print(f"Enhanced image saved as {output_path}")

# call functions 
image_path = '/path/to/image.jpg'  # Provide the path to your image file
enhance_image_with_histogram(image_path)

def im():
    num = int(input())
    if(num==1):
        print(
            '''
# Practical 01 :- 
# TO GET INTRODUCED TO GOOGLE COLAB TO UNDESTAND THE VARIOUS PACKAGES USED FOR IMAGE ANALYSTICS
# !pip install cv2
 
# MoviePy is a Python library used for video editing. 
!pip install moviepy
 
# scikit-image is a collection of algorithms for image processing
!pip install scikit-image
 
# Pillow is a Python Imaging Library (PIL) fork that provides extensive file format support, 
# image processing, and graphics capabilities. 
# It's widely used for opening, manipulating, and saving images.
!pip install pillow
 
# OpenCV (Open Source Computer Vision Library) is primarily used for real-time computer vision tasks. 
# It provides tools for image and video analysis,
!pip install opencv-python
 
 
import cv2
from PIL import Image # pillow
 
import skimage #scikit-image
 
import moviepy.editor as mp #moviepy

'''
        )
    elif(num==3):
        print(
            '''
########################### 3. Resize  , check size and type of new image , copy  ###########
 
# Resizing the images and Check Out The data type
# First, install the required libraries
!pip install opencv-python-headless matplotlib
 
import cv2
import matplotlib.pyplot as plt
 
# Function to display images in Jupyter
def show_image(img, cmap=None):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap=cmap)
    plt.axis('off')  # Hide axes
    plt.show()
 
# Path to your image file
image_path = 'image01-removebg-preview.png'  # Update this with the correct path to your image
 
# Read the image
img = cv2.imread(image_path)
print('Original Image')
show_image(img)
height, width = img.shape[:2]
print(f'height * width = {height} x {width}')
 
# Resizing into a smaller image
print('Resizing into a smaller image')
new_width = int(img.shape[1] * 0.5)
new_height = int(img.shape[0] * 0.5)
resized_img = cv2.resize(img, (new_width, new_height))
show_image(resized_img)
 
height, width = resized_img.shape[:2]
print(f'height * width = {height} x {width}')
print(f'Image data type: {img.dtype}')
# Resizing into a larger image
print('Resizing into a larger image')
new_width1 = int(img.shape[1] * 2)
new_height2 = int(img.shape[0] * 2)
resized_img2 = cv2.resize(img, (new_width1, new_height2))
show_image(resized_img2)
 
height, width = resized_img2.shape[:2]
print(f'height * width = {height} x {width}')
print(f'Image data type: {img.dtype}')
 
# Converting image to grayscale
print('Converting Image to Grayscale')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.show()
 
# Resizing the grayscale image into a smaller size
print('Resizing the grayscale image into a smaller size')
new_width = int(gray_img.shape[1] * 0.5)
new_height = int(gray_img.shape[0] * 0.5)
resized_img = cv2.resize(gray_img, (new_width, new_height))
plt.imshow(resized_img, cmap='gray')
plt.axis('off')
plt.show()
 
height, width = resized_img.shape[:2]
print(f'height * width = {height} x {width}')
print(f'Image data type: {gray_img.dtype}')
 
 
# Resizing the grayscale image into a larger size
print('Resizing the grayscale image into a larger size')
new_width1 = int(gray_img.shape[1] * 2)
new_height2 = int(gray_img.shape[0] * 2)
resized_img2 = cv2.resize(gray_img, (new_width1, new_height2))
plt.imshow(resized_img2, cmap='gray')
plt.axis('off')
plt.show()
 
height, width = resized_img2.shape[:2]
print(f'height * width = {height} x {width}')
print(f'Image data type: {gray_img.dtype}')
 
# Using simple thresholding to create a binary image
print('Creating a binary image using thresholding')
_, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
plt.imshow(binary_img, cmap='gray')
plt.axis('off')
plt.show()
 
# Resizing the binary image into a smaller size
print('Resizing the binary image into a smaller size')
new_width = int(binary_img.shape[1] * 0.5)
new_height = int(binary_img.shape[0] * 0.5)
resized_img = cv2.resize(binary_img, (new_width, new_height))
plt.imshow(resized_img, cmap='gray')
plt.axis('off')
plt.show()
 
height, width = resized_img.shape[:2]
print(f'height * width = {height} x {width}')
print(f'Image data type: {binary_img.dtype}')
 
# Resizing the binary image into a larger size
print('Resizing the binary image into a larger size')
new_width1 = int(binary_img.shape[1] * 2)
new_height2 = int(binary_img.shape[0] * 2)
resized_img2 = cv2.resize(binary_img, (new_width1, new_height2))
plt.imshow(resized_img2, cmap='gray')
plt.axis('off')
plt.show()
 
height, width = resized_img2.shape[:2]
print(f'height * width = {height} x {width}')
print(f'Image data type: {binary_img.dtype}')

'''
        )
    elif(num==4):
        print(
            '''
################################################ 4 Lines circle text ###########################
 
# Install the required libraries (if not already installed)
!pip install opencv-python-headless matplotlib
 
import cv2
import matplotlib.pyplot as plt
 
# Function to display images in Jupyter
def show_image(img, cmap=None):
    if len(img.shape) == 2:  # If the image is grayscale/binary
        plt.imshow(img, cmap=cmap)
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axes
    plt.show()
 
# Path to your image file
image_path = 'image01-removebg-preview.png'  # Make sure the correct path to the image is provided
 
# Read the image
img = cv2.imread(image_path)
 
# Threshold the image to create a binary image
_, img2 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
 
# 4. Draw a line
cv2.line(img2, (0, 0), (100, 100), (255, 0, 0), 5)
 
# 5. Draw an arrowed line
cv2.arrowedLine(img2, (0, 100), (100, 0), (0, 255, 0), 5)
 
# 6. Draw a rectangle
cv2.rectangle(img2, (0, 100), (100, 200), (0, 0, 255), 5)
 
# 7. Draw a circle
cv2.circle(img2, (50, 50), 20, (255, 255, 0), 5)
 
# 8. Draw text on the image
cv2.putText(img2, 'Hello World', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
 
# Display the image with geometric shapes
show_image(img2)
'''
        )
    elif(num==5):
        print(
            '''
# Practical 05 Apply Image Enchacement
# Install the required libraries (if not already installed)
!pip install opencv-python-headless matplotlib numpy
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Function to display images in Jupyter
def show_image(img, cmap=None):
    if len(img.shape) == 2:  # If the image is grayscale/binary
        plt.imshow(img, cmap=cmap)
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axes
    plt.show()
 
# Path to your image file
image_path = 'image01-removebg-preview.png'  # Ensure the correct path to your image
 
# Load the image in color
color_img = cv2.imread(image_path)
 
# Check if the image was loaded correctly
if color_img is None:
    raise FileNotFoundError("The image file was not loaded correctly. Please check the file path.")
 
# Convert the color image to grayscale
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
 
# Create an all-black image with the same dimensions as the color image
black_img = np.zeros_like(color_img)
 
# Display the original color, grayscale, and black images
print("Original Color Image:")
show_image(color_img)
 
print("Original Grayscale Image:")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.show()
print("All Black Image:")
show_image(black_img)
 
# Adjust brightness and contrast
def adjust_brightness_contrast(img, brightness=0, contrast=0):
    img = np.int16(img)
    img = img * (contrast / 127 + 1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)
    return img
 
brightness = 30
contrast = 50
 
adjusted_color_img = adjust_brightness_contrast(color_img, brightness, contrast)
adjusted_gray_img = adjust_brightness_contrast(gray_img, brightness, contrast)
adjusted_black_img = adjust_brightness_contrast(black_img, brightness, contrast)
 
# Display adjusted images
print("Adjusted Color Image:")
show_image(adjusted_color_img)
 
print("Adjusted Grayscale Image:")
plt.imshow(adjusted_gray_img, cmap='gray')
plt.axis('off')
plt.show()
 
print("Adjusted Black Image:")
show_image(adjusted_black_img)
 
# Find digital negative of the image
negative_color_img = 255 - adjusted_color_img
negative_gray_img = 255 - adjusted_gray_img
negative_black_img = 255 - adjusted_black_img
 
# Display digital negative images
print("Color Digital Negative Image:")
show_image(negative_color_img)
 
print("Grayscale Digital Negative Image:")
plt.imshow(negative_gray_img, cmap='gray')
plt.axis('off')
plt.show()
 
print("Black Digital Negative Image:")
show_image(negative_black_img)
 
# Get the red, green, and blue values of each pixel
print("RGB values of the first 10x10 pixels of the negative color image:")
for y in range(10):
    for x in range(10):
        b, g, r = negative_color_img[y, x]
        print(f"Pixel at ({x},{y}): R={r}, G={g}, B={b}")
 
# Subtract each color value from 255 and save them as new color values
# Create new pixel values for the color image
height, width, channels = negative_color_img.shape
new_pixel_values = np.zeros_like(negative_color_img)
 
for y in range(height):
    for x in range(width):
        b, g, r = negative_color_img[y, x]
        new_b = 255 - b
        new_g = 255 - g
        new_r = 255 - r
        new_pixel_values[y, x] = [new_b, new_g, new_r]
 
# Save the new image
output_path_new = 'new_pixel_values.jpg'  # You can update the path if needed
cv2.imwrite(output_path_new, new_pixel_values)
 
# Display the new image
print("New Pixel Values Image:")
show_image(new_pixel_values)
# Plot results using OpenCV (replaced with matplotlib)
print("Plotting results...")
show_image(color_img)
show_image(adjusted_color_img)
show_image(negative_color_img)
show_image(new_pixel_values)
'''
        )
    elif(num==6):
        print(
            '''
######################################### 6 Detect Boundaries , dct , object detection using multiscale######
# Practical 06 :- 
# 1) Perform Boundary Detection on image 
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Step 1: Read the image
image = cv2.imread('image01-removebg-preview.png')
 
# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Step 3: Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
 
# Step 4: Use Canny Edge Detection
edges = cv2.Canny(blurred, 50, 150)
 
# Step 5: Find Contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Step 6: Draw Contours
# Option 1: Draw contours on the original image
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 2)
 
# Option 2: Draw contours on a blank image
blank_image = np.zeros_like(image)
cv2.drawContours(blank_image, contours, -1, (255, 255, 255), 2)
 
# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Contours on Original Image')
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
 
plt.subplot(1, 2, 2)
plt.title('Contours on Blank Image')
plt.imshow(cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB))
 
plt.show()
 
 
# 2) To find Discrete Consine Transform
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Step 3: Apply DCT
dct = cv2.dct(np.float32(gray))
 
# For better visualization, use a logarithmic scale
dct_log = np.log(abs(dct) + 1)
 
# Normalize the DCT image to the range [0, 255] for display
dct_norm = cv2.normalize(dct_log, None, 0, 255, cv2.NORM_MINMAX)
dct_norm = np.uint8(dct_norm)
 
# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Grayscale Image')
plt.imshow(gray, cmap='gray')
 
plt.subplot(1, 2, 2)
plt.title('DCT of Image (Log Scale)')
plt.imshow(dct_norm, cmap='gray')
 
plt.show()
 
 
# 3) To use Haar Transform object detection
 
import cv2
import matplotlib.pyplot as plt
 
# Step 1: Load the Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
# Step 2: Read the image
image = cv2.imread('image01-removebg-preview.png')
 
# Step 3: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Step 4: Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
 
# Step 5: Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
 
# Display the result
plt.figure(figsize=(10, 5))
plt.title('Detected Faces')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
'''
        )
    elif(num==7):
        print(
            '''
# practical 07  image compression
# Install necessary libraries (if not installed already)
!pip install opencv-python-headless pillow matplotlib numpy
 
import cv2
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
 
# Load the image (ensure that the file is in the correct path)
file_name = 'file_example_TIFF_1MB.tiff'  # Update this path if needed
image = cv2.imread(file_name)
 
if image is None:
    raise FileNotFoundError(f"Could not load image at {file_name}. Please check the file path.")
 
# Convert the image to RGB format for display with PIL and matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# Save images with lossless (PNG) and lossy (JPEG) compression
Image.fromarray(image_rgb).save('compressed_image_lossless.png', format='PNG', optimize=True)
cv2.imwrite('compressed_image_lossy.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
 
# Load compressed images
image_lossless = cv2.imread('compressed_image_lossless.png')
image_lossy = cv2.imread('compressed_image_lossy.jpg')
image_lossless_rgb = cv2.cvtColor(image_lossless, cv2.COLOR_BGR2RGB)
image_lossy_rgb = cv2.cvtColor(image_lossy, cv2.COLOR_BGR2RGB)
 
# Function to calculate PSNR (Peak Signal-to-Noise Ratio)
def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    return float('inf') if mse == 0 else 20 * np.log10(255.0 / np.sqrt(mse))
 
# Get file size in KB
def get_size(path):
    return os.path.getsize(path) / 1024
 
# Calculate PSNR values
psnr_lossless = calculate_psnr(image, image_lossless)
psnr_lossy = calculate_psnr(image, image_lossy)
 
# Image dimensions (width x height)
dimensions = f"{image.shape[1]} x {image.shape[0]}"
 
# Plot original, lossless, and lossy images with details
plt.figure(figsize=(18, 8))
 
# List of images and their descriptions
images_info = [
    (image_rgb, 'Original Image', get_size(file_name), 'N/A'),
    (image_lossless_rgb, 'Lossless Compression (PNG)', get_size('compressed_image_lossless.png'), f'{psnr_lossless:.2f}'),
    (image_lossy_rgb, 'Lossy Compression (JPEG)', get_size('compressed_image_lossy.jpg'), f'{psnr_lossy:.2f}')
]
 
# Display each image with its title, size, and PSNR
for idx, (img, title, size, psnr) in enumerate(images_info):
    plt.subplot(1, 3, idx + 1)
    plt.title(f'{title}\nSize: {size:.2f} KB\nDimensions: {dimensions}\nPSNR: {psnr}')
    plt.imshow(img)
    plt.axis('off')
 
plt.show()
 
'''
        )
    elif(num==8):
        print(
            '''

########################################################## # Video Capturing ##############
 
import cv2
import numpy as np
from PIL import Image as PILImage  # Use a distinct alias for PIL Image
from IPython.display import display as ip_display, clear_output
from io import BytesIO
 
# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default camera
 
def detect_faces():
    frame_count = 0  # Counter to limit the number of frames for demo purposes
    max_frames = 50  # Set a limit on how many frames to process
 
    while frame_count < max_frames:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
 
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
 
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
 
        # Convert frame to RGB and display it
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        display_image(frame_rgb)
 
        frame_count += 1  # Increment the frame count
 
    # Release the capture
    cap.release()
 
def display_image(image):
    """Displays the image in Jupyter Notebook."""
    # Convert image to PIL format
    pil_image = PILImage.fromarray(image)
    
    # Convert PIL image to BytesIO object
    buf = BytesIO()
    pil_image.save(buf, format='PNG')
    
    # Display image in the notebook
    ip_display(PILImage.open(buf))  # Display the PIL image directly
    clear_output(wait=True)
 
# Call the function to start face detection
detect_faces()
'''
        )
    elif(num==9):
        print(
            '''
################################################ Image capturing through video #######################
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
 
# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
# Start capturing video from the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default camera
 
# Define a function to display images using Matplotlib
def display_frame(frame):
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axis
    plt.show()
    plt.pause(0.001)  # Small pause to allow for rendering
 
# Start the capture process
start_time = time.time()  # Initialize start_time to track duration
 
try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if not ret:
            print("Failed to grab frame")
            break  # If there's an error, break the loop
 
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
 
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
        # Display the frame
        display_frame(frame)
 
        # Add a termination condition (e.g., after 10 seconds)
        if time.time() - start_time > 10:
            print("10 seconds have passed, exiting.")
            break
 
except KeyboardInterrupt:
    print("Interrupted by user")
 
finally:
    # Release the video capture object
    cap.release()
    print("Video capture released.")
'''
        )
    elif(num==10):
        print(
            '''
# Practical 03 : Resizing Images and checking data types of Images
# Display The Image
import cv2
from google.colab.patches import cv2_imshow
 
# Path to your image file
image_path = '/content/review-banner-03.jpg'
 
img = cv2.imread(image_path)
print('Original Image')
cv2_imshow(img)
height , widht = img.shape[:2]
print(f'height * widht = {height} x {widht}')
 
print('resizing into small image')
# Resize the image  (small size)
new_width = int(img.shape[1] * 0.5)
new_height = int(img.shape[0] * 0.5)
 
resized_img = cv2.resize(img, (new_width, new_height))
 
cv2_imshow(resized_img)
 
height , widht = resized_img.shape[:2]
print(f'height * widht = {height} x {widht}')
 
image_dataType = img.dtype
print(image_dataType)
 
 
# Resize the image (larger size)
new_width1 = int(img.shape[1] * 2)
new_height2 = int(img.shape[0] * 2)
 
resized_img2 = cv2.resize(img, (new_width1, new_height2))
 
cv2_imshow(resized_img2)
 
height , widht = resized_img2.shape[:2]
print(f'height * widht = {height} x {widht}')
 
image_dataType = img.dtype
print(image_dataType)
 
 
 
######################### Converting Image into Gray Scale and then Resizing images
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_img)
cv2_imshow(gray_img)
 
 
print('resizing into small image')
# Resize the image  (small size)
new_width = int(gray_img.shape[1] * 0.5)
new_height = int(gray_img.shape[0] * 0.5)
 
resized_img = cv2.resize(gray_img, (new_width, new_height))
 
cv2_imshow(resized_img)
 
height , widht = resized_img.shape[:2]
print(f'height * widht = {height} x {widht}')
 
image_dataType = gray_img.dtype
print(image_dataType)
 
 
# Resize the image (larger size)
new_width1 = int(gray_img.shape[1] * 2)
new_height2 = int(gray_img.shape[0] * 2)
 
resized_img2 = cv2.resize(gray_img, (new_width1, new_height2))
 
cv2_imshow(resized_img2)
 
height , widht = resized_img2.shape[:2]
print(f'height * widht = {height} x {widht}')
 
image_dataType = gray_img.dtype
print(image_dataType)
 
########################### Using Simple thersholding Method (to Binary Image)
# Threshold the grayscale image to create a binary image
# Using a simple thresholding method
_, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
print(binary_img)
cv2_imshow(binary_img)
 
print('resizing into small image')
# Resize the image  (small size)
new_width = int(binary_img.shape[1] * 0.5)
new_height = int(binary_img.shape[0] * 0.5)
 
resized_img = cv2.resize(binary_img, (new_width, new_height))
 
cv2_imshow(resized_img)
 
height , widht = resized_img.shape[:2]
print(f'height * widht = {height} x {widht}')
 
image_dataType = binary_img.dtype
print(image_dataType)
 
 
# Resize the image (larger size)
new_width1 = int(binary_img.shape[1] * 2)
new_height2 = int(binary_img.shape[0] * 2)
 
resized_img2 = cv2.resize(binary_img, (new_width1, new_height2))
 
cv2_imshow(resized_img2)
 
height , widht = resized_img2.shape[:2]
print(f'height * widht = {height} x {widht}')
 
image_dataType = binary_img.dtype
print(image_dataType)
'''
        )
    elif(num==11):
        print(
            '''
# Practical 04 :- Basic Geometric Operation using OpenCV
import cv2
from google.colab.patches import cv2_imshow
# Display The Image
 
# Path to your image file
image_path = '/content/review-banner-03.jpg'
 
img = cv2.imread(image_path)
# Use only the thresholded image from the output of cv2.threshold
_, img2 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
 
# 4. Draw line.
cv2.line(img2, (0, 0), (100, 100), (255, 0, 0), 5)
 
# 5. Draw Arrowed Line.
cv2.arrowedLine(img2, (0, 100), (100, 0), (0, 255, 0), 5)
 
# 6. Draw Rectangle.
cv2.rectangle(img2, (0, 100), (100, 200), (0, 0, 255), 5)
 
# 7. Draw Circle.
cv2.circle(img2, (50, 50), 20, (255, 255, 0), 5)
 
# 8. Draw text on the image.
cv2.putText(img2, 'Hello World', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
 
# Display the image
cv2_imshow(img2)
'''
        )
    elif(num==12):
        print(
            '''
# Practical 05 :- To Apply Image Enhancement Techniques
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
 
# Path to your image file (ensure the image is located at this path)
image_path = '/content/review-banner-03.jpg'
 
# Load the image in color
color_img = cv2.imread(image_path)
 
# Check if the image was loaded correctly
if color_img is None:
    raise FileNotFoundError("The image file was not loaded correctly. Please check the file path.")
 
# Convert the color image to grayscale
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
 
# Create an all-black image with the same dimensions as the color image
black_img = np.zeros_like(color_img)
 
# Display the original color, grayscale, and black images
print("Original Color Image:")
cv2_imshow(color_img)
print("Original Grayscale Image:")
cv2_imshow(gray_img)
print("All Black Image:")
cv2_imshow(black_img)
 
# Adjust brightness and contrast
def adjust_brightness_contrast(img, brightness=0, contrast=0):
    img = np.int16(img)
    img = img * (contrast / 127 + 1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)
    return img
 
brightness = 30
contrast = 50
 
adjusted_color_img = adjust_brightness_contrast(color_img, brightness, contrast)
adjusted_gray_img = adjust_brightness_contrast(gray_img, brightness, contrast)
adjusted_black_img = adjust_brightness_contrast(black_img, brightness, contrast)
 
# Display adjusted images
print("Adjusted Color Image:")
cv2_imshow(adjusted_color_img)
print("Adjusted Grayscale Image:")
cv2_imshow(adjusted_gray_img)
print("Adjusted Black Image:")
cv2_imshow(adjusted_black_img)
 
# Find digital negative of the image
negative_color_img = 255 - adjusted_color_img
negative_gray_img = 255 - adjusted_gray_img
negative_black_img = 255 - adjusted_black_img
 
# Display digital negative images
print("Color Digital Negative Image:")
cv2_imshow(negative_color_img)
print("Grayscale Digital Negative Image:")
cv2_imshow(negative_gray_img)
print("Black Digital Negative Image:")
cv2_imshow(negative_black_img)
 
# Get the red, green, and blue values of each pixel
print("RGB values of the first 10x10 pixels of the negative color image:")
for y in range(10):
    for x in range(10):
        b, g, r = negative_color_img[y, x]
        print(f"Pixel at ({x},{y}): R={r}, G={g}, B={b}")
 
 
# Subtract each color value from 255 and save them as new color values
# Create new pixel values for color image
height, width, channels = negative_color_img.shape
new_pixel_values = np.zeros_like(negative_color_img)
 
for y in range(height):
    for x in range(width):
        b, g, r = negative_color_img[y, x]
        new_b = 255 - b
        new_g = 255 - g
        new_r = 255 - r
        new_pixel_values[y, x] = [new_b, new_g, new_r]
 
# Save the new image
output_path_new = '/content/new_pixel_values.jpg'
cv2.imwrite(output_path_new, new_pixel_values)
 
# Display the new image
print("New Pixel Values Image:")
cv2_imshow(new_pixel_values)
 
# Plot results using OpenCV
print("Plotting results...")
cv2_imshow(color_img)
cv2_imshow(adjusted_color_img)
cv2_imshow(negative_color_img)
cv2_imshow(new_pixel_values)
'''
        )
    elif(num==13):
        print(
            '''
# Practical 06 :- 
# 1) Perform Boundary Detection on image 
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Step 1: Read the image
image = cv2.imread('/content/download (3).jpg')
 
# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Step 3: Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
 
# Step 4: Use Canny Edge Detection
edges = cv2.Canny(blurred, 50, 150)
 
# Step 5: Find Contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Step 6: Draw Contours
# Option 1: Draw contours on the original image
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 2)
 
# Option 2: Draw contours on a blank image
blank_image = np.zeros_like(image)
cv2.drawContours(blank_image, contours, -1, (255, 255, 255), 2)
 
# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Contours on Original Image')
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
 
plt.subplot(1, 2, 2)
plt.title('Contours on Blank Image')
plt.imshow(cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB))
 
plt.show()
 
 
# 2) To find Discrete Consine Transform
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Step 3: Apply DCT
dct = cv2.dct(np.float32(gray))
 
# For better visualization, use a logarithmic scale
dct_log = np.log(abs(dct) + 1)
 
# Normalize the DCT image to the range [0, 255] for display
dct_norm = cv2.normalize(dct_log, None, 0, 255, cv2.NORM_MINMAX)
dct_norm = np.uint8(dct_norm)
 
# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Grayscale Image')
plt.imshow(gray, cmap='gray')
 
plt.subplot(1, 2, 2)
plt.title('DCT of Image (Log Scale)')
plt.imshow(dct_norm, cmap='gray')
 
plt.show()
 
 
# 3) To use Haar Transform object detection
 
import cv2
import matplotlib.pyplot as plt
 
# Step 1: Load the Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
# Step 2: Read the image
image = cv2.imread('/content/download (3).jpg')
 
# Step 3: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Step 4: Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
 
# Step 5: Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
 
# Display the result
plt.figure(figsize=(10, 5))
plt.title('Detected Faces')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
'''
        )
    elif(num==14):
        print(
            '''
# Practical 07 :- Perform Image Compression (Lossy and Lossless)
# Import necessary libraries
from google.colab import files
import cv2, os, numpy as np
from PIL import Image
import matplotlib.pyplot as plt
 
# Load the image and convert to RGB for Pillow and plotting
file_name = '/content/file_example_TIFF_1MB.tiff'
image = cv2.imread(file_name)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# Save images with lossless (PNG) and lossy (JPEG) compression
Image.fromarray(image_rgb).save('compressed_image_lossless.png', format='PNG', optimize=True)
cv2.imwrite('compressed_image_lossy.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
 
# Load compressed images
image_lossless = cv2.imread('compressed_image_lossless.png')
image_lossy = cv2.imread('compressed_image_lossy.jpg')
image_lossless_rgb = cv2.cvtColor(image_lossless, cv2.COLOR_BGR2RGB)
image_lossy_rgb = cv2.cvtColor(image_lossy, cv2.COLOR_BGR2RGB)
 
# Function to calculate PSNR (Peak Signal-to-Noise Ratio)
def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    return float('inf') if mse == 0 else 20 * np.log10(255.0 / np.sqrt(mse))
 
# Get details: file sizes, dimensions, PSNR values
get_size = lambda path: os.path.getsize(path) / 1024
psnr_lossless = calculate_psnr(image, image_lossless)
psnr_lossy = calculate_psnr(image, image_lossy)
dimensions = f"{image.shape[1]} x {image.shape[0]}"
 
# Plot original, lossless, and lossy images with details
plt.figure(figsize=(18, 8))
for idx, (img, title, size, psnr) in enumerate([
    (image_rgb, 'Original Image', get_size(file_name), 'N/A'),
    (image_lossless_rgb, 'Lossless Compression (PNG)', get_size('compressed_image_lossless.png'), f'{psnr_lossless:.2f}'),
    (image_lossy_rgb, 'Lossy Compression (JPEG)', get_size('compressed_image_lossy.jpg'), f'{psnr_lossy:.2f}')
]):
    plt.subplot(1, 3, idx + 1)
    plt.title(f'{title}\nSize: {size:.2f} KB\nDimensions: {dimensions}\nPSNR: {psnr}')
    plt.imshow(img)
    plt.axis('off')
plt.show()
'''
        )
   
    else:
        print(
            '''
        1: TO GET INTRODUCED TO GOOGLE COLAB TO UNDESTAND THE VARIOUS PACKAGES USED FOR 
        3: Resize  , check size and type of new image , copy
        4 :  Lines circle text 
        5 : Apply Image Enchacement
        6 : Detect Boundaries , dct , object 
        7 : image compression
        8 : Video Capturing 
        9 : Image capturing through video
        10 : (COLAB) Resizing Images and checking data types of Images
        11 : (COLAB) Basic Geometric Operation using OpenCV
        12 : (COLAB) To Apply Image Enhancement Techniques
        13 : (COLAB) Detect Boundaries , dct , object 
        14 : (COLAB) image compression


'''
        )
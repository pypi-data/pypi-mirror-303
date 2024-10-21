def iva():
    num = int(input())
    if(num==1):
        print('''
#Open CV
import cv2

#Scipy
import scipy
from scipy import ndimage

#Pillow
from PIL import Image, ImageDraw, ImageFilter
''')
    elif(num==2):
        print('''
#   !pip install opencv-python
#   !pip install matplotlib
import cv2
from matplotlib import pyplot as plt
import os

# Step 2: Read the image file
image_path = r'/content/them-snapshots-Tp0DalYO_2U-unsplash.jpg'
image = cv2.imread(image_path)

# Step 3: Convert the image from BGR (OpenCV default) to RGB (for correct display in matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 4: Display the image using matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Turn off axis labels
plt.show()

# Step 5: Display the size of the image in pixels (height, width, channels)
image_size_pixels = image.shape  # returns (height, width, channels)
print(f"Image Size (Height, Width, Channels): {image_size_pixels}")

# Step 6: Get the file size in MB
file_size_mb = os.path.getsize(image_path) / (1024 * 1024)  # size in MB
print(f"Image File Size: {file_size_mb:.2f} MB")

# Optional Step 7: Write the displayed image into a new file (saving as 'new_image.jpg')
cv2.imwrite(r'new_image.jpg', image)


              ''')
    elif(num==3):
        print('''
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

image_path = '/content/them-snapshots-Tp0DalYO_2U-unsplash.jpg'

# Read color image
color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Read grayscale image
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Read binary(B\W) image (thresholding may be required)
_, binary_image = cv2.threshold(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), 127, 255, cv2.THRESH_BINARY)

# Display color image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))  # Convert color space for matplotlib
plt.title('Color Image')

# Display grayscale image
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

# Display binary image
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

plt.show()

#color image====================================================================
resized_big_image = cv2.resize(color_image, (500, 500))
resized_small_image = cv2.resize(color_image, (100, 100))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))  # Convert color space for matplotlib
plt.title('Original Image')

# Display big resized image
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(resized_big_image, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')

# Display small resized image
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(resized_small_image, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')

print("Resized Image Shape:", resized_big_image.shape)
print("Resized Image Type:", resized_big_image.dtype)

plt.show()

#GrayScale image================================================================
gresized_big_image = cv2.resize(gray_image, (500, 500))
gresized_small_image = cv2.resize(gray_image, (100, 100))

# Display original image
plt.subplot(2, 3, 1)
plt.imshow(gray_image, cmap='gray')  # Convert color space for matplotlib
plt.title('Original Image')

# Display big resized image
plt.subplot(2, 3, 2)
plt.imshow(gresized_big_image, cmap='gray')
plt.title('Resized Image')

# Display small resized image
plt.subplot(2, 3, 3)
plt.imshow(gresized_small_image, cmap='gray')
plt.title('Resized Image')

print("Resized Image Shape:", gresized_big_image.shape)
print("Resized Image Type:", gresized_big_image.dtype)

plt.show()

#Black and White image==========================================================
gresized_big_image = cv2.resize(binary_image, (500, 500))
gresized_small_image = cv2.resize(binary_image, (100, 100))

# Display original image
plt.subplot(2, 3, 1)
plt.imshow(binary_image, cmap='gray')  # Convert color space for matplotlib
plt.title('Original Image')

# Display big resized image
plt.subplot(2, 3, 2)
plt.imshow(gresized_big_image, cmap='gray')
plt.title('Resized Image')

# Display small resized image
plt.subplot(2, 3, 3)
plt.imshow(gresized_small_image, cmap='gray')
plt.title('Resized Image')

print("Resized Image Shape:", gresized_big_image.shape)
print("Resized Image Type:", gresized_big_image.dtype)

plt.show()

              ''')
    elif(num==4):
        print('''
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Load the RGB image (replace 'your_image.jpg' with the path to your image)
image_path = '/content/them-snapshots-Tp0DalYO_2U-unsplash.jpg'  # Example image path
image = cv2.imread(image_path)

# Step 2: Convert the image to black and white (grayscale)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to display images
def display_image(img, title):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct display
    plt.title(title)
    plt.axis('off')
    plt.show()

# Step 3: Display the grayscale image
display_image(image_gray, 'Grayscale Image')

# Shape parameters
shapes = {
    'line': {
        'start_point': (200, 200),
        'end_point': (5000, 5000),
        'color': (255, 255, 255),  # White
        'thickness': 90
    },
    'arrowed_line': {
        'start_point': (200, 200),
        'end_point': (3000, 3000),
        'color': (255, 255, 255),  # White
        'thickness': 90
    },
    'rectangle': {
        'top_left': (200, 200),
        'bottom_right': (2000, 3000),
        'color': (255, 255, 255),  # White
        'thickness': 50
    },
    'circle': {
        'center': (1000, 1000),
        'radius': 900,
        'color': (255, 255, 255),  # White
        'thickness': 50
    },
    'text': {
        'text': 'OpenCV Shapes',
        'position': (120, 450),
        'font': cv2.FONT_HERSHEY_SIMPLEX,
        'font_scale': 10,
        'color': (255, 255, 255),  # White
        'thickness': 50
    }
}

# Step 4: Draw a line on a copy of the grayscale image
image_line = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)  # Convert to BGR for colored shapes
cv2.line(image_line, shapes['line']['start_point'], shapes['line']['end_point'], shapes['line']['color'], shapes['line']['thickness'])
display_image(image_line, 'Image with Line')

# Step 5: Draw an arrowed line on a copy of the grayscale image
image_arrowed_line = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
cv2.arrowedLine(image_arrowed_line, shapes['arrowed_line']['start_point'], shapes['arrowed_line']['end_point'], shapes['arrowed_line']['color'], shapes['arrowed_line']['thickness'])
display_image(image_arrowed_line, 'Image with Arrowed Line')

# Step 6: Draw a rectangle on a copy of the grayscale image
image_rectangle = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
cv2.rectangle(image_rectangle, shapes['rectangle']['top_left'], shapes['rectangle']['bottom_right'], shapes['rectangle']['color'], shapes['rectangle']['thickness'])
display_image(image_rectangle, 'Image with Rectangle')

# Step 7: Draw a circle on a copy of the grayscale image
image_circle = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
cv2.circle(image_circle, shapes['circle']['center'], shapes['circle']['radius'], shapes['circle']['color'], shapes['circle']['thickness'])
display_image(image_circle, 'Image with Circle')

# Step 8: Put text on a copy of the grayscale image
image_text = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
cv2.putText(image_text, shapes['text']['text'], shapes['text']['position'], shapes['text']['font'], shapes['text']['font_scale'], shapes['text']['color'], shapes['text']['thickness'], cv2.LINE_AA)
display_image(image_text, 'Image with Text')

              ''')
    elif(num==5):
        print('''
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Load the color image (replace with your image path)
image_path = '/content/them-snapshots-Tp0DalYO_2U-unsplash.jpg'  # Example image path
image = cv2.imread(image_path)

# Step 2: Adjust brightness and contrast
alpha = 1.5  # Contrast control (1.0-3.0)
beta = 50    # Brightness control (0-100)

# Adjust brightness and contrast
adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Step 3: Find the digital negative of the image
negative_image = 255 - image

# Step 4: Get the shape of the image
height, width, _ = image.shape

#Step 5: Print RGB values of each pixel evey row and column
#print("RGB Values of each pixel:")
#for y in range(height):
 #   for x in range(width):
  #      b, g, r = image[y, x]  # Get BGR values
   #     print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")

# Step 5: Print RGB values of a sample of pixels every 10th row and 10th column
print("Sample RGB Values of the image:")
for y in range(0, height, height // 10):  # Sample every 10th row
    for x in range(0, width, width // 10):  # Sample every 10th column
        b, g, r = image[y, x]  # Get BGR values
        print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")
    print()  # Add a new line after each row for better readability

# Step 6: Subtract each color value from 255 to create new color values
new_blue_channel = 255 - image[:, :, 0]
new_green_channel = 255 - image[:, :, 1]
new_red_channel = 255 - image[:, :, 2]

# Step 7: Create a new pixel value from the modified colors
new_image = cv2.merge((new_blue_channel, new_green_channel, new_red_channel))

# Step 8: Plot the results
plt.figure(figsize=(15, 10))

# Display the original image
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Display the adjusted image
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
plt.title('Adjusted Brightness and Contrast')
plt.axis('off')

# Display the negative image
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
plt.title('Digital Negative')
plt.axis('off')

# Display the new image created from modified colors
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.title('New Image from Modified Colors')
plt.axis('off')

plt.tight_layout()
plt.show()

              ''')
    elif(num==6):
        print('''
import cv2
from google.colab.patches import cv2_imshow
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/content/Yahya_Khan.webp'  # Update the path if needed
image = cv2.imread(image_path)
image_resized = cv2.resize(image, (500, 500))  # Resize for consistency in display

# Check if the image loaded successfully
if image is None:
    print("Error: Could not read the image. Check the file path.")
else:
    # Step 1: Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Apply Histogram Equalization for better contrast
    gray_image = cv2.equalizeHist(gray_image)

    # Step 3: Apply Gaussian Blur
    img_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Step 4: Detect Canny edges with adjusted thresholds
    lower_threshold = 50
    upper_threshold = 150
    edges = cv2.Canny(img_blur, lower_threshold, upper_threshold)

    # Step 5: Find contours
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print("Number of Contours found =", len(contours))

    # Step 6: Compute Discrete Cosine Transform (DCT)
    img_float = np.float32(gray_image)
    dct = cv2.dct(img_float)
    dct_normalized = cv2.normalize(dct, None, 0, 255, cv2.NORM_MINMAX)  # Normalize for visualization
    dct_display = np.uint8(dct_normalized)

    # Step 7: Inverse DCT to reconstruct the image
    img_reconstructed = cv2.idct(dct)
    img_reconstructed = np.uint8(cv2.normalize(img_reconstructed, None, 0, 255, cv2.NORM_MINMAX))

    # Step 8: Object Detection using Haar Cascade
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    cascade = cv2.CascadeClassifier(cascade_path)

    # Step 9: Detect objects (e.g., faces) in the image
    faces = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Plot Results
    plt.figure(figsize=(15, 10))

    # Original Image
    plt.subplot(3, 2, 1)
    plt.imshow(cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Canny Edges
    plt.subplot(3, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges')
    plt.axis('off')

    # DCT Coefficients
    plt.subplot(3, 2, 3)
    plt.imshow(dct_display, cmap='gray')
    plt.title('DCT Coefficients')
    plt.axis('off')

    # Reconstructed Image from DCT
    plt.subplot(3, 2, 4)
    plt.imshow(img_reconstructed, cmap='gray')
    plt.title('Reconstructed Image from DCT')
    plt.axis('off')

    # Display image with detected objects (faces)
    plt.subplot(3, 2, 5)
    detected_image = image_resized.copy()  # Make a copy of the resized image
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(detected_image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw rectangle around detected objects
        plt.imshow(cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB))
        plt.title('Detected Objects (Faces)')
    else:
        plt.imshow(cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB))
        plt.title('No Faces Detected')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

              ''')
    elif(num==7):
        print('''
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import os

# Step 1: Load the image
image_path = '/content/lossless_image.png'  # Replace with your image path
image = cv2.imread(image_path)

# Step 2: Save the image with Lossless Compression (PNG format)
lossless_image_path = '/content/lossless_image.png'
cv2.imwrite(lossless_image_path, image, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # PNG is lossless by default

# Step 3: Save the image with Lossy Compression (JPEG format)
lossy_image_path = '/content/lossy_image.jpg'
cv2.imwrite(lossy_image_path, image, [cv2.IMWRITE_JPEG_QUALITY, 50])  # JPEG is lossy; quality=50 means medium compression

# Step 4: Load the saved images back for comparison
lossless_image = cv2.imread(lossless_image_path)
lossy_image = cv2.imread(lossy_image_path)

# Step 5: Plot and Compare the results
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Lossless Image (PNG)
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(lossless_image, cv2.COLOR_BGR2RGB))
plt.title('Lossless Compression (PNG)')
plt.axis('off')

# Lossy Image (JPEG)
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(lossy_image, cv2.COLOR_BGR2RGB))
plt.title('Lossy Compression (JPEG)')
plt.axis('off')

plt.tight_layout()
plt.show()

# Step 6: Compare the File Sizes
original_size = os.path.getsize(image_path) / 1024  # in KB
lossless_size = os.path.getsize(lossless_image_path) / 1024  # in KB
lossy_size = os.path.getsize(lossy_image_path) / 1024  # in KB

print(f"Original Image Size: {original_size:.2f} KB")
print(f"Lossless Compressed Image Size (PNG): {lossless_size:.2f} KB")
print(f"Lossy Compressed Image Size (JPEG): {lossy_size:.2f} KB")

# Function to plot the histogram for an image
def plot_histogram(image, title):
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')  # Blue, Green, Red
    plt.figure(figsize=(10, 6))
    for channel, color in zip(channels, colors):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f'{color.upper()} channel')

    plt.title(title)
    plt.xlabel('Intensity Value (0-255)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Step 5: Plot the histograms for the original, lossless, and lossy images
plot_histogram(image, 'Original Image - Color Histogram')
plot_histogram(lossless_image, 'Lossless Image (PNG) - Color Histogram')
plot_histogram(lossy_image, 'Lossy Image (JPEG) - Color Histogram')

              ''')
    elif(num==8):
        print('''
import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
import os

# File path for the TIFF image
tiff_image_path = '/content/drive/MyDrive/file_example_TIFF_1MB.tiff'

# Load the TIFF image
img = cv2.imread(tiff_image_path, cv2.IMREAD_UNCHANGED)

# Save as lossless PNG
cv2.imwrite('lossless_compressed_image.png', img)

# Save as lossy JPEG
jpeg_quality = 90  # A value between 0 and 100 (higher means better quality, but larger file size)
cv2.imwrite('lossy_compressed_image.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])

# Get sizes of the files
original_size = os.path.getsize(tiff_image_path)
lossless_size = os.path.getsize('lossless_compressed_image.png')
lossy_size = os.path.getsize('lossy_compressed_image.jpg')

print(f'Original image size: {original_size} bytes')
print(f'Lossless compressed image size: {lossless_size} bytes')
print(f'Lossy compressed image size: {lossy_size} bytes')

# Load images for display
img = cv2.imread(tiff_image_path, cv2.IMREAD_UNCHANGED)
lossless_img = cv2.imread('lossless_compressed_image.png')
lossy_img = cv2.imread('lossy_compressed_image.jpg')

# Convert BGR to RGB for Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lossless_img_rgb = cv2.cvtColor(lossless_img, cv2.COLOR_BGR2RGB)
lossy_img_rgb = cv2.cvtColor(lossy_img, cv2.COLOR_BGR2RGB)

# Create a figure and a set of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original Image
axes[0].imshow(img_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')  # Hide axes

# Lossless Compressed Image
axes[1].imshow(lossless_img_rgb)
axes[1].set_title('Lossless Compressed Image')
axes[1].axis('off')  # Hide axes

# Lossy Compressed Image
axes[2].imshow(lossy_img_rgb)
axes[2].set_title('Lossy Compressed Image')
axes[2].axis('off')  # Hide axes

# Display the plot
plt.show()

# Function to plot the histogram for an image
def plot_histogram(image, title):
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')  # Blue, Green, Red
    plt.figure(figsize=(10, 6))
    for channel, color in zip(channels, colors):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f'{color.upper()} channel')

    plt.title(title)
    plt.xlabel('Intensity Value (0-255)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Step 5: Plot the histograms for the original, lossless, and lossy images
plot_histogram(img, 'Original Image - Color Histogram')
plot_histogram(lossless_img, 'Lossless Image (PNG) - Color Histogram')
plot_histogram(lossy_img, 'Lossy Image (JPEG) - Color Histogram')

              ''')
    elif(num==9):
        print('''
!pip install opencv-python
!pip install matplotlib
!pip install numpy

#===========live Detection =====================================================================
import cv2
import numpy as np

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break  # If there's an error, break the loop

    # Resize the frame for a consistent window size
    frame_resized = cv2.resize(frame, (400, 300))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Create a copy of the original frame for face detection display
    face_detection_frame = frame_resized.copy()

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(face_detection_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Stack the images horizontally
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # Convert grayscale to BGR for stacking
    stacked_frame = np.hstack((frame_resized, gray_bgr, face_detection_frame))

    # Display the stacked frame
    cv2.imshow('Original | Grayscale | Face Detection', stacked_frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
              ''')
    elif(num==10):
        print('''
!pip install opencv-python
!pip install matplotlib
!pip install numpy

#===========live Detection =====================================================================
import cv2
import numpy as np

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break  # If there's an error, break the loop

    # Resize the frame for a consistent window size
    frame_resized = cv2.resize(frame, (400, 300))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Create a copy of the original frame for face detection display
    face_detection_frame = frame_resized.copy()

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(face_detection_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Stack the images horizontally
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # Convert grayscale to BGR for stacking
    stacked_frame = np.hstack((frame_resized, gray_bgr, face_detection_frame))

    # Display the stacked frame
    cv2.imshow('Original | Grayscale | Face Detection', stacked_frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()


#===========Recording and processing =====================================================================
import cv2
import time

# Step 1: Configure Video Capture Device (open webcam)
video_capture = cv2.VideoCapture(0)  # 0 for the default webcam

# Check if the webcam is opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video capture device.")
    exit()

# Step 2: Capture Video Data for 10 seconds
fps = 20  # Frames per second
frame_width = int(video_capture.get(3))  # Get the frame width
frame_height = int(video_capture.get(4))  # Get the frame height

# Define the codec and create VideoWriter objects to save original and grayscale videos
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_original = cv2.VideoWriter('original_video.avi', fourcc, fps, (frame_width, frame_height))
out_gray = cv2.VideoWriter('grayscale_video.avi', fourcc, fps, (frame_width, frame_height), isColor=False)

# Start a timer to capture video for 10 seconds
start_time = time.time()

while True:
    # Step 3: Read the current frame
    ret, frame = video_capture.read()

    # If frame reading was successful
    if ret:
        # Step 4: Process the video data (convert to grayscale)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Step 5: Transmit (display) the original and grayscale frames
        cv2.imshow('Original Video', frame)
        cv2.imshow('Grayscale Video', gray_frame)

        # Step 6: Store the frames (original and grayscale)
        out_original.write(frame)  # Save original frame
        out_gray.write(gray_frame)  # Save grayscale frame

        # Exit when 10 seconds are reached or if 'q' is pressed
        if (time.time() - start_time) > 10 or cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Step 7: Release the video capture and video writer objects
video_capture.release()
out_original.release()
out_gray.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

print("Video capturing and processing completed!")



#get working dict
import os
print(os.getcwd())
              ''')
    else:
        print('''
    1:Install basic package code
    2:Read image in jpeg format and its size and save image
    3:Resize Image and change into B/W , Grayscale
    4:Black White image with shapes
    5:Adjust brightness, get pixel value , digital negative , divide by 255 etc etc
    6:Detect boundries , object , and find DCT
    7:Lossy and lossless compresion technique
    8:Lossy and Lossless on tiff image
    9:Live video detection and processing
    10:Live video recording and saving in grayscale
              ''')
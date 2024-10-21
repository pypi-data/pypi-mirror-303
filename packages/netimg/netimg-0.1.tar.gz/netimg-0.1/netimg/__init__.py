def help():
    help_code = '''
    1. basic() : Read, Display, Size, Type
    2. convert() : Gray, Binary, Print Size, Resize, Copy
    3. geometry() : Draw Shapes
    4. enhancement() : Brightness & Contrast, Digital Negative
    5. egde() : Canny Edge Detection
    6. dct() : Discrete Cosine Transformation
    7. face()  or eye()  : Object detection
    8. compression() : Lossy & Lossless Compression
    9. video_face() : Pre-Recorded Video
    10. face_live : Face Detection on Live Video
    '''
    print("Available methods in netbg package:\nExample :\n\timport imgpro as m\n\tm.egde()")
    print(f"\n{help_code}")


def basic():
    code = '''
# !pip install opencv-python
import cv2
import mimetypes
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg")

cv2.imwrite('new_image.jpg', image)
print(f"Image Size: {image.shape}")
mime_type, _ = mimetypes.guess_type("flower.jpg")
print(f'File type: {mime_type}')

plt.figure(figsize=(8, 5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')
plt.show()
    '''
    print(code)


def convert():
    code = '''
import cv2
import matplotlib.pyplot as plt

image_path = 'flower.jpg'
original_image = cv2.imread(image_path)
print(f"Original Image Size: {original_image.shape}")

# Display the original image
plt.figure(figsize=(8, 5))
plt.subplot(2,2,1)
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
plt.imshow(original_image_rgb)
plt.title("Original Image")
plt.axis('off')


resized_image = cv2.resize(original_image, (291,194))
print(f"Resized Image Size: {resized_image.shape}")

copied_image = resized_image.copy()
gray_image = cv2.cvtColor(copied_image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

plt.subplot(2,2,2)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# Display the binary image
plt.subplot(2,2,3)
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image")
plt.axis('off')

# Display the copied resized image
copied_image_rgb = cv2.cvtColor(copied_image, cv2.COLOR_BGR2RGB)
plt.subplot(2,2,4)
plt.imshow(copied_image_rgb)
plt.title("Copied Resized Image")
plt.axis('off')
plt.show()
    '''
    print(code)


def geometry():
    code = '''
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.ones((450, 500,3), dtype=np.uint8) * 255
print(image.shape)

cv2.line(image, (50, 50), (350, 50), (255, 0, 0), 2)
cv2.arrowedLine(image, (50, 100), (350, 100), (255, 0, 0), 2)
cv2.rectangle(image, (50, 150), (350, 250), (255, 0, 0), -1)
cv2.circle(image, (200, 350), 50, (255, 0, 0), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Hello, OpenCV!', (60, 200), font, 1, (255, 255, 255), 2)

# Display the image using Matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Drawing Shapes on Color Image')
plt.show()
    '''
    print(code)


def enhancement():
    code ='''
import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('flower.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


bright_contrast_image = cv2.convertScaleAbs(image, alpha=1.2, beta=15)

negative_image =  255 - image

b, g, r = cv2.split(image)
new_b = 255 - b
new_g = 255 - g
new_r = 255 - r
new_image = cv2.merge((new_b, new_g, new_r))

# Plot the results
plt.figure(figsize=(8, 5))
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(bright_contrast_image, cv2.COLOR_BGR2RGB))
plt.title('Bright & Contrast Adjusted')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
plt.title('Digital Negative')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.title('Modified Colors')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.tight_layout()
plt.show()
    '''
    print(code)


def egde():
    code ='''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('flower.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
edges = cv.Canny(img,50,200)

plt.figure(figsize=(8,8))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(edges,cmap = 'gray')
plt.title('Edges of original Image')
plt.axis('off')
plt.show()
    '''
    print(code)


def dct():
    code = '''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('flower.jpg')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

dct_image = cv2.dct(np.float32(gray_image))
restored_image = cv2.idct(dct_image)

plt.figure(figsize=(10,8))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(dct_image, cmap='gray')
plt.title('DCT Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(restored_image, cmap='gray')
plt.title('Inverse DCT Image')
plt.axis('off')
plt.show()
    '''
    print(code)


def face():
    code = '''
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('person.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

plt.figure(figsize=(10, 5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title(f"Faces Detected: {len(faces)}")
plt.axis('off')
plt.show()

    '''
    print(code)


def eye():
    code ='''
import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('eye.webp')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Detect bodies
bodies = body_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected bodies
for (x, y, w, h) in bodies:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 155, 0), 2)  # Body rectangle

# Display the result
plt.figure(figsize=(8, 5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Detected Eyes')
plt.axis('off')
plt.show()
    '''
    print(code)


def compression():
    code = '''
import cv2
import matplotlib.pyplot as plt
import os

image_path = "flower.jpg"
image = cv2.imread(image_path)
lossless_path = 'lossless.png'
cv2.imwrite(lossless_path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9]) # [int(cv2.IMWRITE_PNG_COMPRESSION),5])  Range 0-9, Default 1

lossy_path = 'lossy.jpg'
cv2.imwrite(lossy_path, image,[int(cv2.IMWRITE_JPEG_QUALITY), 20])  # Range 0 to 100, Default 95
lossless_image = cv2.imread(lossless_path)
lossy_image = cv2.imread(lossy_path)

# Convert images from BGR to RGB format for proper color display
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
lossless_image = cv2.cvtColor(lossless_image, cv2.COLOR_BGR2RGB)
lossy_image = cv2.cvtColor(lossy_image, cv2.COLOR_BGR2RGB)

original_size = os.path.getsize(image_path)
lossless_size = os.path.getsize(lossless_path)
lossy_size = os.path.getsize(lossy_path)

# Plot the results
plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
plt.title(f'Original {round(original_size/1024)} kb')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title(f'Lossless {round(lossless_size/1024)} kb')
plt.imshow(lossless_image)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title(f'Lossy {round(lossy_size/1024)} kb')
plt.imshow(lossy_image)
plt.axis('off')
plt.show()
    '''
    print(code)

def video_face():
    code = '''
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('WIN_20241020_12_38_49_Pro.mp4')

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_with_faces.mp4', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("End of video file.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    out.write(frame)

cap.release()
out.release()
    '''
    print(code)


def face_live():
    code = '''
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    out.write(frame)
    cv2.imshow('Face Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
    '''
    print(code)
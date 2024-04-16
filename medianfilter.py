import numpy as np
import cv2

def saltnpepper(img, p):
    # Convert to grayscale if image is colored
    if len(img.shape) == 3:
        gray_img = img[:,:,2]  # Assuming red channel represents grayscale
    else:
        gray_img = img.copy()

    # Randomly add salt and pepper noise
    noisy_img = gray_img.copy()
    salt_pepper = np.random.rand(*gray_img.shape)
    noisy_img[salt_pepper < p/2] = 0  # Salt noise
    noisy_img[salt_pepper > 1 - p/2] = 255  # Pepper noise

    return noisy_img

def median_filter(img, W):
    # Create a padded version of the image to handle boundary pixels
    padded_img = cv2.copyMakeBorder(img, W//2, W//2, W//2, W//2, cv2.BORDER_REFLECT)

    # Apply median filtering
    filtered_img = np.zeros_like(img)
    for i in range(filtered_img.shape[0]):
        for j in range(filtered_img.shape[1]):
            neighborhood = padded_img[i:i+W, j:j+W].flatten()
            median_val = np.median(neighborhood)
            filtered_img[i, j] = median_val

    return filtered_img

# Load the image
image = cv2.imread(r'C:\Users\Gabi Fuller\Documents\Depaul.jpg', cv2.IMREAD_COLOR)

# Add salt-and-pepper noise
noisy_image = saltnpepper(image, p=0.05)  # Adjust p as needed

# Apply median filtering
filtered_image = median_filter(noisy_image, W=3)  # Adjust W as needed

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
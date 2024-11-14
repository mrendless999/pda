from PIL import Image
import numpy as np

# Load the image
image = Image.open("C:\Users\Admin\Pictures\wallpaper\wallpaperflare.com_wallpaper (14).jpg")

# Convert the image to a NumPy array
image_array = np.array(image)

# Crop the image (example: crop 100 pixels from each side)
# Syntax: array[start_row:end_row, start_column:end_column]
cropped_image = image_array[100:-100, 100:-100]

# Flip the image horizontally (axis=1 for left-right flip)
flipped_image = np.flip(cropped_image, axis=1)

# Convert the NumPy array back to an image
result_image = Image.fromarray(flipped_image)

# Save or display the resulting image
result_image.show()  # To display the image
result_image.save("output_image.jpg")  # To save the image

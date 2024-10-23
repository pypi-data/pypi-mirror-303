import numpy as np
from PIL import Image

def band2img(band, filename):
	# Scale the array to the 0-255 range
	scaled_image = ((band - np.min(band)) / (np.max(band) - np.min(band))) * 255

	# Convert the array to 8-bit unsigned integer type
	uint8_image = scaled_image.astype(np.uint8)

	# Save the array as an 8-bit TIFF file
	im = Image.fromarray(uint8_image)
	im.save(filename)
	return
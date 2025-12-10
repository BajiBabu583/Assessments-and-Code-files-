import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

# Initialize Vertex AI
vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")

# Ask user
prompt = input("Enter the description of the image you want:\n")

# Correct model class
model = ImageGenerationModel.from_pretrained("imagen-2.0")

# Generate image
result = model.generate_images(
    prompt=prompt,
    number_of_images=1,
    size="1024x1024"
)

# Save image
img_bytes = result.images[0]._image_bytes

with open("generated.png", "wb") as f:
    f.write(img_bytes)

print("Image saved as generated.png")

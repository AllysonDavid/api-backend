from openai import OpenAI
import base64

client = OpenAI()

result = client.images.generate(
    model="gpt-image-1",
    prompt="A forgotten lighthouse on a rocky shore, comic style",
    size="1024x1024"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("panel1.png", "wb") as f:
    f.write(image_bytes)

print("Image saved as panel1.png")

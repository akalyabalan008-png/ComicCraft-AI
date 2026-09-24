import os
import shutil
from gradio_client import Client


def generate_image(prompt, filename):
    client = Client("mrfakename/Z-Image-Turbo", httpx_kwargs={"timeout": 300})

    result = client.predict(
        prompt,
        512,
        512,
        9,
        42,
        True,
        api_name="/generate_image"
    )

    generated_image = result[0]

    os.makedirs("static/images", exist_ok=True)

    output_path = os.path.join("static/images", filename)

    shutil.copy(generated_image, output_path)

    return f"/static/images/{filename}"

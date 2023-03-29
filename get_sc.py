import requests
from PIL import Image
import io


def extract(url):
    # Download the GIF file from the URL
    url1 = url
    response = requests.get(url1)

    # Open the GIF file from the response content
    gif = Image.open(io.BytesIO(response.content))

    # Iterate through each frame of the GIF to get the last frame
    try:
        while True:
            current_frame = gif.tell()
            gif.seek(current_frame + 1)
    except EOFError:
        pass

    # Get the last frame of the GIF
    last_frame = gif.copy()

    # Save the last frame as a separate image
    last_frame.save("last_frame.png")

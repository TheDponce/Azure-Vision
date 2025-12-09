import os
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AI_SERVICE_ENDPOINT")
key = os.getenv("AI_SERVICE_KEY")
image_file = "images/street.jpg"

analyze_url = endpoint + "vision/v3.2/describe"

with open(image_file, "rb") as f:
    image_data = f.read()

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/octet-stream"
}

response = requests.post(
    analyze_url,
    headers=headers,
    data=image_data
)

result = response.json()
print(result)


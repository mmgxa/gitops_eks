import requests
import json
import base64


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def create_payload(base64_data):
    return {"instances": [{"data": base64_data}]}


encoded_image = encode_image_to_base64("human.jpg")
payload = create_payload(encoded_image)
headers = {
    "Host": "classifier.default.emlo.mmg",
    "Content-Type": "application/json",
}
load_balancer = "acfe54e4ece824c5b8e3d22ac40bdece-1538497744.us-west-2.elb.amazonaws.com"
url = f"http://{load_balancer}/v1/models/classifier:predict"


response = requests.request("POST", url, headers=headers, json=payload)

# print(response.headers)
print(f"Status: {response.status_code}, Result: {response.json()['predictions'][0]}")
# print(response.json())

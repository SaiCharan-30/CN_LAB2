import requests

try:
    # GET request
    response = requests.get("https://httpbin.org/get")
    print("GET Request:")
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    # POST request
    payload = {"name": "sai charan", "course": "Computer Networks"}
    response = requests.post("https://httpbin.org/post", data=payload)
    print("\nPOST Request:")
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)

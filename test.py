import requests

url = "http://authxspy.herokuapp.com/"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    print("Response Status Code:", response.status_code)
    print("Response Content Type:", response.headers.get("content-type"))
    print("Response Body:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)

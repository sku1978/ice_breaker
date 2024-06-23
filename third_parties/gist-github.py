import requests
import json

# URL of the raw JSON file in the GitHub Gist
# gist_url = 'https://gist.githubusercontent.com/username/gistid/raw/filename.json'
gist_url = "https://gist.githubusercontent.com/sku1978/0c1f0ef3fefbe600a675ebcf00fc1695/raw/4bce3b5a29601c180f09a7eec75283d92706bf7f/shaileshkmr-linkedin.json"

# Fetch the content from the URL
response = requests.get(gist_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON content
    data = json.loads(response.content)
    print(data)
else:
    print(f"Failed to retrieve the JSON file. Status code: {response.status_code}")


print(data["full_name"])

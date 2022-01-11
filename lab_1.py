import requests

# virtualenv Step 4
print(f"requests version: {requests.__version__}")

# curl step 5
response = requests.get('http://www.google.com/')
print(f"Headers: {response.headers}", f"Content: {response.content}", sep='\n\n')
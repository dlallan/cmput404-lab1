import os
import requests

SECTION_SEPARATOR = os.linesep*2

# virtualenv Step 4
print(f"requests version: {requests.__version__}", end=SECTION_SEPARATOR)

# curl Step 5
response = requests.get('http://www.google.com/')
print(f"Headers: {response.headers}",
      f"Content: {response.content}", sep=SECTION_SEPARATOR, end=SECTION_SEPARATOR)

# curl Step 10
with requests.get('https://raw.githubusercontent.com/dlallan/cmput404-lab1/main/lab_1.py') as response:
    quine_text = response.content.decode()
    print("Script contents:", quine_text, sep=os.linesep)

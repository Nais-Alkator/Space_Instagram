import requests

def save_image(file_name, url):
  response = requests.get(url, verify=False)
  response.raise_for_status()
  with open(file_name, 'wb') as file:
    file.write(response.content)
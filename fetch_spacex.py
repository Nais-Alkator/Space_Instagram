import requests
from save_image import save_image
from os import makedirs

def get_spacex_images_links():
  response = requests.get("https://api.spacexdata.com/v3/launches/latest")
  response.raise_for_status()
  latest_launches = response.json()
  latest_launches_links = latest_launches["links"]
  images_links = latest_launches_links["flickr_images"]
  return images_links

def fetch_spacex_last_launch():
  makedirs("images", exist_ok=True)
  images_links = get_spacex_images_links()
  for image_link_number, image_link in enumerate(images_links):
  	image_title = "images/image{}.jpg".format(image_link_number)
  	save_image(image_title, image_link)

if __name__ == "__main__":
  try:
    fetch_spacex_last_launch()
  except requests.exceptions.ConnectionError as error:
    exit("Can't get data from server:\n{0}".format(error))
  except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))

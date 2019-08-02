import requests
import argparse
from save_image import save_image
from os import makedirs

def get_hubble_image_links(image_id):
  hubble_api_url = "http://hubblesite.org/api/v3/image/{}".format(image_id)
  response = requests.get(hubble_api_url, verify=False)
  response.raise_for_status()
  image_data = response.json()
  image_data_files = image_data["image_files"]
  image_links = [element["file_url"] for element in image_data_files]
  return image_links

def get_link_extension(url):
  link_extension = url[-4::]
  return link_extension

def get_images_id_from_hubble_api_collection(collection):
  url = "http://hubblesite.org/api/v3/images/{}".format(collection)
  response = requests.get(url)
  response.raise_for_status()
  data = response.json()
  images_ids = [element["id"] for element in data]
  return images_ids

def download_image_from_hubble_api(image_id):
  makedirs("images", exist_ok=True)
  image_links = get_hubble_image_links(image_id)
  image_url = "http:" + image_links[-1]
  image_url_extension = get_link_extension(image_url)
  file_name = "images/{0}{1}".format(image_id, image_url_extension)
  save_image(file_name, image_url)

def download_images_from_hubble_api_collection(collection):
  images_ids = get_images_id_from_hubble_api_collection(collection)
  for image_id in images_ids:
  	image_id = str(image_id)
  	download_image_from_hubble_api(image_id)

def get_parser():
  parser = argparse.ArgumentParser(
	description='Скрипт предназначен для скачивания группы(коллекций) фотографий с Hubble API')
  parser.add_argument('collection', help='Название коллекции фотографий для скачивания', nargs="?", const=1, default="holiday_cards")
  return parser

if __name__ == "__main__":
  args = get_parser().parse_args()
  collection = args.collection
  try:
    download_images_from_hubble_api_collection(collection)
  except requests.exceptions.ConnectionError as error:
    exit("Can't get data from server:\n{0}".format(error))
  except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
from dotenv import load_dotenv
import instabot
import os
import argparse
from instabot import Bot
from os import listdir

load_dotenv()

INSTAGRAM_LOGIN = os.getenv("INSTAGRAM_LOGIN")
INSTAGRAM_PASSWORD= os.getenv("INSTAGRAM_PASSWORD")

def upload_photo_to_instagram(image_name, caption):
  bot = Bot()
  bot.login(username=INSTAGRAM_LOGIN, password=INSTAGRAM_PASSWORD)
  bot.upload_photo(image_name)

def upload_images_to_instagram(directory):
  filenames_list = listdir(directory)
  for filename in filenames_list:
  	name = "{0}/{1}".format(directory, filename)
  	upload_photo_to_instagram(name, caption=None)

def get_parser():
  parser = argparse.ArgumentParser(
	description='Скрипт предназначен для публикации фотографий в профиле Instagram')
  parser.add_argument('directory', help='Директория(папка), из которой будут загружаться фотографии', nargs="?", const=1, default="images")
  return parser

if __name__ == "__main__":
  args = get_parser().parse_args()
  directory = args.directory
  upload_images_to_instagram(directory)

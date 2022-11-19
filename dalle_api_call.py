import openai
from .secrets import DALLE_API_KEY

openai.api_key = DALLE_API_KEY


def create_images(prompt):
  response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
  )
  image_url = response
  # ['data'][0]['url']

  return response
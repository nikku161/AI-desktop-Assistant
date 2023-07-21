
import os
import openai
from apikey import ak

openai.api_key = ak

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[],
  temperature=1,
  max_tokens=515,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
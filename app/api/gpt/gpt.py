import os
from openai import OpenAI

#############################################
### The main function of the GPT package. ###
client = OpenAI(api_key="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")

def gpt(message):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=message
  )
  print(completion.choices[0].message.content)
  return(completion.choices[0].message.content)

# gpt([{"role": "user", "content": "Hi"}])

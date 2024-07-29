import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

'''
for model in genai.list_models():
  if 'generateContent' in model.supported_generation_methods:
    print(model.name)
'''

file = open("output.txt", "w+")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is the meaning of life?")

file.write(response.prompt_feedback)
file.write(to_markdown(response.text).data)
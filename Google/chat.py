import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

while True:
    prompt = input("Enter your prompt : ")
    response = model.generate_content(prompt)
    print(response.text)
    print()
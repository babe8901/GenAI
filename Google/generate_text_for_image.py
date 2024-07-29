import PIL.Image
import google.generativeai as genai
import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

genai.configure(
    api_key=os.environ["GOOGLE_API_KEY"]
)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content()
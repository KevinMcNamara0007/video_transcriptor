import openai
from config import LLM_API_URL, API_KEY

openai.api_key = API_KEY

def summarize(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Summarize the following text: {text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def classify(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Classify the following text: {text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def infer(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Infer information from the following text: {text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def generate_business_points(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate business talking points from the following text: {text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()


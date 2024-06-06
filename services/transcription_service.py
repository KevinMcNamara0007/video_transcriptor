import requests
from config import TRANSCRIPTION_API_URL, API_KEY

def transcribe_audio(mp4_url):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {'url': mp4_url}
    response = requests.post(f'{TRANSCRIPTION_API_URL}/transcribe', headers=headers, json=data)
    return response.json()['transcript']


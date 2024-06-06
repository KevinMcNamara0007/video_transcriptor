import requests
from config import GONG_API_URL, API_KEY

def get_mp4_feed():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{GONG_API_URL}/mp4_feed', headers=headers)
    return response.json()

def get_email_feed():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{GONG_API_URL}/email_feed', headers=headers)
    return response.json()


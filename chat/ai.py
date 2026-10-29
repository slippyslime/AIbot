import os
import requests

API_URL = 'https://openrouter.ai/api/v1/chat/completions'
DEFAULT_MODEL = 'openrouter/free'
TIMEOUT_SECONDS = 60


def ask(question: str) -> str:
    api_key = os.environ.get('OPENROUTER_API_KEY', '').strip()
    response = requests.post(
        API_URL,
        headers={'Authorization': f'Bearer {api_key}'},
        json={
            'model': os.environ.get('OPENROUTER_MODEL', DEFAULT_MODEL),
            'messages': [{'role': 'user', 'content': question}],
        },
        timeout=TIMEOUT_SECONDS,
    )
    content = response.json()['choices'][0]['message']['content']

    return content.strip()
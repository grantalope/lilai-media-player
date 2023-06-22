import requests
import json

# Define the ElevenLabs TTS API endpoint
tts_api_endpoint = "https://api.elevenlabs.io/tts/v1/synthesize"

# Specify your ElevenLabs TTS API Key
api_key = "3de21c41f722cea4f0104495120ccfdb"

# Specify the text to be converted to speech
ad_text = "Hello, this is Huell Howser. Do you want to own a piece of California history? You can with Huell Coins! Each Huell Coin is a unique, blockchain-secured digital asset. It's more than just a coin, it's a digital keepsake of the Golden State. Purchase yours today on OpenSea!"

# Get voice ID for HuellHowser
voice_id_endpoint = "https://api.elevenlabs.io/v1/voices"
headers = {
    "Authorization": api_key,
    "Accept": "application/json"
}
response = requests.get(voice_id_endpoint, headers=headers)
voice_id = response.json()["voice_id"]  # You might need to adjust this line based on the actual response structure

# Specify the TTS API request body
body = {
    "input": {
        "text": ad_text
    },
    "voice": {
        "name": voice_id
    },
    "audioConfig": {
        "audioEncoding": "MP3"
    }
}

headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}

# Make a POST request to the ElevenLabs TTS API to synthesize speech
response = requests.get(voice_id_endpoint, headers=headers)
voices = response.json()  # Assuming the response is a list of voices

# Find the 'HuellHowser' voice and get its ID
voice_id = None
for voice in voices:
    if voice['name'] == 'HuellHowser':
        voice_id = voice['voice_id']
        break

if voice_id is None:
    print("Failed to find 'HuellHowser' voice")
    return
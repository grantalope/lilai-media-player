import requests
import json

# Load the characters from the JSON file
with open('characters.json') as f:
    characters = json.load(f)["players"]

# Specify your ElevenLabs TTS API Key
api_key = "3de21c41f722cea4f0104495120ccfdb"

# Function to generate speech for a given character
def generate_speech(character_name, text):
    # Find the character by name
    character = next((c for c in characters if c["name"] == character_name), None)
    if character is None:
        print(f"No character found with name {character_name}")
        return

    # Get the voice_id for the character
    voice_id = character["voice_id"]

    # Define the ElevenLabs TTS API endpoint
    tts_api_endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    # Specify the TTS API request body
    body = {
      "text": text,
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 1,
        "similarity_boost": 1
      }
    }

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    # Make a POST request to the ElevenLabs TTS API to synthesize speech
    response = requests.post(tts_api_endpoint, headers=headers, json=body, stream=True)

    if response.status_code == 200:
        with open(f'{character_name}_audio.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"{character_name} audio generated successfully.")
    else:
        print(f"Failed to generate audio for {character_name}:", response.json())

# Example usage
generate_speech("Huell Howser", "Hello, this is Huell Howser. Do you want to own a piece of California history?")

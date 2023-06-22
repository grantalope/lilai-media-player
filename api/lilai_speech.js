const axios = require('axios');
const fs = require('fs');

// Specify your ElevenLabs TTS API Key
const api_key = "3de21c41f722cea4f0104495120ccfdb";

// Function to generate speech for a given character
async function generate_speech(character_name, voice_id, text) {
    // Define the ElevenLabs TTS API endpoint
    const tts_api_endpoint = `https://api.elevenlabs.io/v1/text-to-speech/${voice_id}/stream`;

    // Specify the TTS API request body
    const body = {
        text: text,
        model_id: "eleven_monolingual_v1",
        voice_settings: {
            stability: 1,
            similarity_boost: 1
        }
    };

    const headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    };

    // Make a POST request to the ElevenLabs TTS API to synthesize speech
    try {
        const response = await axios.post(tts_api_endpoint, body, { headers: headers, responseType: 'stream' });
        const writer = fs.createWriteStream(`${character_name}_audio.mp3`);
        response.data.pipe(writer);
        console.log(`${character_name} audio generated successfully.`);
    } catch (error) {
        console.log(`Failed to generate audio for ${character_name}:`, error.response.data);
    }
}

// Serverless function to generate speech
module.exports = async (req, res) => {
    const { character_name, voice_id, text } = req.body;
    await generate_speech(character_name, voice_id, text);
    res.status(200).send('Audio generated successfully.');
};

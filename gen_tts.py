from google.cloud import texttospeech


def text_to_wav(text,filename):
    voice_name = 'en-US-Wavenet-C'
    text_input = texttospeech.SynthesisInput(ssml=text)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code='en-US', name=voice_name
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        pitch=-2,
        speaking_rate=1
    )

    client = texttospeech.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )

    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{filename}"')

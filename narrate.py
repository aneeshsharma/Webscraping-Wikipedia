from google.cloud import texttospeech
import vlc
import time
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/text2speech_token.json'


def narrate(text):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config)

    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    player = vlc.MediaPlayer('output.mp3')
    player.play()
    time.sleep(3)
    while player.is_playing():
        time.sleep(1)

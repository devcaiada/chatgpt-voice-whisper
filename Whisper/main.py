import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import os
import openai
from gtts import gTTS
import simpleaudio as sa

# Configura a chave da API da OpenAI
os.environ['OPENAI_API_KEY'] = 'SUA CHAVE AQUI'
language = 'pt'


# Função para gravar áudio
def record_audio(duration=5, sample_rate=44100, file_name='request_audio.wav'):
    print("Ouvindo...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)  # Grava em mono
    sd.wait()  # Aguarda a gravação terminar
    write(file_name, sample_rate, np.int16(recording))  # Salva o áudio como arquivo WAV
    print(f"Áudio gravado e salvo como {file_name}")
    return file_name


# Função para tocar o áudio gravado
def play_audio(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Espera até que o áudio termine de tocar


# Grava o áudio por 5 segundos
record_file = record_audio()

# Utiliza a biblioteca Whisper para transcrever o áudio gravado
model = whisper.load_model("small")
result = model.transcribe(record_file, fp16=False, language=language)
transcription = result["text"]
print("Transcrição:", transcription)

# Usa a API do OpenAI GPT para processar a transcrição
openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.ChatCompletion.create(
    model="gpt-3.5",
    messages=[{"role": "user", "content": transcription}]
)

# Obtém a resposta gerada pelo ChatGPT
chatgpt_response = response.choices[0].message.content
print("Resposta do ChatGPT:", chatgpt_response)

# Converte a resposta em fala usando gTTS
gtts_object = gTTS(text=chatgpt_response, lang=language, slow=False)
response_audio = "response_audio.wav"
gtts_object.save(response_audio)
print(f"Resposta sintetizada salva como {response_audio}")

# Toca o áudio da resposta
play_audio(response_audio)

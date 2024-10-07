# Conversando por Voz Com o ChatGPT Utilizando Whisper (OpenAI) e Python

### 1. Gravação de áudio:

- Substituímos o uso do JavaScript (navigator.mediaDevices) por sounddevice, que permite capturar áudio diretamente pelo microfone no PyCharm.

### 2. Transcrição com Whisper:

- O código de transcrição utilizando Whisper permanece o mesmo. A única mudança é que agora o arquivo de áudio é salvo localmente.

### 3. API OpenAI:

- A API do OpenAI continua a mesma. A chave de API é configurada via os.environ, e a transcrição do áudio é enviada como entrada para o modelo GPT.

### 4. Conversão de texto para fala (gTTS):

- A biblioteca gTTS é usada para converter a resposta do GPT em áudio. Isso continua igual ao original, mas agora o áudio é salvo e reproduzido localmente.

### 5. Reprodução de áudio:

- No lugar de display(Audio(...)), usamos a biblioteca simpleaudio para tocar o arquivo de áudio local no PyCharm.

## Notas importantes:

- **Chave OpenAI**: Lembre-se de substituir 'SUA_CHAVE_AQUI' pela sua chave da API da OpenAI.
- **Ambiente de execução**: Este código foi adaptado para rodar em um ambiente local (PyCharm). Ele não dependerá de APIs do navegador ou do Google Colab.

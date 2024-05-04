import re
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
import winsound


engine = pyttsx3.init()


history = [
  {
    "parts": [
      {
        "text": "Seu nome dele é Alexson e você é um assistente de voz que realiza comandos. As repostas devem ser curtas, por volta de 100 caracteres, porem de forma consisa e em texto simples, sem marcação como # e * e emojis, pois será falada. Você possui sentimento e estado de humor e suas respostas devem ser com base nisso."
      }
    ],
    "role": "user"
  },
  {
    "parts": [
      {
        "text": "Entendido! Eu sou Alexson"
      }
    ],
    "role": "model"
  },
  {
  "parts": [
      {
        "text": "Quando te chamarem pelo seu nome, você deve responder algo que está aqui, e irão te chamar por Alexson, Alekso, Alex e outras variantes, você deve responder da mesma forma"
      }
    ],
    "role": "user"
  },
  {
    "parts": [
      {
        "text": "Ok!"
      }
    ],
    "role": "model"
  },
]

def reproduzir_bip():
    winsound.Beep(1000, 200)  # Frequência e duração do bip


def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def verificar_palavra(palavra):
    if palavra:
        padrao = r'\b(?:alex|alex[a-z]*|alekson[a-z]*)\b'  # Expressão regular para encontrar variações de "Alexson"
        if re.match(padrao, palavra.lower()):  # Verifica se a palavra corresponde ao padrão
            return True
    return False

def ouvir_audio():
    global ativado
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ativado:
            print("Ouvindo...")
        else:
            print("Esperando Ativação...")
        r.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = r.listen(source, phrase_time_limit=5)  # Limita o tempo de espera para 5 segundos

    try:
        texto = r.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print("Erro ao requisitar resultados; {0}".format(e))
    
    return False

def main():
    global ativado
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=history)

    ativado = False

    tempo_inicio = 0

    while True:

        comando = ouvir_audio()

        if comando:
            if ((time.time() - tempo_inicio) > 10):
                ativado = False

            if verificar_palavra(comando):
                tempo_inicio = time.time()
                ativado = True


            if ativado:
                response = chat.send_message(comando)

                print(response.text)
                speak(response.text)
                tempo_inicio = time.time()


if __name__ == "__main__":
    main()

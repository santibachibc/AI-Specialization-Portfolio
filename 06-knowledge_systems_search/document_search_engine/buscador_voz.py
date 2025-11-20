import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import os

def hablar(texto, filename="respuesta.mp3"):
    tts = gTTS(text=texto, lang='es')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Di tu consulta:")
        audio = recognizer.listen(source)

        try:
            consulta = recognizer.recognize_google(audio, language='es-ES')
            print(f"🗣️ Has dicho: {consulta}")
            return consulta
        except sr.UnknownValueError:
            print("❌ No entendí. Intenta de nuevo.")
            hablar("No entendí. Intenta de nuevo.")
        except sr.RequestError:
            print("❌ Error al conectar con el servicio de reconocimiento.")
            hablar("Error al conectar con el servicio de reconocimiento.")
    return None

def buscar(consulta):
    ix = open_dir("indexdir")
    qp = QueryParser("content", schema=ix.schema)
    query = qp.parse(consulta)

    with ix.searcher() as searcher:
        results = searcher.search(query, limit=5)
        if results:
            respuesta = f"He encontrado {len(results)} documentos:"
            print(respuesta)
            for r in results:
                print(f" - {r['title']}")
                respuesta += f" {r['title']},"
        else:
            respuesta = "No encontré ningún documento relacionado."
            print(respuesta)

        hablar(respuesta)

if __name__ == "__main__":
    hablar("Bienvenido al buscador de documentos por voz.")
    while True:
        consulta = escuchar()
        if consulta:
            if consulta.lower() in ['salir', 'terminar', 'adiós']:
                hablar("Hasta luego.")
                break
            buscar(consulta)

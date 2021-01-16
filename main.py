import speech_recognition as sr


def get_speak():
    mic = sr.Recognizer()
    text = None

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")
        audio = mic.listen(source)
        print("Processando...")

    try:
        text = mic.recognize_google(audio, language='pt-BR')
        print(">> " + text)
        text = text.upper()
    except:
        print("Áudio não reconhecido!")
    return text

text = get_speak()

if "OLÁ" in text:
    print("Saudações")

print("Finalizado.")

from translate import Translator
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen_for_audio():
    with sr.Microphone() as source:
        print('Clearing the background noises..')
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print('Waiting for your message')
        try:
            audio = recognizer.listen(source, timeout=5)
            print('Done recording')
            return audio
        except sr.WaitTimeoutError:
            print("Timeout. No speech detected. Please try again.")
            return None

def trans():
    audio = listen_for_audio()

    if audio:
        try:
            print('Recognizing')
            result = recognizer.recognize_google(audio, language='en')
            print('You said:', result)

            langinput = input('Type the language code you want to translate: ')
            translator = Translator(to_lang=langinput)
            
            try:
                translate_text = translator.translate(result)
                print('Translation:', translate_text)

                engine.say(translate_text)
                engine.runAndWait()
            except Exception as ex:
                print(f"Error translating: {ex}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        trans()  # Recursive call to continue the translation process

# Call the trans function to start the translation process
trans()

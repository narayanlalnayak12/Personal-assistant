import speech_recognition as sr
import output_module
r=sr.Recognizer()
def spc_to_text():
    with sr.Microphone() as source:
        # output_module.output("Narayan say something.")
        print("speak now")
        audio=r.listen(source)
        query=r.recognize_google(audio)
        return query
# spc_to_text()
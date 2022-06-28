from gtts import gTTS  
from playsound import playsound  

language = 'en'  
def speech(txt):
    obj = gTTS(text=str(txt), lang=language, slow=False)
    obj.save("assitant.mp3")
    playsound("assitant.mp3")


# speech("good morning ,how are you doing")
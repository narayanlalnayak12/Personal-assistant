import webbrowser as web
import os
def open_facebook():
    web.open("https://facebook.com")

def open_google():
    web.open("https://google.com")

def close_browser():
    os.system("pkill chrome")
# open_facebook()
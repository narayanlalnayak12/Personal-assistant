import urllib.request
import wikipedia
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False


def check_on_wikipedia(query):
    query=query.replace("who is","")
    query=query.replace("what is","")
    query=query.replace("do you know","")
    query=query.replace("tell me about","")

    query=query.strip()

    try:
        data=wikipedia.summary(query,sentences=1)
        # print(data)
        return data
    except Exception as e:
        # print(e)
        return ""
# check_on_wikipedia('naredra modi')



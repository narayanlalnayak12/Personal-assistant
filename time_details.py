from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H hours, %M minutes ,%S seconds")

def get_time():
    return 'Time is ' +current_time
# print("Current Time =", current_time)
# print(get_time())

def get_hour():
    now = datetime.now()
    current_time = now.strftime("%H")
    return current_time

# print(get_hour())
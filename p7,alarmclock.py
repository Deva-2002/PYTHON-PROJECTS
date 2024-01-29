
from playsound import playsound

import time

def alarm(seconds):
    time_elapsed=0

    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60

        print(f"{minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

minutes=int(input("how many minutes to wait: "))
seconds=int(input("how many seconds to wait: "))
total_second=minutes*60*seconds


alarm(total_second)

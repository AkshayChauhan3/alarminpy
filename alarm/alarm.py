import datetime
import time
import playsound #install playsound module in your device (write : 'pip install playsound' in your terminal)

def set_alarm(alaram_time) :
    print(f"Alaram is set for time : {alaram_time}")
    audio = "morning_alarm.mp3"
    is_running = True

    while is_running:
        currunt_time = datetime.datetime.now().strftime("%H : %M : %S")
        print(currunt_time)
        time.sleep(1)

        if currunt_time == alaram_time :
            print("Alarm is Ringing")
            playsound.playsound(audio)
            is_running = False


if __name__ == "__main__" :
    alaram_time = input("Enter the Alaram Time (in HH : MM : SS form) : ")
    set_alarm(alaram_time)

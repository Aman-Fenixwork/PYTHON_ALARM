from playsound import playsound
import time 

CLEAR = "\033[2J" #Escape sequence for clearing terminal
CLEAR_AND_RETURN = "\033[H" 

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds :
        time.sleep(1);
        time_elapsed += 1
        total_time = seconds - time_elapsed;
        minutes = total_time // 60
        seconds_left = total_time % 60;
        
        print(f'{CLEAR_AND_RETURN}{minutes:02d}:{seconds_left:02d}')

input_minutes = int(input("enter how many minutes :")) * 60
input_seconds = int(input("enter how many seconds :")) 

alarm(input_minutes+input_seconds)

#Practice
# from playsound import playsound #for playing sounds
# import time 

# CLEAR = "\033[2J" #Escape sequence for clearing terminal
# CLEAR_AND_RETURN = "\033[H" 
# def alarm(seconds):
#     time_passed = 0
#     print(CLEAR)
#     while time_passed < seconds:
#         time.sleep(1)  #wait for one second
#         time_passed += 1 #increment the timer

#         time_left = seconds - time_passed
#         minutes_left = time_left // 60
#         seconds_left = time_left % 60
#         print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
#     playsound("Broken_Instrumental_Ringtone_Sad_Instrumental_Rin.mp3")

# user_ip_minutes  = int(input("Enter minutes : "));
# user_ip_seconds = int(input("Enter seconds : "));
# total_time = user_ip_minutes * 60 + user_ip_seconds

# alarm(total_time)
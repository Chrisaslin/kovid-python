# import the time & playsound module
# import the time & playsound module
import time
from playsound import playsound 
  
# define the countdown timer function
def countdown_timer(seconds):
    
    while seconds > 0:       

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        seconds -= 1
      
    print('Time Up!')

    playsound('C:/Users/91880/Downloads/PRO-C110-Teacher-Reference-Code-AA-main-main (1)/PRO-C110-Teacher-Reference-Code-AA-main-main/mixkit-sound.wav')
  
  
# input time in seconds
seconds = input("Enter the time in number of seconds: ")
  
# function call
countdown_timer(int(seconds))
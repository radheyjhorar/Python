import time
import gtts 
from playsound import playsound 


timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
mints = int(time.strftime('%M'))

def greets():
    if hour > 5 and hour < 12:
        return "Good Morning Sir, Welcome"
    elif hour > 12 and hour < 18:
        return "Good Afternoon Sir, Welcome"
    elif hour > 18 and hour < 22:
        return "Good Evening Sir, Welcome"
    elif hour > 22 and hour < 5:
        return "Good Night Sir, Welcome"
    else:
        return "welcome sir, thanks for visit"
        
greet = greets()

t1 = gtts.gTTS("Its " + str(hour) + ":" + str(mints) + ", " + greet)
t1.save("timeAndGreet.mp3")
playsound('timeAndGreet.mp3')
print("Its " + str(hour) + ":" + str(mints) + ", " + greet)

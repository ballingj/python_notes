#####################################################
# text to speech module does not work under linux WSL
# install two modules:
# 1. pip install -U textblob
# 2. pip install pyttsx3
#######################################################

from textblob import TextBlob
import pyttsx3

print("""
 __  __  _         _       _                          __  __        __              _    
|  \/  |(_) _ __  (_) ___ | |_  _ __  _   _    ___   / _| \ \      / /  ___   _ __ | | __
| |\/| || || '_ \ | |/ __|| __|| '__|| | | |  / _ \ | |_   \ \ /\ / /  / _ \ | '__|| |/ /
| |  | || || | | || |\__ \| |_ | |   | |_| | | (_) ||  _|   \ V  V /  | (_) || |   |   <
|_|  |_||_||_| |_||_||___/ \__||_|    \__, |  \___/ |_|      \_/\_/    \___/ |_|   |_|\_\\
                                      |___/

""")
engine = pyttsx3.init()
engine.say("Hello employee 478125.  We hope you had a great day of work.  It's time to submit your employee wellness statements.")
engine.runAndWait()

print("Enter your employee wellness statement: ")
phrase = input("> ")
blob = TextBlob(phrase)
print(blob.sentiment.polarity)
while blob.sentiment.polarity < 0.5:
    engine.say("employee 478125, that was not a very positive employee wellness statement. Try to be more positive please: ")
    engine.runAndWait()
    print("More positive please: ")
    phrase = input("> ")
    blob = TextBlob(phrase)
    print(blob.sentiment.polarity)

print("We appreciate you too!")
engine.say("Employee 478125, thank you for such a kind and positive statement!  We here at the ministry of work appreciate you too!  Have a great day!")
engine.runAndWait()

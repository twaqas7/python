# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

#Little fun with github copilot 

import pyttsx3
import datetime
import random

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user based on the current time
def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# Provide a random programming tip
def programming_tip():
    tips = [
        "Keep your code clean and readable.",
        "Comment your code to explain complex logic.",
        "Practice makes perfect. Keep coding!",
        "Always test your code with different inputs.",
        "Learn to use version control systems like Git."
    ]
    speak(random.choice(tips))

# Main function
def main():
    speak("Welcome to the world of Python Programming")
    greet_user()
    programming_tip()

# Run the main function
if __name__ == "__main__":
    main()
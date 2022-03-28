# The library downloaded and used was pyttsx3

import pyttsx3


# Variable to initialize the installed library for the speech to text.
speech = pyttsx3.init()


# This helps to take any input and turn it into a string. For better output.
answer = input("What is it that you want to convert?")


# The say function converts what text you give into speech.
speech.say(answer)

#This exits from the program.
speech.runAndWait()


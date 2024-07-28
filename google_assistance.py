import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

r = sr.Recognizer()

machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def get_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            speech = r.listen(source)
            instruction = r.recognize_google(speech)
            instruction = instruction.lower()
            if "giri" in instruction:
                instruction = instruction.replace('giri', "")
                print(instruction)
                return instruction
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None


def play_instruction():
    instruction = get_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time' + time)
        print(time)

    elif "open google" in instruction:
        talk("Opening Google ")
        webbrowser.open("www.google.com")

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk('Today date ' + date)
        print(date)

    elif "send message" in instruction:
        pywhatkit.sendwhatmsg("+918523828196", "Happy Birthday", 23, 57)
        print("sent msg")


    elif "open star" in instruction:
        pywhatkit.search("Altiostar Bengaluru")
        print("searching")

    elif 'how are you' in instruction:
        talk('I am fine, how about you')
        print("Iam fine what about you")

    elif 'what is your name' in instruction:
        talk('I am giri, what can i do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)


play_instruction()

import datetime
import time

name=input("please enter your name:")
presentHour=datetime.datetime.now().hour
if 5 <= presentHour <=11:
    print("Good Morning",name)
elif 11<= presentHour <=17:
    print("Good Afternoon",name)
elif 17<= presentHour <=20:
    print("Good Evening",name)
else:
    print("Good Night",name)

print("Namaste! Welcome to your Buddy Chatbot")
print("you can ask me basic question, Type 'bye' to exit the chatbot.")


#chatbot memory creation[dictionary of responses]

responses = {
    "hello": "hello! how can I help you?",
    "how are you?": "i am very fine, Thank you",
    "who are you?": "I am smart AI chatbot",
    "motivate me": "you can do it, just believe in yourself",
    "happy": "great!to hear that",
    "function kya hote hai": "jakr chapter 7 padho"
    
}

    
# method/function to get response of bot

def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "i am not able to tell  that yet. mai jald hi yeh sikh lunga"
#take user input
while True:
    userInput= input("please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break

        
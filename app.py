from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time


application = Flask(__name__)

MyName = "Friday"
chatbot = ChatBot(MyName, storage_adapter="chatterbot.storage.SQLStorageAdapter", logic_adapters=["chatterbot.logic.MathematicalEvaluation","chatterbot.logic.BestMatch"])
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.export_for_training('./export.yml')
trainer.train("chatterbot.corpus.english.conversations")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english")
#trainer.export_for_training('./my_export.json')
#userinput="What is your name"
#if userinput == 'What is your name':
#    output = "I m "+myname
#else:
#    output=str(chatbot.get_response(userinput))
#print(output)


@application.route("/")
def home():
    return render_template("index.html")


@application.route("/get")
def bot_inout():
    subtext = request.args.get('msg')
    message=str(subtext)
    message=message.lower()
    if message == 'what is your name' or message == 'what is your name?':
        reply = "I'm Friday"
        return reply
    elif message == 'what is my name' or message == 'what is my name ?':
        reply = "I'm not an astrologer"
        return reply
    elif message.__contains__('bye') or message == 'see you':
        reply = "It was good to spend time with you. Bye Bye!!!"
        return reply
    elif message.__contains__('fuck'):
        reply = 'Dont speak bad words!!!\nI m really disappointed!!!'
        return reply
    elif message == "okay" or message == "fine" or message == "oh okay" or message == "ohokay":
        reply = 'Hmm'
        return reply

    else:
        return str(chatbot.get_response(subtext))


if __name__ == '__main__':
    application.run()
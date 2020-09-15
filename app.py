from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import datetime
#from datetime package import datetime module
import pytz


application = Flask(__name__)

MyName = "Alice"
chatbot = ChatBot(MyName, storage_adapter="chatterbot.storage.SQLStorageAdapter", logic_adapters=["chatterbot.logic.MathematicalEvaluation","chatterbot.logic.BestMatch"])
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.export_for_training('./export.yml')
trainer.train("chatterbot.corpus.english.conversations")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english")
ist=pytz.timezone('Asia/Kolkata')
DateTime = datetime.now()
Time= datetime.now(ist)
Date=str(DateTime.strftime("%d"))+str(DateTime.strftime("%B"))+str(DateTime.year)
Time=Time.strftime('%H:%M:%S')
#print(x.year)
#print(x.strftime("%A"))
#print(x.strftime("%d"))
#print(x.strftime("%m"))
#print(x.strftime("%B"))
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
    if message.__contains__('what is your name'):
        reply = "I m "+MyName
        return reply
    elif message.__contains__('what is my name'):
        reply = "I'm not an astrologer"
        return reply
    elif message.__contains__('bye') or message == 'see you':
        reply = "It was good to spend time with you. Bye Bye!!!"
        return reply
    elif message == "okay" or message == "fine" or message == "oh okay" or message == "ohokay":
        reply = 'Hmm'
        return reply
    elif message.__contains__('what is the time') or message.__contains__("what's the time"):
        reply = Time
        return reply
    elif (message.__contains__("today's") or message.__contains__("today")) and message.__contains__('date'):
        reply = Date
        return reply
    else:
        return str(chatbot.get_response(subtext))


if __name__ == '__main__':
    application.run()
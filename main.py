from calendar import c
from cmath import phase
from flask import Flask, request
import requests, json
import asyncio





def send_message(chat_id, text):
    method = "sendMessage"

    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


def button1(chat_id):
    method = "sendMessage"
    
    #reply_markup={"KeyboardButton":["text":"fff", "one_time_keyboard":True]}
    url = f"https://api.telegram.org/bot{token}/{method}"


    data = {"chat_id": chat_id, "text": "отправьте свой номер телефона, используя кнопку ниже", "reply_markup": json.dumps({"keyboard": [
        [{
        "text": "Отправить",
        "request_contact":True,
        
    }]], "one_time_keyboard":True})}

    requests.post(url, data=data)



def send_message(chat_id, text):
    method = "sendMessage"

    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)




app = Flask(__name__)
token = "5109358782:AAF5rOAFzLaPSWWvDDAi_DqNq4fB3elEmNQ"
@app.route("/", methods=["POST"])
async def receive_update():
    r = request.json
    if 'contact' in r['message']:
        chat_id = r['message']['chat']['id']
        phone = r['message']['contact']['phone_number']
        print(r['message']['contact']['phone_number'])
        send_message(chat_id, phone)
    try:
        chat_id = r['message']['chat']['id']
        text = r['message']['text']
        if text == "/start":
            button1(chat_id)
            print(r)
        return {"ok": True}
    except:
        return {"ok": True}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
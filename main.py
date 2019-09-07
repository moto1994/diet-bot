from flask import Flask, request, abort
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('QgQu1p3zPbyLJYeg0G4yZzKU8AGaCQbkanX+MutsQPccZDNClUTqgGD7DUh8MGMI/d4N+TnZHVzPf+Jo0Ro94ErSGx/X9JwreK3pflOourtohnsZHj2I1GqZ0TXq7Lz7aPXQrPzmGgfRkRvh/XbMfwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('979d7d85f9afe2034623bbfa9f9fe47b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  reply = create_reply(event.message.text)
  line_bot_api.reply_message(
  event.reply_token,
  TextSendMessage(text=reply))

def create_reply(user_text):
  apikey = "DZZ3wYssLsf2MnETFnuxfAjQFgQ1AkAh"
  client = pya3rt.TalkClient(apikey)
  res = client.talk(user_text)

  return res['results'][0]['reply']


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()

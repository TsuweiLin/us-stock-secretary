from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
# LINE BOT info
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

@app.route("/callback", methods=['POST'])
def callback():
  signature = request.headers['X-Line-Signature']
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)
  print(body)
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)
  return 'OK'

# TextMessage event
@handler.add(MessageEvent, message=TextMessage) # message=TextMessage、ImageSendMessage、VideoSendMessage、StickerSendMessage
def echo(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=event.message.text)
  )

if __name__ == "__main__":
  app.run()
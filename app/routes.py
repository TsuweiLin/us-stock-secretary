from app import app, handler, notify

from flask import request, abort
from linebot.exceptions import InvalidSignatureError

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
  signature = request.headers['X-Line-Signature']

  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'


@app.route("/callback/notify", methods=['GET'])
def callback_nofity():
  assert request.headers['referer'] == 'https://notify-bot.line.me/'
  code = request.args.get('code')
  state = request.args.get('state')

  access_token = notify.get_token(code, notify.client_id, notify.client_secret, notify.redirect_uri)

  return f'恭喜完成 LINE Notify 連動！請關閉此視窗。{access_token}'
  

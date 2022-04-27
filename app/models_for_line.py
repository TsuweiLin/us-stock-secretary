from app import handler, line_bot_api, notify
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# TextMessage event
@handler.add(MessageEvent, message=TextMessage) # message=TextMessage、ImageSendMessage、VideoSendMessage、StickerSendMessage
def echo(event):
  user_id = event.source.user_id
  username = line_bot_api.get_profile(event.source.user_id).display_name
  line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
  line_bot_api.reply_message(event.reply_token,TextSendMessage(text=notify.create_auth_link(user_id)))
  

def bot_push_message(to_user_id, text):
  line_bot_api.push_message(to_user_id, TextSendMessage(text))
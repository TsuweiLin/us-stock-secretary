from flask import Flask
from linebot import LineBotApi, WebhookHandler
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

from app import routes, models_for_line